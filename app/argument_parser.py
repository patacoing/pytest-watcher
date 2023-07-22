import sys

class ArgumentParser:
    def __init__(self):
        if len(sys.argv) < 2:
            raise NotEnoughArgumentsError("Not enough arguments were provided.")
        self._args: list[str] = sys.argv[1:]

    @property
    def path_arg(self) -> str:
        return self._args[0]
    
    @property
    def pytest_args(self) -> str:
        return " ".join(self._args[1:])
    

class NotEnoughArgumentsError(Exception):
    def __init__(self, message: str):
        super().__init__(message)