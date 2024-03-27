class Author:
    def __init__(self, id, name, email="def@mail.ru"):
        self.id = id
        self.name = name
        self.email = email
        
    def __repr__(self):
        return f"Author({self.id}): {self.name}|{self.email}"


class Learner:
    def __init__(self, uid, name, final_test):
        self.uid = uid
        self.name = name
        self.final_test = final_test

    def __repr__(self):
        return f"Author({self.uid}): {self.name}|{self.final_test}"