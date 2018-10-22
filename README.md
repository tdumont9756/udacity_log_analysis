

Project Logs Analysis:
Author: Trais Dumont

Discription:
    The logs_nalysis.py script runs three queries that return answers to the following questions:
        1. What are the most popular three articles of all time?
        2. Who are the most popular article authors of all time?
        3. On which days did more than 1% of requests lead to errors? 
    It pulls these questions as well as the corresponding queries for the newsdata.sql database.
    The queries as well as other String Constants are stored in logs_analysis_strings.py, meaning this file is 
    required as well. 

To run:
    1) Make sure that you have Postgressqul installed on your virtual machine
    2) Make sure that psycopg2 is installed for python 3 on your virtual machine
    3) Make sure there is a table setup as "news" for the newsdata.sql file in your psql database. 
    4) Confirm that logs_analysis_strings.py is in the same directory as your logs_analysis.py
    3) vagrant@vagrant:/vagrant/news$ python3 logs_analysis.py

Expected output:
    vagrant@vagrant:/vagrant/news$ python3 logs_analysis.py
    /usr/local/lib/python3.5/dist-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
    """)
    Hello! Project_1.py will be running three queries for you.  These queries will run sequentially, so please give each query time to run.

    1. What are the most popular three articles of all time?

    Bad things gone, say good people 171762
    Bears love berries, alleges bear 256365
    Candidate is jerk, alleges rival 342102

    Who are the most popular article authors of all time?

    Ursula La Multa 512805
    Rudolf von Treppenwitz 427781
    Anonymous Contributor 171762
    Markoff Chaney 85387

    On which days did more than 1% of requests lead to errors?

    2016-07-17 2.26%

    vagrant@vagrant:/vagrant/news$