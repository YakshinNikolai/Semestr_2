CREATE TABLE fruits (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE drinks (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
    photo BLOB NOT NULL, 
    resume BLOB NOT NULL
);

CREATE TABLE new_employee (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    photo BLOB NOT NULL, 
    resume BLOB NOT NULL
);
