SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Productspp
GROUP BY ROLLUP(Company, ProductCount)
ORDER BY Company;