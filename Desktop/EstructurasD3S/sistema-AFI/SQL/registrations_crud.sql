-- name: create
INSERT INTO Users (matricula, password_hash, name, apellido_paterno, apellido_materno, role, faculty_id, career_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

-- name: read_all
SELECT * FROM Users;

-- name: read_by_matricula
SELECT * FROM Users WHERE matricula = ?;
