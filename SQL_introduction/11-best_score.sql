-- Lists all rrecords with a score of 10 or less in second_table.

SELECT score, name FROM second_table HAVING score>=10 ORDER BY score DESC;