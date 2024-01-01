import dataclasses


@dataclasses.dataclass
class User:
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

    first_name: str = None
    last_name: str = None
    age: int = 0
    salary: int = 0
    department: str = None
