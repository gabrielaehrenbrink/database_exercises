DROP TABLE posts CASCADE;
DROP TABLE comments;

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text, 
    content text
);

CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    title_comment text,
    content_comment text, 
    author text,
    post_id int,
    constraint fk_post foreign key(post_id) references posts(id)
    on delete cascade
);


-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content) VALUES ('Post title', 'Lots of content');
INSERT INTO posts (title, content) VALUES ('New title', 'very good content');
INSERT INTO posts (title, content) VALUES ('Old title', 'terrible content');

INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('Loved it', 'This post is amazing', 'gabs123', 1);
INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('amazing', 'cool blog', 'misterious_author', 1);
INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('Nice', 'very interesting', 'john', 1);
INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('terrible', 'This post is very bad', 'gabs123', 2);
INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('wow', 'love it love it', 'gabs123', 3);
INSERT INTO comments (title_comment, content_comment, author, post_id) VALUES ('ok', 'not impressive', 'mary321', 2)
