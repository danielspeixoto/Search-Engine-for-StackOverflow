from copy import copy
from typing import Dict

from src.main.domain.model.Post import Post


class Answer(Post):

    PARENT_ID = 'ParentId'

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)
        self.parent_id: int = self.init_int_var(self.PARENT_ID, data)

