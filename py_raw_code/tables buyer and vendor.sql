CREATE TABLE buyer(
    username VARCHAR(100),
    pass VARCHAR(100),
    buyerid INT PRIMARY KEY AUTO_INCREMENT
);

INSERT INTO buyer (username, pass) VALUE
('bruh', 'bruhpass'),
('notbruh', 'notbruhpass')
;

///////////////////////////

CREATE TABLE vendor(
    username VARCHAR(100),
    pass VARCHAR(100),
    buyerid INT PRIMARY KEY AUTO_INCREMENT
);


INSERT INTO vendor VALUE
('vbruh', 'vbruhpass', 1),
('vnotbruh', 'vnotbruhpass', 2)
;