-- Creates a database base htbn_0d_usa and states in that database
CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE (id)
);