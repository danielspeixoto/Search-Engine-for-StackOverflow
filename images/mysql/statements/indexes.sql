USE `qa`;

CREATE INDEX parent ON posts(parent_id);
CREATE INDEX owner ON posts(owner_user_id);
CREATE INDEX related ON links(post_id);
CREATE INDEX kind ON links(post_id, type);
