CREATE TABLE Procrr
(
  Id SERIAL PRIMARY KEY,
  ProductName VARCHAR(30) NOT NULL,
  Company VARCHAR(20) NOT NULL,
  ProductCount INTEGER DEFAULT 0,
  Price NUMERIC NOT NULL,
  IsDiscounted BOOLEAN  
);

CREATE TABLE Customeet
(
  Id SERIAL PRIMARY KEY,
  FirstName VARCHAR(30) NOT NULL
);

CREATE TABLE Outputet
(
  Id SERIAL PRIMARY KEY,
  ProcrrId INTEGER NOT NULL REFERENCES Procrr (Id) ON DELETE CASCADE,  
  CustomeetId INTEGER NOT NULL REFERENCES Customeet(Id) ON DELETE CASCADE,  
  CreatedAt DATE NOT NULL,
  ProductCount INTEGER DEFAULT 1,
  Price NUMERIC NOT NULL 
);

INSERT INTO Procrr(ProductName, Company, ProductCount, Price, IsDiscounted)
VALUES
('iPhone X', 'Apple', 3, 76000, false),
('iPhone 8', 'Apple', 2, 71000, true),
('iPhone 7', 'Apple', 5, 42000, true),
('Galaxy S9', 'Samsung', 2, 46000, false),  
('Galaxy S8 Plus', 'Samsung', 1, 56000, true),  
('Desire 12', 'HTC', 5, 28000, true),
('Nokia 9', 'HMD Global', 6, 38000, true);

INSERT INTO Customeet (FirstName)
VALUES ('Tom'),('Bob'),('Alex');

INSERT INTO Outputet (ProcrrId, CustomeetId, CreatedAt, ProductCount, Price)
VALUES
(1, 1, '2023-01-15', 1, 76000),  
(4, 2, '2023-01-16', 1, 46000),  
(2, 3, '2023-01-17', 2, 71000);


SELECT Outputet.CreatedAt, Outputet.ProductCount, Procrr.ProductName
FROM Outputet
JOIN Procrr ON Procrr.Id = Outputet.ProcrrId;

SELECT FirstName, CreatedAT, ProductCount, Price, ProcrrId
FROM Outputet
LEFT JOIN Customeet ON Outputet.CustomeetId=Customeet.Id;