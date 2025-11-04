# models/user.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int]
    matricula: str
    role: str  # 'admin' | 'faculty' | 'student'
    password_hash: str
    name: str
    apellido_paterno: str
    apellido_materno: Optional[str] = None
    faculty_id: Optional[int] = None
    career_id: Optional[int] = None
