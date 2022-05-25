# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays ( \
        songplay_id varchar PRIMARY KEY,\
        start_time numeric NOT NULL,\
        user_id varchar NOT NULL REFERENCES users (user_id),\
        level varchar NOT NULL,\
        song_id varchar NOT NULL REFERENCES songs (song_id),\
        artist_id varchar NOT NULL REFERENCES artists (artist_id),\
        session_id int,\
        location varchar,\
        user_agent varchar\
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (\
        user_id varchar PRIMARY KEY,\
        first_name varchar NOT NULL,\
        last_name varchar NOT NULL,\
        gender varchar NOT NULL,\
        level varchar NOT NULL\
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (\
        song_id varchar PRIMARY KEY,\
        title varchar NOT NULL,\
        artist_id varchar NOT NULL,\
        year int NOT NULL,\
        duration numeric NOT NULL\
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (\
        artist_id varchar PRIMARY KEY,\
        name varchar NOT NULL,\
        location varchar,\
        latitude numeric,\
        longitude numeric\
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS times (\
        id INTEGER PRIMARY KEY,\
        songplay_id varchar NOT NULL REFERENCES songplays (songplay_id),\
        start_time numeric NOT NULL,\
        hour numeric NOT NULL,\
        day numeric NOT NULL,\
        week numeric NOT NULL,\
        month numeric NOT NULL,\
        year numeric NOT NULL,\
        weekday numeric NOT NULL\
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id,\
        level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""
    INSERT INTO times (id, songplay_id, start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT song_id, artist_id FROM songs;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, songplay_table_create, time_table_create]
drop_table_queries = [time_table_drop, songplay_table_drop, user_table_drop, artist_table_drop, song_table_drop]