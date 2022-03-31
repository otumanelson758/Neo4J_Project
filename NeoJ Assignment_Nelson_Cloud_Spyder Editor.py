# -*- coding: utf-8 -*-
"""
Nelson Cloud Spyder Editor

This is a temporary script file.
"""
Project:
Neo4J Fundamentals -Nelson  Otuma Ongaya

1. Introduction

You have been given the task of answering the following questions using a graph consisting of
an institution's data. The nodes and relationships are specified in Cypher as shown:

2. Creation - Nodes and relationships

#MATCH (n) DETACH DELETE n;

CREATE (s1: Student {studentID: "1", lastName: "Doe", firstName: "Ana", middleName: "Maria"})
CREATE (r1: Room {roomName: "Pascal"})
CREATE (p1: Project {projectNr: "34", projectName: "eCommerce database"})
CREATE (c1: Course {courseNr: "1", courseName: "Databases"})
CREATE
	(c1) – [:TAKESPLACEIN] –> (r1),
	(s1) – [:ENROLLEDIN] –> (c1),
	(s1) – [:WORKSON {hours: 1} ] –> (p1)
 
CREATE (s2: Student {studentID: "2", lastName: "Ung", firstName: "Peter", middleName: "John"})
CREATE (c2: Course {courseNr: "2", courseName: "Programming"})
CREATE (p2: Project {projectNr: "24", projectName: "eCommerce website"})
CREATE (r2: Room {roomName: "Seminar C"})
CREATE
	 (c2) – [:TAKESPLACEIN] –> (r2),
     (s2) – [:ENROLLEDIN] –> (c1),
     (s1) – [:WORKSON {hours: 2} ] –> (p2),
     (s2) – [:WORKSON {hours: 3} ] –> (p1),
     (s2) – [:WORKSON {hours: 4} ] –> (p2)

CREATE (s3: Student {studentID: "3", lastName: "Doe", firstName: "John"})
CREATE (c3: Course {courseNr: "3", courseName: "Graphics"})
CREATE (p3: Project {projectNr: "13", projectName: "User interface"})
CREATE (r3: Room {roomName: "Alpha"})
CREATE
	(c1) – [:TAKESPLACEIN] –> (r3),
	(s3) – [:ENROLLEDIN] –> (c2),
	(s2) – [:WORKSON {hours: 1} ] –> (p3),
	(s3) – [:WORKSON {hours: 1} ] –> (p1),
	(s3) – [:WORKSON {hours: 2} ] –> (p2)
	
CREATE (s4: Student {studentID: "4", lastName: "Berre", firstName: "Stine"})
CREATE (p4: Project {projectNr: "26", projectName: "Reporting"})
CREATE (r4: Room {roomName: "Beta"})
CREATE
	(c1) – [:TAKESPLACEIN] –> (r4),
	(s4) – [:ENROLLEDIN] –> (c1),
	(s2) – [:WORKSON {hours: 1} ] –> (p4),
	(s3) – [:WORKSON {hours: 3} ] –> (p4)

CREATE (s5: Student {studentID: "5", lastName: "Travolta", firstName: "John"})

3. Specify the following queries in Cypher and execute them in Neo4j.

Question 1
In which rooms do courses with course number "1" take place? Retrieve the course
name and the names of the rooms in which the course takes place.

Cypher:

MATCH (c:Course {courseNr: '1'})-[:TAKESPLACEIN]->(r:Room)
RETURN c.courseName AS Course_Name, r.roomName AS Room_Name

Output:

+-------------------------+
¦"Course_Name"¦"Room_Name"¦
¦-------------+-----------¦
¦"Databases"  ¦"Beta"     ¦
+-------------+-----------¦
¦"Databases"  ¦"Alpha"    ¦
+-------------+-----------¦
¦"Databases"  ¦"Pascal"   ¦
+-------------------------+

Question 2
How many hours and in which projects do students with student number "1" works?
Retrieve the first name of the student, the project the student works on, and the
corresponding number of hours worked on the project.

Cypher:

MATCH (s:Student {studentID: '1'})-[rel:WORKSON]->(p:Project)
RETURN s.firstName AS Student_First_Name, p.projectName AS Project_Name, sum(rel.hours) AS Project_Hours

Output:

