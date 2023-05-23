-- script that creates the MySQL server user user_0d_1
--	user_0d_1 have all privileges on your MySQL server
--	user_0d_1 password is set to user_0d_1_pwd
--      The script consider if the user user_0d_1 already exists
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost
