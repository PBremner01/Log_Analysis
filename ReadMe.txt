Readme for bremnerphilip Udacity Full Stack Developer NC
	Project 3 - Log Analysis Reporting

		Purpose: Your task is to create a reporting tool that prints out reports (in plain text) 			based on the data in the database. This reporting tool is a Python program using 			the psycopg2 module to connect to the database.

		Notes: The report runs off the Udacity supplied "news" db.  Some assoicated views (see 			below) were created on the DB.

 
Used Libraries:
  psycopg2 -  a DB API 2.0 compliant PostgreSQL driver that is actively developed. It is designed for 		multi-threaded applications and manages its own connection pool.

To run:
  1. Place file is choosen directory.
      Files:  LogAnalysisV2.py

  2. In Vagrant ( running ) run : python LogAnalysisV2.py
		Note: Using Python Vs 3.6

Created Views for question #3 support:
create view log_total_cnt_by_day as select time::timestamp::date as logdate, 
count(id) as total_cnt  
from log
group by logdate
order by logdate asc;


create view log_percent_failed as select l.time::timestamp::date as logdate, (cast(count(l.id) as float) / cast((t.total_cnt) as float) * 100) as perc_failed
from log as l
inner join log_total_cnt_by_day as t
on l.time::timestamp::date = t.logdate
where l.status <> '200 OK'
group by l.time::timestamp::date, t.total_cnt
