SELECT Company, COUNT(*) AS ModelsCount
FROM Productsp
GROUP BY Company
HAVING COUNT(*) > 1;