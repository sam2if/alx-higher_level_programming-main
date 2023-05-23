-- script that creates the table unique_id
-- unique_id description:
--			id INT with the default value 1 and must be unique
--			name VARCHAR(256)
-- The script will not fail, if the table unique_id already exists
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
