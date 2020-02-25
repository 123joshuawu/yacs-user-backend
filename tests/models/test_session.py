from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid1

from typing import List, Optional
from psycopg2.extensions import connection

from Model.Session import Session
from ..conftest import TestDatabase

# Session model attributes 
@dataclass
class SessionModel:
    sessionid: str
    uid: int
    start_time: datetime 
    end_time: Optional[datetime]

# Dummy data
sessions: List[SessionModel] = [
    SessionModel(str(uuid1()), i, datetime(2000 + i, i, i, i, i, i, i, timezone.utc), None) for i in range(1, 9)
]

# Put unit tests here
def test_session(test_session_model: Session) -> None:
    fake_session: SessionModel = sessions[0]

    fake_session.sessionid = test_session_model.createSessionID()

    assert len(test_session_model.getSession()) == 0
    print()

    assert test_session_model.startSession(fake_session.sessionid, fake_session.uid, fake_session.start_time) == 0

    results = test_session_model.getSession()
    assert len(results) == 1
    assert results[0][0] == fake_session.sessionid
    assert results[0][3] is None 
  
    results = test_session_model.getSession(fake_session.sessionid)
    assert len(results) == 1
    assert results[0][0] == fake_session.sessionid
    assert results[0][3] is None

    assert test_session_model.endSession(fake_session.sessionid) == 0

    results = test_session_model.getSession(fake_session.sessionid)
    assert len(results) == 1
    assert results[0][0] == fake_session.sessionid
    assert results[0][3] is not None

    




