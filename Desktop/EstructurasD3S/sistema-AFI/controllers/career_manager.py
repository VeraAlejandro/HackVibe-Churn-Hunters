from core.db import get_db

class CareerManager:
    def __init__(self):
        self.db = get_db()

    # ==========================================
    # CREATE
    # ==========================================
    def create_career(self, name, id_faculty, semesters):
        """Crea una nueva carrera asociada a una facultad"""
        return self.db.execute_from_file("careers_crud.sql", "create", (name, id_faculty, semesters))

    # ==========================================
    # READ ALL
    # ==========================================
    def get_all_careers(self):
        """Obtiene todas las carreras junto con su facultad"""
        return self.db.execute_from_file("careers_crud.sql", "read_all")

    # ==========================================
    # READ BY ID
    # ==========================================
    def get_career_by_id(self, id_career):
        """Obtiene una carrera específica por su ID"""
        result = self.db.execute_from_file("careers_crud.sql", "read", (id_career,))
        return result[0] if result else None

    # ==========================================
    # UPDATE
    # ==========================================
    def update_career(self, id_career, name, id_faculty, semesters):
        """Actualiza los datos de una carrera"""
        return self.db.execute_from_file("careers_crud.sql", "update", (name, id_faculty, semesters, id_career))

    # ==========================================
    # DELETE
    # ==========================================
    def delete_career(self, id_career):
        """Elimina una carrera"""
        return self.db.execute_from_file("careers_crud.sql", "delete", (id_career,))
