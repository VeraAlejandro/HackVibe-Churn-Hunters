# models/afi.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Afi:
    id: Optional[int]
    name: str
    description: Optional[str]
    afi_type: Optional[str]
    faculty_id: int
    location: Optional[str]
    date: str  # 'YYYY-MM-DD'
    time: Optional[str]  # 'HH:MM'
    capacity: int
    created_by: Optional[int] = None
