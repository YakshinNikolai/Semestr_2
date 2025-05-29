SELECT Company, COUNT(*) AS ModelsCount
FROM Productsp
WHERE Price * ProductCount > 80000
GROUP BY Company
HAVING COUNT(*) > 1;