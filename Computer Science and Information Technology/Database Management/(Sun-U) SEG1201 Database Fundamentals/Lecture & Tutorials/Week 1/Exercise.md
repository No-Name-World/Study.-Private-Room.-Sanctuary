# Exercise 1 - Using Oracle Apex (SQL Workshop)
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

E.
DELETE FROM student 
WHERE student_name = 'George'

F.
DROP TABLE student;


---

# Exercise 2 - Using Oracle Apex (SQL Workshop)
A. 
CREATE TABLE product (
    id CHAR(5),
    name VARCHAR2(20),
    description VARCHAR(50),
    quantity NUMBER(5,0),
    price_per_unit NUMBER(*,2)    
);

DESC product;

B.
INSERT INTO product VALUES ('B-100','book','materials of schools','10','1');
INSERT INTO product VALUES ('S-201','shoes','shoes for kindergarten','300','2.5');
INSERT INTO product VALUES ('N-122','snacks','snacks for break time','400','1');
INSERT INTO product VALUES ('B-101','magazine','magazine for the office','50','99.90');

C.
SELECT * FROM product;

D.
DELETE FROM product
WHERE quantity > 280;

SELECT * FROM product;
