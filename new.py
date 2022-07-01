class Name:
    def __init__(self):
        self.name="paritosh"
        self.surname="kapadiya"
        print("name:",self.name)

    def show(self):
        ok=self.name
        return ("ok:",ok)   

d
a=Name()

class b(Name):
    def __init__(self):
        print("aaaaaaaa")

c=b()
print(c)

