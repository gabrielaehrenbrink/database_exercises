-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('gabi123', 'gabi@gmail.com');
INSERT INTO users (username, email) VALUES ('john_doe', 'john.doe@example.com');
INSERT INTO users (username, email) VALUES ('alice_smith', 'alice.smith@example.com');
INSERT INTO users (username, email) VALUES ('robert_jones', 'robert.jones@example.com');
INSERT INTO users (username, email) VALUES ('emily_miller', 'emily.miller@example.com');


-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int
);

INSERT INTO posts (title, content, views, user_id) VALUES ('title', 'my contents', 2, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('another post', 'different content', 8, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('long post', 'This is a much longer content for the post. It can include multiple sentences or paragraphs.', 12, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('popular post', 'interesting content', 20, 2);
