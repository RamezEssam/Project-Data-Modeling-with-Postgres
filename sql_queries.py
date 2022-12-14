# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS user_table"
song_table_drop = "DROP TABLE IF EXISTS song_table"
artist_table_drop = "DROP TABLE IF EXISTS artist_table"
time_table_drop = "DROP TABLE IF EXISTS time_table"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplay(
    start_time timestamp PRIMARY KEY, user_id int NOT NULL, level varchar,
    song_id varchar, artist_id varchar, session_id int, location varchar, user_agent 
    varchar)
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS user_table (user_id int PRIMARY KEY, first_name varchar, 
    last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS song_table (song_id varchar PRIMARY KEY, title varchar NOT 
    NULL, artist_id varchar, year int, duration numeric NOT NULL)
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artist_table (artist_id varchar PRIMARY KEY, name 
    varchar NOT NULL, location varchar, latitude double precision, longitude double 
    precision)
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS  time_table (start_time timestamp PRIMARY KEY, hour int, 
    day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplay(start_time , user_id 
    , level , song_id , artist_id , session_id , location 
    , user_agent )
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO user_table(user_id, first_name , 
    last_name , gender , level )
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
    INSERT INTO song_table(song_id , title , 
    artist_id , year , duration )
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artist_table(artist_id, name 
    , location , latitude , longitude )
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time_table(start_time, hour , 
    day , week , month , year , weekday )
    VALUES(%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
    select song_table.song_id, artist_table.artist_id from song_table
    join artist_table on song_table.artist_id=artist_table.artist_id
    where song_table.title=%s
    and artist_table.name=%s
    and song_table.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]