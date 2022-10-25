-- create database and user for hbnb
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER ID NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_de_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost;'