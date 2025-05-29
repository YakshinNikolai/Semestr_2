SELECT O.CreatedAt, O.ProductCount, P.ProductName
FROM Outputet AS O
JOIN Procrr AS P
ON P.Id=O.ProcrrId;

