def from_code(code: int) -> AwsCrtError: ...

class AwsCrtError(Exception):
    def __init__(self, code: int, name: str, message: str) -> None:
        self.code: int = ...
        self.name: str = ...
        self.message: str = ...
