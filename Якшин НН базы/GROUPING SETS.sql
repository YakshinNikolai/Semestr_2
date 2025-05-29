SELECT Company, COUNT(*) AS Models, ProductCount
FROM Productspp
GROUP BY GROUPING SETS(Company, ProductCount);