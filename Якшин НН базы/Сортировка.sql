SELECT FirstName ||''|| LastName AS FullName
FROM Drimm
UNION SELECT FirstName ||''|| LastName AS RaaapName
FROM Raaap
ORDER BY FullName;