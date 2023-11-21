-- Script that lists all records of the table second_table with the highest score.

SELECT score, name FROM second_table WHERE score = (SELECT MAX(score) FROM second_table);