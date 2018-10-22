#Prompts
INITIAL_PROMPT = 'Hello! Project_1.py will be running three queries for you.  These queries will run sequentially, so please give each query time to run. \n'


#questions
QUESTION_1 = '1. What are the most popular three articles of all time? \n'
QUESTION_2 = '2. Who are the most popular article authors of all time? \n'
QUESTION_3 = '3. On which days did more than 1% of requests lead to errors? \n'  

#queries

QUERY_1 = """select fixed_articles.title as Title , count(log.path) as Views
from (select concat('/article/',articles.slug) as mod_path, title from articles) as fixed_articles
join log  on log.path = fixed_articles.mod_path
where log.status !='404 NOT FOUND' and log.path != '/'
group by log.path, fixed_articles.title
order by Views desc 
limit 3; \n """

QUERY_2 = """select authors.name as Name, sum(top_articles.Views) as Views
from authors 
join ( select fixed_articles.author, fixed_articles.title,  count(log.path) as Views
    from (select concat('/article/',articles.slug) as mod_path, title, author from articles) as fixed_articles
    join log  on log.path = fixed_articles.mod_path
    where log.status !='404 NOT FOUND' and log.path != '/'
    group by log.path, fixed_articles.title, fixed_articles.author
    order by Views desc ) as top_articles
on top_articles.author = authors.id
group by authors.name
order by views desc; \n """

QUERY_3 = """select totalRequestsForDay.theDate, (round(( CAST(errors.totalRequests as DECIMAL) /  CAST(totalRequestsForDay.totalRequests as DECIMAL) ) * 100, 2) || '%') as Percent
from (
    select  time::timestamp::date as theDate,  count(time::timestamp::date) as totalRequests
    from log
    group by theDate
) as totalRequestsForDay
join  (select  time::timestamp::date as theDate, status,  count(time::timestamp::date) as totalRequests
        from log
        group by theDate, status
        having status like '%404%')  as errors
on totalRequestsForDay.theDate = errors.theDate
where 
     errors.theDate = totalRequestsForDay.theDate
    and (( CAST(errors.totalRequests as DECIMAL) /  CAST(totalRequestsForDay.totalRequests as DECIMAL) ) >= .01);
 \n """ 
