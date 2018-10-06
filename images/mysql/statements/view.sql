use qa;
CREATE VIEW answers_to_a_question AS
    SELECT posts.*, users.reputation as user_reputation FROM qa.posts JOIN qa.users
    ON posts.owner_user_id = users.id WHERE posts.post_type_id = 2 ORDER BY score DESC;
CREATE VIEW questions AS
    SELECT posts.*, users.reputation as user_reputation
     FROM qa.posts JOIN qa.users ON posts.owner_user_id = users.id WHERE posts.post_type_id = 1;