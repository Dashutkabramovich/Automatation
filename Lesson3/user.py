class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def say_fm(self): 
       print("Имя:", self.first_name)
    def say_lm(self):
       print("Фамилия:", self.last_name)
    def say_all(self):
        print("Имя и Фамилия:", self.first_name, self.last_name)
        