SELECT Company, COUNT(*) AS Models, SUM(ProductCount) AS Units
FROM Productspp
GROUP BY CUBE(Company);