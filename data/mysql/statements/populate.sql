LOAD XML CONCURRENT LOCAL INFILE
'/custom/Posts.xml'
into table Posts (Id, Title, Body, @AcceptedAnswerId, @AnswerCount,
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