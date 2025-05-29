SELECT FirstName, COUNT (Jim.Id)
FROM Thh JOIN Jim
ON Jim.ThhId=Thh.Id
GROUP BY Thh.Id, Thh.FirstName;