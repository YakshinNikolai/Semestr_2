SELECT FirstName, CreatedAt, ProductCount, Price
FROM Thh LEFT JOIN Jim
ON Jim.ThhId=Thh.Id;