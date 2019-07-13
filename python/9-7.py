class User():
    def __init__(self,first_name,last_name,user_age):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
    def describe_user(self):
        print("name: "+ self.first_name.title()+self.last_name.title())
        print("age: " + str(self.user_age))     #此处int型数字需转换成string
    def greet_user(self):
        print("hello")

class Admin(User):
    def __init__(self,first_name,last_name,user_age):
        super().__init__(first_name,last_name,user_age)
        self.privileges = []
    def addPrivileges(self,privileges=[]):
        self.privileges = privileges
    def showPrivileges(self):
        print(self.first_name.title()+self.last_name.title()+"'s privileges:")
        for privilege in self.privileges:
            print(privilege)

lorwaysan = Admin("lorway",'san',21)
lorwaysan.describe_user()
lorwaysan.addPrivileges(["root","RWX777"])
lorwaysan.showPrivileges()