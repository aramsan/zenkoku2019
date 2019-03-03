DROP TABLE IF EXISTS `entry`;
CREATE TABLE IF NOT EXISTS entry (
    id           INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(255) NOT NULL,
    email        VARCHAR(255) NOT NULL,
    password     VARCHAR(255) NOT NULL,
    type         VARCHAR(255) NOT NULL,
    grade        VARCHAR(255) NOT NULL,
    departure    VARCHAR(255) NOT NULL,
    adult        INTEGER,
    child        INTEGER,
    picture      TEXT,
    message      TEXT,
    cancel       INTEGER,
    admin        INTEGER,
    created_on   DATETIME,
    updated_on   DATETIME 
);
