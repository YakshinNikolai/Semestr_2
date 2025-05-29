SELECT Thh.FirstName, Jim.CreatedAt,
    Jkk.ProductName, Jkk.Company
FROM Jim
LEFT JOIN Thh ON Jim.ThhId=Thh.Id
LEFT JOIN Jkk ON Jim.JkkId=Jkk.Id;

