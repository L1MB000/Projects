CREATE TABLE Customers(
CustomerID varchar(50) Primary Key, customer_name varchar(50), customer_email varchar(50), customer_address varchar(50)
);

CREATE TABLE Shipment(
ShipmentID varchar(50) Primary Key, shipment_date date, shipment_status varchar(50)
);


CREATE TABLE Manager(
ManagerID varchar(50) Primary Key, manager_name varchar(50), manager_email varchar(50), manager_address varchar(50)
);

CREATE TABLE AuthorAccount(
authorID varchar (50) primary key, author_name varchar(50)
);

CREATE TABLE PublisherAccount(
publisherID varchar (50) primary key, publisher_name varchar(50)
);

CREATE TABLE Warehouse(
WarehouseID varchar(50) Primary Key, book_stock int
);

CREATE TABLE TotalBook(
ISBN varchar(10) Primary Key, book_title varchar(50), book_price float, book_quantity int,
authorID varchar(50) Foreign Key references AuthorAccount(authorID),
publisherID varchar(50) Foreign Key references PublisherAccount(publisherID), 
WarehouseID varchar(50) Foreign Key references Warehouse(WarehouseID)
);

CREATE TABLE CustomerReview(
ReviewID varchar(10) Primary Key, CustomerID varchar(50) Foreign Key references Customers (CustomerID), 
ISBN varchar(10) Foreign Key references TotalBook(ISBN), book_review varchar(50), book_rating float
);

CREATE TABLE OrderDetail(
OrderID varchar(50) Primary Key, order_date date, shipmentID varchar(50) Foreign Key references Shipment(ShipmentID),
ISBN varchar(10) Foreign Key references TotalBook(ISBN)
);

CREATE TABLE CustomerOrder(
OrderID varchar(50) Foreign Key references OrderDetail(OrderID), CustomerID varchar(50) Foreign Key references Customers(CustomerID)
);

CREATE TABLE OrderAmount(
OrderID varchar(50) Foreign Key references OrderDetail(OrderID), order_amount int
);

CREATE TABLE ManagerOrder(
ManagerID varchar(50) Foreign Key references Manager(ManagerID), OrderID varchar(50) Foreign Key references OrderDetail(OrderID),
publisherID varchar (50) Foreign Key references PublisherAccount(publisherID)
);

INSERT INTO Customers(CustomerID, customer_name, customer_email, customer_address)VALUES
('CUS00001', 'Allan', 'allan@mail.com', 'Cyberjaya'), ('CUS00002', 'Andy', 'andy@mail.com', 'Bukit bintang'),
('CUS00003', 'Dobby', 'dobby@mail.com', 'Bukit jalil'), ('CUS00004', 'Samsul', 'samsul@mail.com', 'Cheras'), 
('CUS00005', 'Putri', 'putri@mail.com', 'Sungai besi'), ('CUS00006', 'Kenzo', 'kenzo@mail.com', 'Selangor');

INSERT INTO Shipment(ShipmentID, shipment_date, shipment_status)VALUES
('SID00001', '2022-03-12', 'Delivered'), ('SID00002', '2022-03-15', 'Delivered'),('SID00003', '2022-05-04', 'Not Delivered'), 
('SID00004', '2022-06-1', 'Not Delivered'), ('SID00005', '2022-06-15', 'Ordered'), ('SID00006', '2022-06-16', 'Ordered'),
('SID00007', '2022-06-18', 'Ordered');

INSERT INTO Manager(ManagerID, manager_name, manager_email, manager_address)VALUES
('MAN00001', 'Willy', 'willy@manager.com', 'Bukit nanas'), ('MAN00002', 'Komeng', 'komeng@amanger.com', 'Bukit bintang'),
('MAN00003', 'Darren', 'darren@manager.com', 'Bukit jalil'), ('MAN00004', 'Shanice', 'shanice@manager.com', 'Selangor'), 
('MAN00005', 'Jackquelyn', 'jackquelyn@manager.com', 'Cheras');

INSERT INTO AuthorAccount(authorID, author_name)VALUES
('AID00001', 'Shakepear'), ('AID00002', 'Dean Armando'), ('AID00003', 'james'), ('AID00004', 'Keith'), ('AID00005', 'Tsun Zi');

