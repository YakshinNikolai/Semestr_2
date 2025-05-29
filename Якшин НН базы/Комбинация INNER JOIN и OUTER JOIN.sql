SELECT Thh.FirstName, Jim.CreatedAt,
    Jkk.ProductName, Jkk.Company
FROM Jim
JOIN Jkk ON Jim.JkkId=Jkk.Id AND Jkk.Price > 45000
LEFT JOIN Thh ON Jim.ThhId=Thh.Id
ORDER BY Jim.CreatedAt;