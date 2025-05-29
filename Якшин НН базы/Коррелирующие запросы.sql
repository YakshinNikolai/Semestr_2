SELECT CreatedAt,
    Price,
     (SELECT ProductName FROM Prooducts
     WHERE Prooducts.Id=Orderss.ProductId) AS Product
FROM Orderss;
