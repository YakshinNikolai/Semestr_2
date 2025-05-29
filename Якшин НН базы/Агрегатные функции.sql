CREATE TABLE Productse
(
  Id SERIAL PRIMARY KEY,
  ProductName VARCHAR(30) NOT NULL,
  Company VARCHAR(30) NOT NULL,
  ProductCount INT DEFAULT 0,
  Price NUMERIC NOT NULL,
  IsDiscounted BOOL
);

INSERT INTO Productse(ProductName, Company, ProductCount, Price, IsDiscounted)
VALUES
('iPhone X', 'Apple', 3, 76000, false),
('iPhone 8', 'Apple', 2, 71000, true),
('iPhone 7', 'Apple', 5, 42000, true),
('Calaxy S9', 'Samsung', 2, 46000, false),
('Calaxy S8 Plus', 'Samsung', 1, 56000, true),
('Desire 12', 'HTC', 5, 28000, true),
('Nokia 9', 'HMD Global', 6, 38000, true);


SELECT AVG(Price) AS Average_Price FROM Productse;