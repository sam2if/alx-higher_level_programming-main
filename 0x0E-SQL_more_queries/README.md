# 0x0E. SQL - More queries

## Concepts

Reading through the resources and working on tasks i was able to understand

    How to create a new MySQL user
    How to manage privileges for a user to a database or table
    What a PRIMARY KEY is
    What a FOREIGN KEY is
    How to use NOT NULL and UNIQUE constraints
    How to retrieve datas from multiple tables in one request
    What subqueries are
    What JOIN and UNION are


## Table of content
| Task     | Description |
| -------- | -------------- |
| [0-privileges.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/0-privileges.sql) | script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost) |
| [1-create_user.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/1-create_user.sql) | script that creates the MySQL server user user_0d_1 |
| [2-create_read_user.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/2-create_read_user.sql) | script that creates the database hbtn_0d_2 and the user user_0d_2 |
| [3-force_name.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/3-force_name.sql) | script that creates the table force_name on your MySQL server |
| [4-never_empty.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/4-never_empty.sql) | script that creates the table id_not_null on your MySQL server |
| [5-unique_id.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/5-unique_id.sql) | script that creates the table unique_id on your MySQL server. |
| [6-states.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/6-states.sql) | script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server |
| [7-cities.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/7-cities.sql) | creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server |
| [8-cities_of_california_subquery.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql) | script that lists all the cities of California that can be found in the database hbtn_0d_usa |
| [9-cities_by_state_join.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/9-cities_by_state_join.sql) | script that lists all cities contained in the database hbtn_0d_usa |
| [10-genre_id_by_show.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/10-genre_id_by_show.sql) | script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked |
| [11-genre_id_all_shows.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/11-genre_id_all_shows.sql) | script that lists all shows contained in the database hbtn_0d_tvshows |
| [12-no_genre.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/12-no_genre.sql) | script that lists all shows contained in hbtn_0d_tvshows without a genre linked |
| [13-count_shows_by_genre.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/13-count_shows_by_genre.sql) | script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each |
| [14-my_genres.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/14-my_genres.sql) | script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter |
| [14-my_genres.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/14-my_genres.sql) | script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter |
| [15-comedy_only.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/15-comedy_only.sql) | script that lists all Comedy shows in the database hbtn_0d_tvshows |
| [16-shows_by_genre.sql](https://github.com/mickiyas123/alx-higher_level_programming/blob/2be3b3bb4836464572bbaf1c7d630ba2ca3efa24/0x0E-SQL_more_queries/16-shows_by_genre.sql) | script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows |
