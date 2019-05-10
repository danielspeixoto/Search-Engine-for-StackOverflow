from typing import Dict


class Post:
    ID = 'Id'
    BODY = 'Body'
    VIEW_COUNT = 'ViewCount'
    SCORE = 'Score'
    LAST_ACTIVITY_DATE = 'LastActivityDate'
    CREATION_DATE = 'CreationDate'
    OWNER_USER_ID = 'OwnerUserId'
    TITLE = 'Title'

    def __init__(self, data: Dict[str, str]):
        self._id: str = self.init_var(self.ID, data)
        self.title: str = self.init_var(self.TITLE, data)
        self.body: str = self.init_var(self.BODY, data)
        self.creation_date = self.init_var(self.CREATION_DATE, data)
        self.last_activity_date = self.init_var(self.LAST_ACTIVITY_DATE, data)
        self.owner_user_id: str = self.init_var(self.OWNER_USER_ID, data)
        self.view_count: int = self.init_int_var(self.VIEW_COUNT, data)
        self.score: int = self.init_int_var(self.SCORE, data)

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
        if other is not Post:
            return False
        return self.__dict__ == other.__dict__