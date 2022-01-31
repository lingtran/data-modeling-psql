# Data Engineering - Project 1 - Data Modeling with Postgres

## Objective
To optimize queries on song play analysis related to related to user activity and songs being streamed on Sparkify.

## Methodology
Data currently resides in two local directories of JSON - (1) user activity on app logs and (2) metadata on the songs in app. We are building an ETL pipeline using Python and SQL to transfer the data into relational tables in Postgres database `sparkifydb`.

## Table of contents
* [Run scripts](#run-scripts)
* [Description of project files](#description-of-project-files)
* [Database schema and ETL pipeline](#database-schema-and-etl-pipeline)
* [Queries](#queries)

## Run scripts
wip

## Description of project files
 - `data/` 
    - `/log_data`
    - `/song_data`
 -  `create_tables.py`
    - *drops and creates tables. needs to be run at least once to create `sparkifydb`*
 - `etl.ipynb`
    - *reads and processes a single file from `/song_data` and `/log_data` and loads the data into database tables. This notebook contains detailed instructions on the ETL process for each of the tables.*
 - `etl.py`
    - *reads and processes files from `/song_data` and `/log_data` and loads them into database tables.*
 - `sql_queries.py`
    - *contains all your sql queries, and is imported into `create_tables.py`, `etl.ipynb`, and `etl.py`.*
 - `test.ipynb`
    - *displays the first few rows of each table as a way to let us check the database.*

## Database schema and ETL pipeline
wip

## Queries
wip