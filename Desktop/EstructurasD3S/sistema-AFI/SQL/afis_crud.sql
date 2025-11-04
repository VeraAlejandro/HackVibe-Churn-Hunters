-- create
INSERT INTO AFIs (name, date, time, location, id_faculty, type_afi, max_capacity)
VALUES (?, ?, ?, ?, ?, ?, ?);

-- read_all
SELECT A.id_afi, A.name, A.date, A.time, A.location, A.type_afi, A.max_capacity, F.name AS faculty_name
FROM AFIs A
JOIN Faculties F ON A.id_faculty = F.id_faculty;

-- read
SELECT * FROM AFIs WHERE id_afi = ?;

-- update
UPDATE AFIs
SET name = ?, date = ?, time = ?, location = ?, id_faculty = ?, type_afi = ?, max_capacity = ?
WHERE id_afi = ?;

-- delete
DELETE FROM AFIs WHERE id_afi = ?;
