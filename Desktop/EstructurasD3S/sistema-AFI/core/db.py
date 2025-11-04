import sqlite3
from pathlib import Path

# ==========================================
# RUTAS BASE
# ==========================================
BASE_DIR = Path(__file__).resolve().parent.parent
SQL_DIR = BASE_DIR / "SQL"
DB_PATH = SQL_DIR / "afis.db"
SCHEMA_FILE = SQL_DIR / "schema.sql"

class Database:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self.conn = None

    # ==========================================
    # CONEXIÓN Y DESCONEXIÓN
    # ==========================================
    def connect(self):
        """Establece conexión con la base de datos"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

    def close(self):
        """Cierra la conexión"""
        if self.conn:
            self.conn.close()

    # ==========================================
    # MÉTODOS BASE
    # ==========================================
    def execute_script(self, script_path):
        """Ejecuta un archivo SQL completo (como schema.sql)"""
        with open(script_path, "r", encoding="utf-8") as file:
            script = file.read()
        with self.conn:
            self.conn.executescript(script)

    def query(self, sql, params=()):
        """Ejecuta una consulta SELECT"""
        with self.conn:
            cur = self.conn.execute(sql, params)
            rows = cur.fetchall()
            return [dict(row) for row in rows]

    def execute(self, sql, params=()):
        """Ejecuta INSERT, UPDATE o DELETE"""
        with self.conn:
            cur = self.conn.execute(sql, params)
            self.conn.commit()
            return cur.lastrowid

    def execute_from_file(self, filename, key, params=()):
        """
        Ejecuta una sentencia SQL desde un archivo CRUD.
        key → comentario identificador ('-- create', '-- read', etc.)
        """
        file_path = SQL_DIR / filename
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # separa los bloques por comentario
        sections = content.split("--")
        query = None
        for section in sections:
            if key.lower() in section.lower():
                query = section.strip().split("\n", 1)[1].strip()
                break

        if not query:
            raise ValueError(f"No se encontró la consulta con clave '{key}' en {filename}")

        if query.lower().startswith("select"):
            return self.query(query, params)
        else:
            return self.execute(query, params)

    # ==========================================
    # INICIALIZAR BASE DE DATOS
    # ==========================================
    def init_db(self):
        """Crea la base de datos y el esquema si no existe"""
        if not self.db_path.exists():
            print("🆕 Creando base de datos AFIs...")
            self.db_path.parent.mkdir(parents=True, exist_ok=True)
            self.connect()
            self.execute_script(SCHEMA_FILE)
            self.close()
            print(f"✅ Base de datos creada exitosamente en: {self.db_path}")
        else:
            print(f"📂 Base de datos ya existente en: {self.db_path}")

# ==========================================
# FUNCIÓN GLOBAL
# ==========================================
def get_db():
    """Devuelve una instancia activa de la base de datos"""
    db = Database()
    db.connect()
    return db

if __name__ == "__main__":
    db = Database()
    db.init_db()
