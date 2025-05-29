SELECT *
FROM Prooducts
WHERE Price>(SELECT AVG(Price) FROM Products);