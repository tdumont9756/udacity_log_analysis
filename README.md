
Project Logs Analysis:
Author: Travis Dumont

Discription:
    The logs_nalysis.py script runs three queries that return answers to the following questions:
        1. What are the most popular three articles of all time?
        2. Who are the most popular article authors of all time?
        3. On which days did more than 1% of requests lead to errors? 
    It pulls these questions as well as the corresponding queries for the newsdata.sql database.
    The queries as well as other String Constants are stored in logs_analysis_strings.py, meaning this file is 
    required as well. 

To run:
    1) This program is set up to run on a linux environment with Postgres Sql installed. You can setup a virtual environment using Virtual Box and Vagrant.
        a) First install and set up Virtual Box.  This is the url to their website and also contains trouble shooting
        https://www.virtualbox.org/wiki/Downloads
        b) Next, set up Vagrant.  Again here is the url for the download.
        https://www.vagrantup.com/downloads.html
    
    2) Download the VM setup directory.  This file will download the configuration needed to connect to the 
    virtual environment. 
        a) Download the zip file from https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
        b) Find the file called fsnd-virtual-machine.zip and unzip it to the directory that you wish to work from.
        c) You will now have a directory called fsnd-virtual-machine.  With vagrant running, files added to this directory
        will be accessable from both your Virtual Machine instance as well as your normal computer. 
    
    3) To start Vagrant, Open a command line prompt and cd to path/to/your/fsnd-virtual-machine/vagrant/
    
    4) Inside the vagrant directory, run the following command:
            $: vagrant up
        This will go through the setup process of creating your Virtual Environment.  If this is the first time creating it, it may take several minutes. 
    
    5) Once vagrant up has finished running, you can log into the instance by running
            $: vagrant ssh

    6) If you have not already done so, download a copy or clone the git repo for this project to your path/to/your/fsnd-virtual-machine/vagrant/
        $: cd path/to/your/fsnd-virtual-machine/vagrant/
        $: git int
        $: git clone https://github.com/tdumont9756/udacity_log_analysis.git
        $: cd logs_analysis/


    7) Setting up the database with the test data.  
    The sample data for the project can be downloaded from the following url:
    https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

    The next step is creating the database and importing the sql data into the database. I did an example here 
    creating the "test" database and using the 'testData.sql'.  For the actual data, simply replace news.sql or 
    what ever you named your sql file in place of test or testData.sql :
        vagrant@vagrant:/vagrant/tmp$ ls
        testData.sql
        vagrant@vagrant:/vagrant/tmp$ psql
        psql (9.5.14)
        Type "help" for help.

        vagrant=> CREATE DATABASE test;
        CREATE DATABASE
        vagrant=> \list
                                        List of databases
        Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
        -----------+----------+----------+-------------+-------------+-----------------------
        test      | vagrant  | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
        vagrant   | vagrant  | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
        (8 rows)

        vagrant=> \q
        vagrant@vagrant:/vagrant/tmp$ psql test < testData.sql    

    8) The last step is to install the psycopg2 dependency to connect python to the psql database.
    CD to the project directory where you pulled down the project file and run the following commands (note: 
    thtat since I have the package installed already, I get the following output.)
        vagrant@vagrant:/vagrant/tmp$ pip install -U pip
        Requirement already up-to-date: pip in /usr/local/lib/python2.7/dist-packages (18.1)
        vagrant@vagrant:/vagrant/tmp$ pip install psycopg2-binary
        Requirement already satisfied: psycopg2-binary in /usr/local/lib/python2.7/dist-packages (2.7.5)
        vagrant@vagrant:/vagrant/tmp$

    9) Run the program:
    vagrant@vagrant:/vagrant/tmp$ python3 logs_analysis.py
    

Expected output:
    vagrant@vagrant:/vagrant/logs_analysis$ python3 logs_analysis.py
    /usr/local/lib/python3.5/dist-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
    """)
    Hello! Project_1.py will be running three queries for you.  These queries will run sequentially, so please give each query time to run.

    1. What are the most popular three articles of all time?

    --------------------------------------------------
    title                                   views
    --------------------------------------------------
    Candidate is jerk, alleges rival        338647
    Bears love berries, alleges bear        253801
    Bad things gone, say good people        170098



    2. Who are the most popular article authors of all time?

    --------------------------------------------------
    name                                    views
    --------------------------------------------------
    Ursula La Multa                         507594
    Rudolf von Treppenwitz                  423457
    Anonymous Contributor                   170098
    Markoff Chaney                          84557



    3. On which days did more than 1% of requests lead to errors?

    --------------------------------------------------
    thedate                                 percent
    --------------------------------------------------
    2016-07-17                              2.26%



    vagrant@vagrant:/vagrant/logs_analysis$