-- this script creates a table "users" with follwing fields
-- id, email, name and country(enumeration of US, CO and TN)
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)
