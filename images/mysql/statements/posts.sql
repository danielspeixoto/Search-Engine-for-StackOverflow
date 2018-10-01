LOAD XML CONCURRENT LOCAL INFILE
'/custom/Posts.xml'
into table posts (Id, Title, Body, @AcceptedAnswerId, @AnswerCount,
 @CommentCount, @CreationDate, @LastActivityDate,
 @OwnerUserId, Score, @ViewCount, Tags, @PostTypeId, @ParentId)
 SET accepted_answer_id=@AcceptedAnswerId,
answer_count = @AnswerCount,
comment_count = @CommentCount,
creation_date = @CreationDate,
last_activity_date = @LastActivityDate,
owner_user_id = @OwnerUserId,
view_count = @ViewCount,
post_type_id = @PostTypeId,
parent_id = @ParentId;

INSERT INTO questions
(
Id, Title, Body, Score, Tags,
accepted_answer_id,
answer_count,
comment_count,
creation_date,
last_activity_date,
owner_user_id,
view_count
)
select
Id, Title, Body, Score, Tags,
accepted_answer_id,
answer_count,
comment_count,
creation_date,
last_activity_date,
owner_user_id,
view_count
from posts
where posts.post_type_id = 1;

INSERT INTO answers
(
Id, Title, Body, Score, Tags,
comment_count,
creation_date,
last_activity_date,
owner_user_id,
view_count,
parent_id
)
select
Id, Title, Body, Score, Tags,
comment_count,
creation_date,
last_activity_date,
owner_user_id,
view_count,
parent_id
from posts
where posts.post_type_id = 2;
