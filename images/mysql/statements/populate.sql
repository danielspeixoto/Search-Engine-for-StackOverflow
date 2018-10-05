USE `qa`;

LOAD XML CONCURRENT LOCAL INFILE
'/custom/Users.xml'
into table qa.users ( Id,
  Reputation,
  UpVotes,
  DownVotes,
  @LastAccessDate,
  Views,
  @CreationDate)
 SET last_access_date = @LastAccessDate,
  creation_date = @CreationDate;

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


LOAD XML CONCURRENT LOCAL INFILE
'/custom/Links.xml'
into table qa.links ( Id,
  @PostId,
  @RelatedPostId,
  @LinkTypeId,
  @CreationDate)
 SET post_id = @PostId,
type = @LinkTypeId,
 related_post_id = @RelatedPostId,
  creation_date = @CreationDate;