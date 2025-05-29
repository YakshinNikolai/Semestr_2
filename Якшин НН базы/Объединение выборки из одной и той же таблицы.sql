SELECT FirstName, LastName, AccountSum + AccountSum * 0.1 AS TotalSum
FROM Drimm WHERE AccountSum < 3000
UNION SELECT FirstName, LastName, AccountSum + AccountSum * 0.3 AS TotalSum
FROM Drimm WHERE AccountSum >= 3000