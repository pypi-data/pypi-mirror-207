"""     
__      _____  __ _  ___  
\ \ /\ / / _ \/ _` |/ _ \ 
 \ V  V /  __/ (_| | (_) |
  \_/\_/ \___|\__,_|\___/ 
                          
"""

from typing import Tuple

__all__: Tuple[str, ...] = (
    "WEAOException",
    "UnsupportedExploit",
    "ExploitNotFound",
    "StatusUnavailable",
    "LogsUnavailable",
)

class WEAOException(Exception):
    """Generic API Exception For WEAO

    Attributes
    -----------
    message: :class:`str`
        The messages of this request
    """

    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(message)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} message={self.message}>"
    
class UnsupportedExploit(WEAOException):
    """Raised When A Executor Is Unsupported"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message)

class ExploitNotFound(WEAOException):
    """Raised When A Exploit Couldn't Be Found"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message)

class StatusUnavailable(WEAOException):
    """Raised When Status Call Failed"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message)

class LogsUnavailable(WEAOException):
    """Raised When Logs Call Failed"""

    def __init__(self, message: str) -> None:
        super().__init__(message=message)