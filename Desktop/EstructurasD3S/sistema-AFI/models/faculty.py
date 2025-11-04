# models/faculty.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Faculty:
    id: Optional[int]
    name: str
    matricula: str
