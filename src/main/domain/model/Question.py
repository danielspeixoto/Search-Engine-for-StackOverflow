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
    TITLE = 'Title'

    def __init__(self, dict: Dict[str, str]):
        self.id: str = dict[self.ID]
        self.body: str = dict[self.BODY]
        self.view_count: int = int(dict[self.VIEW_COUNT])
        self.score: float = float(dict[self.SCORE])
        self.answer_count: int = int(dict[self.ANSWER_COUNT])
        self.last_activity_date = dict[self.LAST_ACTIVITY_DATE]
        self.creation_date = dict[self.CREATION_DATE]
        self.accepted_answer_id: str = dict[self.ACCEPTED_ANSWER_ID] \
                if self.ACCEPTED_ANSWER_ID in dict \
                else None
        self.owner_user_id: str = dict[self.OWNER_USER_ID]
        self.title: str = dict[self.TITLE]

    def __eq__(self, other):
        return self.__dict__ == other.__dict__