# Sparkify ETL Project

## Project Summary

#### Sparkify ETL is an extract, transform, load pipeline for song play data from web log files into modelled star schema for song analysis.

## How to run scripts

    1.Populate the SQL queries in sql_queries.py to create the tables, insert statements, and select statements
    2.Run the create_table.py file in the terminal to create the sparkify database and all the schema tables
    3.Run etl.py in the terminal to execute the ETL process and load the data into the database
    
## File descriptions

    -sql_queries.py: This python file contains all DDL, DCL, DML statements needed to create/reset the database, schema and tables needed for the ETL pipline.
    
    -etl.ipynb: This notebook contains ETL development process and trials
    
    -test.ipynb: This notebook performs unit testing and sanity checks for data validation.
    
    -create_tables.py; This python file creates/resets the sparkify database and all the needed tables
    
    -etl.py: This Python file runs the ETL pipleine to extract the data from the web log files, perform the required transformations, and load the data into the target tables in the sparkify database