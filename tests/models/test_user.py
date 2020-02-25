from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from uuid import uuid1

from typing import List, Optional
from psycopg2.extensions import connection

from Model.User import User
from ..conftest import TestDatabase

# Session model attributes 
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
sessions: List[UserModel] = [
    UserModel(f"Name{i}", f"email{i}@gmail.com", f"{i}"*8, f"Password{i}", f"Major{i}", f"Degree{i}") for i in range(1, 9)
]

# Put unit tests here
def test_user(test_user: UserModel) -> None:
    u: User = users[0]

    # assert len(test_user.getUser()) == 0

    # assert test_user.addUser(**asdict(u)) == 0
    
    # assert len(test_user.getUser()) == 1



    




