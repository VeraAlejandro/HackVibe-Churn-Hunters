import hashlib
from core.db import execute_query, load_sql_statements

SQL = load_sql_statements("users_crud.sql")

def hash_password(password: str) -> str:
    """Genera el hash SHA256 de una contraseña."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def verify_login(matricula: str, password: str):
    """Verifica si el usuario existe y la contraseña es correcta."""
    user = execute_query(SQL["read"], (matricula,), fetchone=True)
    if not user:
        return None

    pw_hash = hash_password(password)
    if user["password_hash"] == pw_hash:
        return user
    return None

def register_user(matricula, role, password, name, apellido_paterno, apellido_materno, faculty_id=None, career_id=None):
    """Registra un nuevo usuario."""
    password_hash = hash_password(password)
    execute_query(SQL["create"], (matricula, role, password_hash, name, apellido_paterno, apellido_materno, faculty_id, career_id))
    return True