+---------------------------------------------------------+
¦"Student_First_Name"¦"Project_Name"      ¦"Project_Hours"¦
¦--------------------+--------------------+---------------¦
¦"Ana"               ¦"eCommerce website" ¦2              ¦
+--------------------+--------------------+---------------¦
¦"Ana"               ¦"eCommerce database"¦1              ¦
+---------------------------------------------------------+


Question 3
Which students and how many hours do they work on the project with project number
"24"? Retrieve the project name, the last name of the student and the corresponding
number of hours worked on the project.

Cypher:

MATCH (s:Student )-[rel:WORKSON]->(p:Project{projectNr:'24'})
RETURN s.lastName AS Student_Last_Name, p.projectName AS Project24_Name,sum(rel.hours) AS Project_Hours

Output:

+-------------------------------------------------------+
¦"Student_Last_Name"¦"Project24_Name"   ¦"Project_Hours"¦
¦-------------------+-------------------+---------------¦
¦"Doe"              ¦"eCommerce website"¦4              ¦
+-------------------+-------------------+---------------¦
¦"Ung"              ¦"eCommerce website"¦4              ¦
+-------------------------------------------------------+

Question 4
Which students work on which projects and how many hours? Retrieve the last name of
the students, the name of the projects they work on, and the corresponding number of
hours. Order the results by the last name of the students. Limit the results to four.

Cypher:

MATCH (s:Student )-[rel:WORKSON]->(p:Project)
RETURN s.lastName AS Student_Last_Name, p.projectName AS Project_Name,sum(rel.hours) AS Project_Hours ORDER BY s.lastName LIMIT 4

Output:

+--------------------------------------------------------+
¦"Student_Last_Name"¦"Project_Name"      ¦"Project_Hours"¦
¦-------------------+--------------------+---------------¦
¦"Doe"              ¦"eCommerce website" ¦4              ¦
+-------------------+--------------------+---------------¦
¦"Doe"              ¦"Reporting"         ¦3              ¦
+-------------------+--------------------+---------------¦
¦"Doe"              ¦"eCommerce database"¦2              ¦
+-------------------+--------------------+---------------¦
¦"Ung"              ¦"Reporting"         ¦1              ¦
+--------------------------------------------------------+

Question 5
Which students work on more than two projects and on how many projects exactly?
Retrieve the last name of the students and the corresponding number of projects. Order
the results by the number of projects.

Cypher 1:

MATCH (s:Student )-[rel:WORKSON]->(p:Project)
RETURN s.lastName AS Student_Last_Name, count(rel) AS No_of_Projects ORDER BY count(rel)
# Using firstName instead of lastName as s1 and s3 have the same lastName

Output 1:

+------------------------------------+
¦"Student_Last_Name"¦"No_of_Projects"¦
¦-------------------+----------------¦
¦"Ung"              ¦4               ¦
+-------------------+----------------¦
¦"Doe"              ¦5               ¦
+------------------------------------+

Cypher 2:

MATCH (s:Student )-[rel:WORKSON]->(p:Project)
RETURN s.firstName AS Student_First_Name, count(rel) AS No_of_Projects ORDER BY count(rel)

Output 2:

¦"Student_First_Name"¦"No_of_Projects"¦
¦--------------------+----------------¦
¦"Ana"               ¦2               ¦
+--------------------+----------------¦
¦"John"              ¦3               ¦
+--------------------+----------------¦
¦"Peter"             ¦4               ¦
+-------------------------------------+

Question 6
Which students have the same last name and work on the same projects? Retrieve the
first name of the students and the name of the projects they share.

Cypher:

MATCH (x:Student)-[:WORKSON]->(y:Project),(x1:Student)-[:WORKSON]->(y1:Project)
WHERE x.lastName = x1.lastName AND y.projectName = y1.projectName
RETURN DISTINCT x.firstName AS Student_First_Name, y.projectName AS Project_Name ORDER BY x.firstName;

Output:

+-----------------------------------------+
¦"Student_First_Name"¦"Project_Name"      ¦
¦--------------------+--------------------¦
¦"Ana"               ¦"eCommerce website" ¦
+--------------------+--------------------¦
¦"Ana"               ¦"eCommerce database"¦
+--------------------+--------------------¦
¦"John"              ¦"eCommerce website" ¦
+--------------------+--------------------¦
¦"John"              ¦"eCommerce database"¦
+-----------------------------------------+

"Python 3.9.7 (default, Sep 16 2021, 16:59:28) [MSC v.1916 64 bit (AMD64)]
