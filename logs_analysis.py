#!/usr/bin/env python3
import psycopg2
from logs_analysis_strings import *

conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


def get_posts(cursor, query):
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    posts = cursor.fetchall()
    posts_data = [columns, posts]
    return posts_data


def display_posts(post_data):
    dashes = '-'*50
    entries_index = 0
    for entries in post_data:
        if(entries_index == 0):
            entries_index += 1
            print(dashes)
            print('{:<40s}{:<10s}'.format(entries[0], entries[1]))
            print(dashes)
        else:
            for line in entries:
                print('{:<40s}{:<10s}'.format(str(line[0]), str(line[1])))


def query_db():
    queries = [QUERY_1, QUERY_2, QUERY_3]
    questions = [QUESTION_1, QUESTION_2, QUESTION_3]
    print(INITIAL_PROMPT)
    count = 0

    for query in queries:
        cursor = conn.cursor()
        print(questions[count])
        count += 1
        display_posts(get_posts(cursor, query))
        print('\n \n')
    conn.close()


# run the code
query_db()
