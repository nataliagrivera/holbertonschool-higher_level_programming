-- Prints the description of the table first_table from database hbtn_0c_0 in your MySQL server.
USE information_schema;

SELECT COLUMN_NAME, COLUMN_TYPE
FROM COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
