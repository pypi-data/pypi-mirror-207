"""     
__      _____  __ _  ___  
\ \ /\ / / _ \/ _` |/ _ \ 
 \ V  V /  __/ (_| | (_) |
  \_/\_/ \___|\__,_|\___/ 
                          
"""

from typing import Dict, List, Final, Tuple, final

from yarl import URL

__all__: Tuple[str, ...] = ("API",)

@final
class API:
    """
    Class Representing Constants For API
    """
    BASE_URL: Final[URL] = URL("https://api.whatexploitsare.online")
    ALTERNATIVE_BASE_URL: Final[URL] = URL("https://api.weao.dev")
    HEADERS: Final[Dict[str, str]] = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50",
        "content-type": "application/json",
    }
    Exploits: Final[List[str]] = ["Synapse",
                            "Script-Ware",
                            "KRNL",
                            "DX9WARE",
                            "Electron",
                            "WeAreDevs API",
                            "Oxygen",
                            "Fluxus",
                            "Celestial",
                            "Comet",
                            "Elexe",
    ]
    LOG_LIMIT: Final[int] = 50