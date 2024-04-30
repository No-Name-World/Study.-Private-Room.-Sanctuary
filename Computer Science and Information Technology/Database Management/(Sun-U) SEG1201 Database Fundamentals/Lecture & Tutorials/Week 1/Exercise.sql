# Exercise 1
A.
CREATE TABLE student (
    student_name varchar2(20),
    gender char(6),
    DOB DATE,
    CGPA NUMBER(*,1)    
);

desc student

B. 
INSERT INTO student VALUES ('George','Male','1 Jan 2001','3.2');
INSERT INTO student VALUES ('Jane','Female','21 Dec 1999','2.6');

C.
SELECT *
FROM student;

D.
DELETE FROM student 
WHERE student_name = 'George'
