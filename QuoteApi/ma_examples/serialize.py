from pprint import pprint
from random import choice
from schema import LearnerSchema
from author import Learner
from author import Author
from schema import AuthorSchema

# Примеры из практики

# author = Author("123", "Alex", "alex5@mail.ru")
# author_schema = AuthorSchema()
# result = author_schema.dump(author)
# print(result, type(result))

# authors = [
#     Author("1", "Alex"),
#     Author("1", "Ivan"),
#     Author("1", "Tom")
# ]
# authors_schema = AuthorSchema(many=True)
# result = authors_schema.dump(authors)
# print(result, type(result))


# Домашнее задание
# Один экземпляр
learner = Learner(1, "Alex", True)
learner_schema = LearnerSchema()
result = learner_schema.dump(learner)
print(result)

# Список экземпляров
learners = [
    Learner("1", "Alex", True),
    Learner("2", "Ivan", False),
    Learner("3", "Tom", True)
]
schemas = LearnerSchema(many=True)
res = schemas.dump(learners)
pprint(res)


# Реализация проверки типов через pattern matching
print('==== CHECK ONE ====')
data = choice([learners, learner])
match type(data):
    case s if s is Learner:
        learner_schema = LearnerSchema()
        result = learner_schema.dump(data)
        print(result)
    case s if s is list:
        schemas = LearnerSchema(many=True)
        res = schemas.dump(data)
        pprint(res)

print('==== CHECK TWO ====')
data = choice([learners, learner])
match data:
    case Learner():
        learner_schema = LearnerSchema()
        result = learner_schema.dump(data)
        print(result)
    case list():
        schemas = LearnerSchema(many=True)
        res = schemas.dump(data)
        pprint(res)

