CREATE TABLE Drem
(
  Id SERIAL PRIMARY KEY,
  FirstName VARCHAR(20) NOT NULL,
  LastName VARCHAR(20) NOT NULL,
  AccountSum NUMERIC DEFAULT 0
);
CREATE TABLE Reap
(
  Id SERIAL PRIMARY KEY,
  FirstName VARCHAR(20) NOT NULL,
  LastName VARCHAR(20) NOT NULL
);
INSERT INTO Drem(FirstName, LastName, AccountSum) VALUES
('Tom', 'Smith', 2000),
('Sam', 'Brown', 3000),
('Paul', 'Ins', 4200),
('Victor', 'Baya', 2800),
('Mark', 'Adams', 2500),
('Tim', 'Cook', 2800);

INSERT INTO Reap(FirstName, LastName) VALUES
('Homer', 'Simpson'),
('Tom', 'Smith'),
('Mark', 'Adams'),
('Nick', 'Svensson');

SELECT FirstName, LastName
FROM Drem
EXCEPT SELECT FirstName, LastName
FROM Reap;

SELECT FirstName, LastName
FROM Drem
INTERSECT SELECT FirstName, LastName
FROM Reap;