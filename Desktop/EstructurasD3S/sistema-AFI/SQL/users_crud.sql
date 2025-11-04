-- create
INSERT INTO Users (matricula, role, password_hash, name, apellido_paterno, apellido_materno, faculty_id, career_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);

-- read
SELECT * FROM Users WHERE matricula = ?;

-- read_all
SELECT * FROM Users;

-- update
UPDATE Users
SET name = ?, apellido_paterno = ?, apellido_materno = ?, faculty_id = ?, career_id = ?
WHERE matricula = ?;

-- delete
DELETE FROM Users WHERE matricula = ?;
