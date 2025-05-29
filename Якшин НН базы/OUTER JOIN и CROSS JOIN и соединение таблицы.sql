CREATE TABLE Jkk 
( 
  Id SERIAL PRIMARY KEY, 
  ProductName VARCHAR(30) NOT NULL, 
  Company VARCHAR(20) NOT NULL, 
  ProductCount INTEGER DEFAULT 0, 
  Price NUMERIC NOT NULL, 
  IsDiscounted BOOLEAN   
); 

CREATE TABLE Thh 
(
  Id SERIAL PRIMARY KEY, 
  FirstName VARCHAR(30) NOT NULL 
); 

CREATE TABLE Jim 
(
  Id SERIAL PRIMARY KEY, 
  JkkId INTEGER NOT NULL REFERENCES Jkk (Id) ON DELETE CASCADE,   
  ThhId INTEGER NOT NULL REFERENCES Thh (Id) ON DELETE CASCADE,   
  CreatedAt DATE NOT NULL, 
  ProductCount INTEGER DEFAULT 1, 
  Price NUMERIC NOT NULL  
); 


INSERT INTO Jkk(ProductName, Company, ProductCount, Price, IsDiscounted) 
VALUES 
('iPhone X', 'Apple', 3, 76000, false), 
('iPhone 8', 'Apple', 2, 71000, true), 
('iPhone 7', 'Apple', 5, 42000, true), 
('Galaxy S9', 'Samsung', 2, 46000, false),   
('Galaxy S8 Plus', 'Samsung', 1, 56000, true),   
('Desire 12', 'HTC', 5, 28000, true), 
('Nokia 9', 'HMD Global', 6, 38000, true); 


INSERT INTO Thh (FirstName) 
VALUES ('Jason Durelo'),('AnastasiZ'),('Brian Maps'); 

INSERT INTO Jim (JkkId, ThhId, CreatedAt, ProductCount, Price) 
VALUES 
(1, 1, '2023-01-15', 1, 76000),   
(4, 2, '2023-01-16', 1, 46000),   
(2, 3, '2023-01-17', 2, 71000); 

SELECT FirstName, CreatedAt, ProductCount, Price, JkkId
FROM Jim LEFT JOIN Thh
ON Jim.ThhId=Thh.Id;