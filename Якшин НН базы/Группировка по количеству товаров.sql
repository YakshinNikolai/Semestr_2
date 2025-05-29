SELECT Company, ProductCount, COUNT(*) AS ModelsCount
FROM Productsp
GROUP BY Company, ProductCount;