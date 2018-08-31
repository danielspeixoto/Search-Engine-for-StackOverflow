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
        try:
            self.question_id: str = self.init_var(self.ID, dict)
            self.title: str = self.init_var(self.TITLE, dict)
            self.body: str = self.init_var(self.BODY, dict)
            self.creation_date = self.init_var(self.CREATION_DATE, dict)
            self.last_activity_date = self.init_var(self.LAST_ACTIVITY_DATE, dict)
            self.owner_user_id: str = self.init_var(self.OWNER_USER_ID, dict)

            self.answer_count: int = self.init_int_var(self.ANSWER_COUNT, dict)
            self.view_count: int = self.init_int_var(self.VIEW_COUNT, dict)
            self.score: int = self.init_int_var(self.SCORE, dict)

            self.accepted_answer_id: str = self.init_var(self.ACCEPTED_ANSWER_ID, dict)
        except:
            print(self.question_id)

    def init_var(self, content: str, dict):
        return dict[content] \
            if content in dict \
            else None


    def init_int_var(self, content: str, dict):
        res = self.init_var(content, dict)
        if res is not None:
            res = int(res)
        return res

    def __eq__(self, other):
        if other is not Question:
            return False
        return self.__dict__ == other.__dict__
