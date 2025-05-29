SELECT Outputet.CreatedAt, Customeet.FirstName, Procrr.ProductName
FROM Outputet
JOIN Procrr ON Procrr.Id=Outputet.ProcrrId AND Procrr.Company='Apple'
JOIN Customeet ON Customeet.Id=Outputet.CustomeetId
ORDER BY Customeet.FirstName;