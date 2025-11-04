from core.db import get_db

class FacultyManager:
    def __init__(self):
        self.db = get_db()

    # ==========================================
    # CREATE
    # ==========================================
    def create_faculty(self, name):
        """Crea una nueva facultad"""
        return self.db.execute_from_file("faculties_crud.sql", "create", (name,))

    # ==========================================
    # READ ALL
    # ==========================================
    def get_all_faculties(self):
        """Obtiene todas las facultades"""
        return self.db.execute_from_file("faculties_crud.sql", "read_all")

    # ==========================================
    # READ BY ID
    # ==========================================
    def get_faculty_by_id(self, faculty_id):
        """Obtiene una facultad por su ID"""
        result = self.db.execute_from_file("faculties_crud.sql", "read", (faculty_id,))
        return result[0] if result else None

    # ==========================================
    # UPDATE
    # ==========================================
    def update_faculty(self, faculty_id, name):
        """Actualiza el nombre de una facultad"""
        return self.db.execute_from_file("faculties_crud.sql", "update", (name, faculty_id))

    # ==========================================
    # DELETE
    # ==========================================
    def delete_faculty(self, faculty_id):
        """Elimina una facultad"""
        return self.db.execute_from_file("faculties_crud.sql", "delete", (faculty_id,))
