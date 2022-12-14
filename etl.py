import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """
    reads one json song_file and extarcts the relevant data from it and loads it into 
    song_table, and artist_table
    
    inputs:
        cur:(required) database cursor object
        filepath:(required) the absolute path to the json song_file
    outputs: 
        None
    
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = (df.values[0][7], df.values[0][8], df.values[0][0], df.values[0][9], 
                 df.values[0][5])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = (df.values[0][0], df.values[0][4], df.values[0][2], df.values[0][1], 
                   df.values[0][3])
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    process one json log file for song plays and extarcts relevant data from it and perform 
    the appropriate transformations to load it into the users_table and songplay table
    
    inputs: 
        cur:(required) database cursor object
        filepath:(reuired) absolute filepath to the log file
    outputs:
        None
        
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms') 
    
    # insert time data records
    time_data = [(value, value.hour, value.day, value.weekofyear, value.month, value.year, 
                  value.weekday()) for index, value in t.items()]
    column_labels = ("timestamp", "hour", "day", "week_of_year", "month", "year", 
                     "weekday")
    time_df = pd.DataFrame(time_data, columns=column_labels)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", 
                  "level"]].drop_duplicates(subset=["userId"])

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (pd.to_datetime(row.ts, unit='ms'), row.userId, row.level, songid, 
                         artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """
    applies the appropriate processing function on all data files specified in the filepath
    
    inputs:
        cur:(required) databsse cursor object
        conn:(required) database connection object
        filepath:(required) absolute path to the data directory containing data files
        func:(required) appropriate function to process each data file
    ouputs:
        None
        
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()