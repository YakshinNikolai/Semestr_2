INSERT INTO Productsd(ProductName, Company, ProductCount, Price)
VALUES 
('iPhone X', 'Apple', 2, 66000),
('iPhone 8', 'Apple', 2, 51000),
('Galaxy S9','Samsung', 2, 56000),
('Galaxy S8 Plus','Samsung', 1, 46000),
('Nokia 9','HMD Global', 2, 26000),
('Desire 12','HTC', 6, 38000);

INSERT INTO Cusstomers(FirstName)
VALUES ('Tom'), ('Bob'), ('Sam');

INSERT INTO Orrders(ProductId, CustomersId, CreatedAt, ProductCount, Price)
VALUES
(
    (SELECT Id FROM Productsd WHERE ProductName='Galaxy S9'),
    (SELECT Id FROM Cusstomers WHERE FirstName='Tom'),
    '2017-07-11',
    2,
    (SELECT Price FROM Productsd WHERE ProductName='Galaxy S9')
),
(
    (SELECT Id FROM Productsd WHERE ProductName='iPhone 8'),
    (SELECT Id FROM Cusstomers WHERE FirstName='Tom'),
    '2017-07-13',
    1,
    (SELECT Price FROM Productsd WHERE ProductName='iPhone 8')
),
(
    (SELECT Id FROM Productsd WHERE ProductName='iPhone 8'),
    (SELECT Id FROM Cusstomers WHERE FirstName='Bob'),
    '2017-07-11',
    1,
    (SELECT Price FROM Productsd WHERE ProductName='iPhone 8')
);

SELECT * FROM Orrders, Cusstomers;