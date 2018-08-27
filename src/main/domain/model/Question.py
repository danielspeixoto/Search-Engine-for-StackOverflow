from typing import Dict


class Question:

    ID = 'Id'
    BODY = 'Body'
    VIEW_COUNT = 'ViewCount'
    SCORE = 'Score'
    ANSWER_COUNT = 'AnswerCount'
    LAST_ACTIVITY_DATE = 'LastActivityDate'
    CREATION_DATE = 'CreationDate'
    ACCEPTED_ANSWER_ID = 'AcceptedAnswerId'
    OWNER_USER_ID = 'OwnerUserId'

    def __init__(self, dict: Dict[str, str]):
        self.id = dict[self.ID]
        self.body = dict[self.BODY]
        self.view_count = dict[self.VIEW_COUNT]
        self.score = dict[self.SCORE]
        self.answer_count = dict[self.ANSWER_COUNT]
        self.last_activity_date = dict[self.LAST_ACTIVITY_DATE]
        self.creation_date = dict[self.CREATION_DATE]
        self.accepted_answer_id = dict[self.ACCEPTED_ANSWER_ID]
        self.owner_user_id = dict[self.OWNER_USER_ID]