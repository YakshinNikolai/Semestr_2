SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Productspp
WHERE Price * ProductCount > 80000
GROUP BY Company
HAVING SUM(ProductCount) > 2
ORDER BY Units DESC;

SELECT Company, COUNT(*) AS Models, ProductCount
FROM Productspp
GROUP BY GROUPING SETS(Company, ProductCount);
