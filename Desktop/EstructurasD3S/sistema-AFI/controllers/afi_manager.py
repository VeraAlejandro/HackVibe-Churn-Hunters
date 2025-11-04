from core.db import get_db

class AFIManager:
    def __init__(self):
        self.db = get_db()

    # ==========================================
    # CREATE
    # ==========================================
    def create_afi(self, name, date, time, location, id_faculty, type_afi, max_capacity):
        """Crea una nueva AFI asociada a una facultad"""
        return self.db.execute_from_file(
            "afis_crud.sql",
            "create",
            (name, date, time, location, id_faculty, type_afi, max_capacity)
        )

    # ==========================================
    # READ ALL
    # ==========================================
    def get_all_afis(self):
        """Obtiene todas las AFIs con información de la facultad"""
        return self.db.execute_from_file("afis_crud.sql", "read_all")

    # ==========================================
    # READ BY ID
    # ==========================================
    def get_afi_by_id(self, id_afi):
        """Obtiene una AFI específica por su ID"""
        result = self.db.execute_from_file("afis_crud.sql", "read", (id_afi,))
        return result[0] if result else None

    # ==========================================
    # UPDATE
    # ==========================================
    def update_afi(self, id_afi, name, date, time, location, id_faculty, type_afi, max_capacity):
        """Actualiza los datos de una AFI"""
        return self.db.execute_from_file(
            "afis_crud.sql",
            "update",
            (name, date, time, location, id_faculty, type_afi, max_capacity, id_afi)
        )

    # ==========================================
    # DELETE
    # ==========================================
    def delete_afi(self, id_afi):
        """Elimina una AFI"""
        return self.db.execute_from_file("afis_crud.sql", "delete", (id_afi,))
