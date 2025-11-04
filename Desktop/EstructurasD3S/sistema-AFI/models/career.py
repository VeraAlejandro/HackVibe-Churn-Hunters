# models/career.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Career:
    id: Optional[int]
    name: str
    faculty_id: int
    semesters: int = 8
