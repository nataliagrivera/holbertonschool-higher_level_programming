-- Create unique_id on server. Int with default value of 1 and must be unique.
CREATE TABLE IF NOT EXIST unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256)
    UNIQUE (id)
);