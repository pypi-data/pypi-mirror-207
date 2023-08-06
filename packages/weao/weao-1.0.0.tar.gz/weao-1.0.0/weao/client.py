"""     
__      _____  __ _  ___  
\ \ /\ / / _ \/ _` |/ _ \ 
 \ V  V /  __/ (_| | (_) |
  \_/\_/ \___|\__,_|\___/ 
                          
"""

import logging
from typing import Dict, List, Optional, Tuple

import aiohttp
from aiohttp import ClientSession

from .errors import UnsupportedExploit, ExploitNotFound, StatusUnavailable, LogsUnavailable
from .exploit import Exploit, Log
from .status import Status
from .constants import API


__all__: Tuple[str, ...] = ("Client",)

class Client:
    """
    Client Interfact For Innteracting With WEAO API

    Parameters
    -----------
    session: Optional[aiohttp.ClientSession]
        Client Session Used For HTTP Requests
    use_alternative_api: Optional[:class:`bool`]
        Whether To Use Alternative API URL
    """

    ___slots__ = (
        "session",
        "logger",
        "use_alt"
    )

    def __init__(self, session: Optional[ClientSession] = None, use_alternative_api: bool = False) -> None:
        self.logger = logging.getLogger(__name__)
        self.use_alt = use_alternative_api
        if session is None:
            self.session = aiohttp.ClientSession(headers=API.HEADERS)
        else:
            self.session = session

        
    async def _make_request(self, target: str) -> Dict:
        """

        Sends An HTTP /GET Request To WEAO API

        Parameters
        ----------
        target: :class:`str`
            API Endpoint

        Returns
        -------
        Dict
            JSON Response From API

        Raises
        ------
        HTTPError
            If The Request Failed
        """
        if self.use_alt:
            URL = API.ALTERNATIVE_BASE_URL
        else:
            URL = API.BASE_URL
        async with self.session.get(URL / target) as response:
            self.logger.debug(f"Sending HTTP /GET Request: {URL}/{target}")
            json = await response.json()
            return json
        
    async def cleanup(self) -> None:
        """Closes The Current Client Session

        Raises
        ------
        RuntimeError
            If The Session Was Already Closed
        """
        if self.session.closed:
            raise RuntimeError("Client Session Already Closed.")
        self.logger.debug("Closing Session")
        await self.session.close()
        self.logger.debug("Session Closed")

    async def get_exploit(self, exploit: str) -> Exploit:
        """
        Get Certain Exploit Status
        
        
        Parameters
        ----------
        exploit: :class:`str`
            Exploit Name, Must be a Valid Exploit Name
        
        Returns
        -------
        Exploit
            Exploit Class Object
        
        Raises
        ------
        UnsupportedExploit
            If Exploit Name is not Valid
        ExploitNotFound
            If Exploit couldn't be found, due to HTTP Error
        """
        if exploit not in API.Exploits:
            raise UnsupportedExploit(f"{exploit} is not a supported executor by WEAO")
        
        data = await self._make_request(f"status/{exploit}/")
        if data:
            return Exploit(data[0][exploit])
        else:
            raise ExploitNotFound(f"{exploit} Could Not Be Found, Likely due to Network Error")
        
    async def get_logs(self, exploit: str, amount: int) -> List[Log]:
        """
        Get Logs For Exploit
        
        
        Parameters
        ----------
        exploit: :class:`str`
            Name of Exploit, Must Be a Valid Exploit Name
        amount: :class:`int`
            Amount of Logs To Pull
        
        Returns
        -------
        List[Log]
            List of Logs Provided by API
        
        Raises
        ------
        ValueError
            If amount exceeds 50        
        UnsupportedExploit
            If Exploit Name is not Valid
        LogsUnavailable
            If Logs couldn't be found due to HTTP Error
        """
        if amount > API.LOG_LIMIT:
            raise ValueError(f"Log Value Too High, Should be > {API.LOG_LIMIT}, not {amount}")
        
        if exploit not in API.Exploits:
            raise UnsupportedExploit(f"{exploit} is not a supported executor by WEAO")
        
        data = await self._make_request(f"logs/{exploit}/{amount}")
        logs = []
        if data:
            for index, data, in enumerate(data, start=1):
                logs.append(Log(data[str(index)]))
        else:
            raise LogsUnavailable(f"Could Not Find Logs for {exploit} ({amount} amounts).")
        return logs
            
    async def get_status(self) -> Status:
        """
        Get Status of All Exploits
        
        
        Returns
        -------
        Status
            Object Representing Status of All Exploits
        """
        data = await self._make_request("status")
        if data:
            return Status(data)
        else:
            raise StatusUnavailable("Can't Find Status Right Now, Try Again Later.")