INSERT INTO PublisherAccount(publisherID, publisher_name)VALUES
('PID00001', 'Jason'), ('PID00002', 'Park'), ('PID00003', 'Sonny'), ('PID00004', 'Lucas'), ('PID00005', 'Johan');

INSERT INTO Warehouse(WarehouseID, book_stock)VALUES
('WHS00001', '6'), ('WHS00002', '12'), ('WHS00003', '5'), ('WHS00004', '3'), ('WHS00005', '9');

INSERT INTO TotalBook(ISBN, book_title, book_price, book_quantity, authorID, publisherID, WarehouseID)VALUES
('A00001', 'Contrarella', '70', '6', 'AID00001', 'PID00001', 'WHS00001'), ('A00002', 'kanata no astra', '40', '12','AID00002', 'PID00002', 'WHS00002'), 
('A00003', 'County n country', '25', '5', 'AID00003', 'PID00003', 'WHS00003'),('A00004', 'das kommandier', '15', '3', 'AID00004', 'PID00004', 'WHS00004'), 
('A00005', 'art of peace', '20', '9', 'AID00005', 'PID00005', 'WHS00005');

INSERT INTO CustomerReview(ReviewID, CustomerID, ISBN, book_review, book_rating)VALUES
('RNR00001', 'CUS00001', 'A00001', 'it worth the time reading it', '7'), ('RNR00002', 'CUS00002', 'A00002', 'The book waste my time', '3'),
('RNR00003', 'CUS00003', 'A00003', 'It is not worth it', '2'), ('RNR00004', 'CUS00004', 'A00004', 'Good plot by the author', '8'),
('RNR00005', 'CUS00005', 'A00005', 'THIS BOOK IS A MASTERPIECE!!! ', '10'), ('RNR00006', 'CUS00005', 'A00005', 'the ending could have been better ', '7'),
('RNR00007', 'CUS00005', 'A00005', 'it really missing something', '5');

INSERT INTO OrderDetail(OrderID, order_date, shipmentID, ISBN)VALUES
('ORD00001', '2022-03-12', 'SID00001', 'A00001'), ('ORD00002', '2022-03-15', 'SID00002', 'A00002'), 
('ORD00003', '2022-05-04', 'SID00003', 'A00003'), ('ORD00004', '2022-06-1', 'SID00004', 'A00004'), 
('ORD00005', '2022-06-15', 'SID00005', 'A00005'), ('ORD00006', '2022-06-16', 'SID00006', 'A00005'),
('ORD00007', '2022-06-18', 'SID00007', 'A00005');

INSERT INTO CustomerOrder(OrderID, CustomerID)VALUES
('ORD00001', 'CUS00001'), ('ORD00002', 'CUS00002'), ('ORD00003', 'CUS00003'), ('ORD00004', 'CUS00004'), 
('ORD00005', 'CUS00005'), ('ORD00006', 'CUS00005'), ('ORD00007', 'CUS00005');

INSERT INTO OrderAmount(OrderID, order_amount)VALUES
('ORD00001', '2'), ('ORD00002', '1'), ('ORD00003', '1'), ('ORD00004', '3'), ('ORD00005', '2'), ('ORD00006', '1'),('ORD00007', '1');

INSERT INTO ManagerOrder(ManagerID, OrderID, publisherID)VALUES
('MAN00001', 'ORD00001', 'PID00001'), ('MAN00002', 'ORD00002', 'PID00002'), ('MAN00003', 'ORD00003', 'PID00003'), 
('MAN00004', 'ORD00004', 'PID00004'), ('MAN00005', 'ORD00005', 'PID00005'), ('MAN00005', 'ORD00006', 'PID00005'),
('MAN00005', 'ORD00007', 'PID00005');

SELECT * FROM Customers
SELECT * FROM Shipment
SELECT * FROM Manager
SELECT * FROM AuthorAccount
SELECT * FROM PublisherAccount
SELECT * FROM Warehouse
SELECT * FROM CustomerReview
SELECT * FROM TotalBook
SELECT * FROM OrderDetail
SELECT * FROM CustomerOrder
SELECT * FROM OrderAmount
SELECT * FROM ManagerOrder