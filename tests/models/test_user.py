from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid1

from typing import List, Optional
from psycopg2.extensions import connection

from Model.User import User
from ..conftest import TestDatabase

# User model attributes 
@dataclass
class UserModel:
    # uid: str
    name: Optional[str]
    email: str
    phone: Optional[str]
    password: Optional[str]
    major: Optional[str]
    degree: Optional[str]

# Dummy data
users: List[UserModel] = [
    UserModel(f"Name{i}", f"email{i}@gmail.com", f"{i}"*8, f"Password{i}", f"Major{i}", f"Degree{i}") for i in range(1, 9)
]

# Put unit tests here
def test_user(test_user_model: UserModel) -> None:
    fake_user: User = users[0]




    




