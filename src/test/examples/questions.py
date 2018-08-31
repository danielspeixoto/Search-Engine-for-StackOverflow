from src.main.domain.model.Question import Question


def question() -> Question:
    return Question({
        Question.ID: "1",
        Question.BODY: "That's a body",
        Question.VIEW_COUNT: 1,
        Question.SCORE: 3,
        Question.ANSWER_COUNT: 1,
        Question.LAST_ACTIVITY_DATE: "2013-05-22T00:28:24.497",
        Question.CREATION_DATE: "2013-05-21T22:27:22.957",
        Question.ACCEPTED_ANSWER_ID: "2",
        Question.OWNER_USER_ID: "3",
        Question.TITLE: "A fun title",
    })


def questions() -> [Question]:
    return [question(),
        Question({
            Question.ID: "4",
            Question.BODY: "That's a body too",
            Question.VIEW_COUNT: 10,
            Question.SCORE: 30,
            Question.ANSWER_COUNT: 10,
            Question.LAST_ACTIVITY_DATE: "2013-05-22T19:49:51.107",
            Question.CREATION_DATE: "2013-05-22T19:00:16.933",
            Question.ACCEPTED_ANSWER_ID: "5",
            Question.OWNER_USER_ID: "6",
            Question.TITLE: "Not a fun title",
        })
    ]