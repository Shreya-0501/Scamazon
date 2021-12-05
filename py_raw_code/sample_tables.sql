CREATE TABLE buyer(
    username VARCHAR(100),
    pass VARCHAR(100),
    buyerid INT PRIMARY KEY AUTO_INCREMENT
);


INSERT INTO buyer (username, pass) VALUE
('bruh', 'bruhpass'),
('notbruh', 'notbruhpass')
;


/*checking*/
SELECT*FROM buyer;

DROP TABLE buyer;

/*//////////////////////////////////////*/

CREATE TABLE vendor(
    username VARCHAR(100),
    pass VARCHAR(100),
    vendorid INT PRIMARY KEY AUTO_INCREMENT
);


INSERT INTO vendor (username, pass)VALUE
('vbruh', 'vbruhpass'),
('vnotbruh', 'vnotbruhpass')
;

SELECT*FROM vendor;

DROP TABLE vendor;

/*/////////////////////////////////////*/

CREATE TABLE items(
    i_name VARCHAR(100),
    listedon DATETIME,
    listedby INT,
    i_id INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY(listedby) REFERENCES vendor (vendorid)
);


INSERT INTO items (i_name, listedon, listedby)VALUE
('red shoes', '2020-09-14 23:18:17', 1),
('blue shoes', '2020-09-14 23:18:18', 1),
('red shirt', '2020-09-14 23:18:18', 2)
;

SELECT*FROM items;

SELECT*FROM items WHERE listedby = 1 ORDER BY listedon;

DROP TABLE items;
