from schema import LearnerSchema
from author import Learner
from author import Author
from schema import AuthorSchema
from pprint import pprint

# Примеры из практики

# json_data = """
# {
#    "id": 99,
#    "name": "Ivan",
#    "email": "ivan@mail.ru"
# }
# """

# schema = AuthorSchema()
# result = schema.loads(json_data)
# print(result)

# json_data = """
# [
#    {
#        "id": 1,
#        "name": "Alex",
#        "email": "alex@mail.ru"
#    },
#    {
#        "id": 2,
#        "name": "Ivan",
#        "email": "ivan@mail.ru"
#    },
#    {
#        "id": 4,
#        "name": "Tom",
#        "email": "tom@mail.ru"
#    }
# ]
# """
# schemas = AuthorSchema(many=True)
# result = schemas.loads(json_data)
# print(result)


# Домашнее задание


json_data = """
[
   {
        "uid": 1,
        "name": "Alex",
        "final_test": true
   },
   {
        "uid": 2,
        "name": "Ivan",
        "final_test": false
   },
   {
        "uid": 4,
        "name": "Tom",
        "final_test": true
   }
]
"""
# Для работы со списком не забываем указать аргумент <many>(many=True)
schema = LearnerSchema(many=True)
result = schema.loads(json_data)
pprint(result)
