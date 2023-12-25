import dataclasses


@dataclasses.dataclass
class User:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
