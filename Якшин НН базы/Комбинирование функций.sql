SELECT COUNT (*) AS ProdCount,
    SUM(ProductCount) AS TotalCount,
	MIN(Price) AS MinPrice,
	MAX(Price) AS MaxPrice,
	AVG(Price) AS AvgPrice
FROM Productse;