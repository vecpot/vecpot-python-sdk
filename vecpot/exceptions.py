from typing import Any, Optional, Dict


class CommonError(Exception):
    def __init__(self, message=None) -> None:
        super(CommonError, self).__init__(message)

        self.message = message

    def __str__(self) -> str:
        msg = self.message
        return msg

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={str(self)})"

class JSONError(CommonError):
    def __init__(self, message=None) -> None:
        super().__init__(message)

class ConnectionError(CommonError):
    def __init__(self, message=None) -> None:
        super().__init__(message)