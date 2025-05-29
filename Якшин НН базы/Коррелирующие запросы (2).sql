SELECT ProductName,
       Company,
       Price,
     (SELECT AVG(Price) FROM Prooducts AS SubProds
	 WHERE SubProds.Company=Prods.Company)AS AvgPrice
FROM Prooducts AS Prods
WHERE Price>
   (SELECT AVG(Price) FROM Prooducts AS SubProds
   WHERE SubProds.Company=Prods.Company)
