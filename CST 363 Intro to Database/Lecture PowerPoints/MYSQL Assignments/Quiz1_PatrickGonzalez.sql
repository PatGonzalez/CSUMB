/*Using MySQL Workbench, create a new schema names “art”.  
Download the sql script “Art Course Tables.sql” and execute this script to create the tables Customer, Course, Enrollment.  
The Art Course database is described on pages 9 and 10 of chapter 1.  Use the Art Course database tables to answers questions 3 and 4.*/

#3
SELECT CourseNumber, Course, CourseDate
FROM course
WHERE course REGEXP 'oil';

#4
SELECT Course, CourseNumber, CourseDate
FROM course
WHERE coursedate >= '2015-10-01' and course REGEXP 'Pastels';

#5 
SELECT DISTINCT customerlastname AS 'Student Last Name', customerfirstname AS 'Student First Name'
FROM course cr 
	JOIN enrollment e
		ON cr.CourseNumber=e.CourseNumber
	JOIN customer c
		ON e.CustomerNumber=c.CustomerNumber
WHERE e.coursenumber IN 
	(SELECT coursenumber
     FROM course
     WHERE course REGEXP 'Pastels');

