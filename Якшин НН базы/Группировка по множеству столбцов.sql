SELECT Company, COUNT(*) AS ModelsCount
FROM Productsp
WHERE Price > 30000
GROUP BY Company
ORDER BY ModelsCount DESC;