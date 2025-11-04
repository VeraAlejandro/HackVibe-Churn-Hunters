-- create
INSERT INTO Careers (name, id_faculty, semesters)
VALUES (?, ?, ?);

-- read_all
SELECT C.id_career, C.name, C.semesters, F.name AS faculty_name
FROM Careers C
JOIN Faculties F ON C.id_faculty = F.id_faculty;

-- read
SELECT * FROM Careers WHERE id_career = ?;

-- update
UPDATE Careers
SET name = ?, id_faculty = ?, semesters = ?
WHERE id_career = ?;

-- delete
DELETE FROM Careers WHERE id_career = ?;
