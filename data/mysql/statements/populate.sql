LOAD XML CONCURRENT LOCAL INFILE
'/custom/Posts.xml'
into table Posts (Id, Title, Body, AcceptedAnswerId, AnswerCount, CommentCount,
CreationDate, LastActivityDate, OwnerUserId, Score, ViewCount, Tags, PostTypeId, ParentId);