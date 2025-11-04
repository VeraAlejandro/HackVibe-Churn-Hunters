# controllers/user_manager.py
import hashlib
import sqlite3
from core.db import get_db

SQL_FILENAME = "users_crud.sql"

def hash_password(password: str) -> str:
    """Hash SHA-256 de la contraseña."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def create_user(matricula: str, role: str, password: str, name: str,
                apellido_paterno: str, apellido_materno: str = "", faculty_id=None, career_id=None) -> bool:
    """
    Crea un usuario a partir del CRUD en SQL/users_crud.sql --create.
    Devuelve True si se creó correctamente, False si hubo conflicto (ej. matrícula duplicada).
    """
    db = get_db()
    pw_hash = hash_password(password)
    try:
        db.execute_from_file(SQL_FILENAME, "create",
                             (matricula, role, pw_hash, name, apellido_paterno, apellido_materno, faculty_id, career_id))
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        db.close()

def get_user_by_matricula(matricula: str):
    """
    Obtiene un usuario por matrícula usando --read.
    Devuelve un dict (row) o None.
    """
    db = get_db()
    try:
        rows = db.execute_from_file(SQL_FILENAME, "read", (matricula,))
        # execute_from_file devuelve lista (query) o lastrowid; en SELECT usamos query -> lista de dicts
        if rows:
            # rows probablemente sea una lista de dicts debido a query()
            if isinstance(rows, list):
                return rows[0] if len(rows) > 0 else None
            return rows  # fallback
        return None
    finally:
        db.close()

def get_all_users():
    """
    Devuelve la lista de todos los usuarios (usar --read_all).
    """
    db = get_db()
    try:
        rows = db.execute_from_file(SQL_FILENAME, "read_all", ())
        # Debería ser una lista de dicts
        return rows if rows is not None else []
    finally:
        db.close()

def update_user(name: str, apellido_paterno: str, apellido_materno: str,
                faculty_id, career_id, matricula: str) -> bool:
    """
    Actualiza campos del usuario (según --update).
    Devuelve True si la operación se ejecutó (no verifica cambios afect).
    """
    db = get_db()
    try:
        db.execute_from_file(SQL_FILENAME, "update", (name, apellido_paterno, apellido_materno, faculty_id, career_id, matricula))
        return True
    finally:
        db.close()

def delete_user(matricula: str) -> bool:
    """
    Elimina el usuario por matrícula (según --delete).
    """
    db = get_db()
    try:
        db.execute_from_file(SQL_FILENAME, "delete", (matricula,))
        return True
    finally:
        db.close()

def verify_login(matricula: str, password: str):
    """
    Verifica credenciales: busca el usuario y compara hash.
    Devuelve el usuario (dict) si es correcto, o None si falla.
    """
    user = get_user_by_matricula(matricula)
    if not user:
        return None
    pw_hash = hash_password(password)
    if user.get("password_hash") == pw_hash:
        return user
    return None
