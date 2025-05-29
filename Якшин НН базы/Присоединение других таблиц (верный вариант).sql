SELECT Outputet.CreatedAt, Customeet.FirstName, Procrr.ProductName
FROM Outputet
JOIN Procrr ON Procrr.Id=Outputet.ProcrrId
JOIN Customeet ON Customeet.Id=Outputet.CustomeetId
