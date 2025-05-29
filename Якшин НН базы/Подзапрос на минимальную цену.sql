SELECT *
FROM Prooducts
WHERE Price=(SELECT MIN(Price) FROM Products);