#Exam 1

#Q4
SELECT  CONCAT(lastname, ', ', firstname) AS student_name, major, gpa
FROM student
WHERE major REGEXP '^BIO' AND (GPA BETWEEN 3.0 AND 3.5)
ORDER BY lastname, firstname;

#Q5
SELECT major, count(studentid) AS number_of_students, avg(gpa) AS average_gpa
FROM student
GROUP BY major;

#Q6 & 7
SELECT s.lastname, s.firstname
FROM student s 
	JOIN enrollment e
		ON s.studentid = e.studentid
	JOIN course c 
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Discrete Math' AND e.grade REGEXP 'A|B';


#Q9
#student that tooke calc 1 with a grade of c and higher
SELECT e.studentid
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE (grade REGEXP 'A|B|C' and c.name REGEXP 'Calculus 1') AND (c.name REGEXP 'Calculus 2' and e.semester REGEXP '2018Spring');

#student taking calc 2
SELECT e.studentid
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Calculus 2' and e.semester REGEXP '2018Spring';

SELECT e.studentid
FROM (SELECT e2.studentid, c2.name
		FROM enrollment e2 join course c2
			ON c2.courseid = e2.courseid
		WHERE e2.grade REGEXP 'A|B|C' and c2.name REGEXP 'Calculus 1') 
WHERE c.name REGEXP 'Calculus 2' and e.semester REGEXP '2018Spring';


SELECT e.studentid
FROM enrollment e join (SELECT e.studentid
					FROM enrollment e join course c
					ON c.courseid = e.courseid
					WHERE grade REGEXP 'A|B|C' and c.name REGEXP 'Calculus 1') t
WHERE c.name REGEXP 'Calculus 2' and e.semester REGEXP '2018Spring';

#final answer
SELECT e.studentid
FROM enrollment e 
		join course c
			ON c.courseid = e.courseid
        JOIN (SELECT e2.studentid, c2.courseid
				FROM enrollment e2 join course c2
					ON c2.courseid = e2.courseid
				WHERE grade REGEXP 'A|B|C' and c.name REGEXP 'Calculus 1') p 
            ON c.courseid=p.courseid
WHERE c.name REGEXP 'Calculus 2' and e.semester REGEXP '2018Spring';

#Q10
# students in calc 1
SELECT e.studentid
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Calculus 1';

#student in clac2
SELECT e.studentid
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Calculus 2';

#final answer
SELECT clc1.instructor AS InstructorCaculus1, count(clc2.studentid) AS NumberTakingCalculus2, 
		AVG(CASE clc1.grade 
			WHEN 'A' THEN 4.0
            WHEN 'B' THEN 3.0
			WHEN 'C' THEN 2.0
            WHEN 'D' THEN 1.0
		END) AS AverageGradeCalculus2 
FROM (SELECT e1.studentid, c1.instructor, e1.grade
		FROM enrollment e1 join course c1
		ON c1.courseid = e1.courseid
		WHERE c1.name REGEXP 'Calculus 1') clc1
	JOIN (SELECT e2.studentid, c2.instructor, e2.grade
			FROM enrollment e2 join course c2
			ON c2.courseid = e2.courseid
			WHERE c2.name REGEXP 'Calculus 2') clc2
	ON clc1.studentid = clc2.studentid
GROUP BY InstructorCaculus1;

#Q11
Select e.studentid, c.name, e.semester, e.grade, e.units
FROM enrollment e
	JOIN course c 
		ON c.courseid = e.courseid
WHERE studentid = '5430'
ORDER BY semester;

#Q12
SELECT e.studentid, count(e.studentid), min(e.grade)
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Discrete Math' AND e.grade < 'D'
GROUP BY e.studentid, e.grade;

SELECT e.studentid, count(c.name REGEXP 'Discrete Math') AS num_of_times_taken, min(e.grade)As highestgrade
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP '^Calculus'
GROUP BY e.studentid;

#final answer
SELECT e.studentid, count(c.name REGEXP 'Discrete Math') AS num_of_times_taken, min(e.grade) As highestgrade,
	IF(count(c.name REGEXP 'Discrete Math') = 2 and count(e.grade > 'C') =2, '1', '0') AS taken_n_failx2,
    IF(count(c.name REGEXP 'Discrete Math') <=2 and e.grade < 'C' , '1', '0') AS taken_n_passed
FROM enrollment e join course c
		ON c.courseid = e.courseid
WHERE c.name REGEXP 'Discrete Math' AND e.grade < 'D'
GROUP BY e.studentid, e.grade;

#Q13
#find that student
Select e.studentid, s.lastname, c.name, e.semester, e.grade, e.units
FROM student s 
	JOIN enrollment e
		ON s.studentid = e.studentid
	JOIN course c 
		ON c.courseid = e.courseid
WHERE s.lastname = 'Last14' and c.name = 'Discrete Math'
;


# Final Answer
UPDATE student s 
	JOIN enrollment e
		ON s.studentid = e.studentid
	JOIN course c 
		ON c.courseid = e.courseid
SET grade = 'A'
WHERE s.lastname = 'Last14' and c.name = 'Discrete Math';

#Q16
create index name_index on world.country(name);
         
select * from world.country where code='USA' and name='United States';

select * from world.country where code='USA' or name='United States';

