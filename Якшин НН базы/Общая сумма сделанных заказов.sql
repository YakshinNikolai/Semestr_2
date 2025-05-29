SELECT Jkk.ProductName, Jkk.Company,
     SUM(Jim.ProductCount*Jim.Price) AS TotalSum
FROM Jkk LEFT JOIN Jim
ON Jim.JkkId=Jkk.Id
GROUP BY Jkk.Id, Jkk.ProductName, Jkk.Company;