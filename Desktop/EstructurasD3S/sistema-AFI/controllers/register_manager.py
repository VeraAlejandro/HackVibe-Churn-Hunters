# controllers/user_manager.py
from core.db import get_db

class UserManager:
    def __init__(self):
        self.db = get_db()

    # ==========================================
    # CREATE USER
    # ==========================================
    def create_user(self, matricula, password_hash, name, apellido_paterno, apellido_materno,
                    role, faculty_id=None, career_id=None):
        """Crea un nuevo usuario"""
        return self.db.execute_from_file(
            "users_crud.sql", 
            "create",
            (matricula, password_hash, name, apellido_paterno, apellido_materno, role, faculty_id, career_id)
        )

    # ==========================================
    # READ USERS
    # ==========================================
    def get_all_users(self):
        """Obtiene todos los usuarios"""
        return self.db.execute_from_file("users_crud.sql", "read_all")

    def get_user_by_matricula(self, matricula):
        """Obtiene un usuario por su matrícula"""
        result = self.db.execute_from_file("users_crud.sql", "read_by_matricula", (matricula,))
        return result[0] if result else None
