-- create
INSERT INTO Faculties (name)
VALUES (?);

-- read_all
SELECT * FROM Faculties;

-- read
SELECT * FROM Faculties WHERE id_faculty = ?;

-- update
UPDATE Faculties
SET name = ?
WHERE id_faculty = ?;

-- delete
DELETE FROM Faculties WHERE id_faculty = ?;
