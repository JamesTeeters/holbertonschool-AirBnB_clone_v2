-- creating Database and user of hbnb
CREATE DATABASE IF NOT EXSITS hbnb_dev_db;
CREATE USER IF NOT EXSITS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';