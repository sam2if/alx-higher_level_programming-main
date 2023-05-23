-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states description:
--		      id INT unique, auto generated, is not null and is a primary key
--		      name VARCHAR(256) can’t be null
-- The script will not fail, if the database hbtn_0d_usa already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
