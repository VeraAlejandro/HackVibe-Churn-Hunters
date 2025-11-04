CREATE TABLE IF NOT EXISTS Faculties (
    id_faculty INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Careers (
    id_career INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    id_faculty INTEGER,
    semesters INTEGER,
    FOREIGN KEY (id_faculty) REFERENCES Faculties(id_faculty)
);

CREATE TABLE IF NOT EXISTS Users (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    name TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    apellido_materno TEXT,
    faculty_id INTEGER,
    career_id INTEGER,
    FOREIGN KEY (faculty_id) REFERENCES Faculties(id_faculty),
    FOREIGN KEY (career_id) REFERENCES Careers(id_career)
);

CREATE TABLE IF NOT EXISTS AFIs (
    id_afi INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    date TEXT,
    time TEXT,
    location TEXT,
    id_faculty INTEGER,
    type_afi TEXT,
    max_capacity INTEGER,
    FOREIGN KEY (id_faculty) REFERENCES Faculties(id_faculty)
);

CREATE TABLE IF NOT EXISTS Registrations (
    id_registration INTEGER PRIMARY KEY AUTOINCREMENT,
    id_afi INTEGER,
    id_user INTEGER,
    status TEXT DEFAULT 'Pendiente',
    FOREIGN KEY (id_afi) REFERENCES AFIs(id_afi),
    FOREIGN KEY (id_user) REFERENCES Users(id_user)
);
