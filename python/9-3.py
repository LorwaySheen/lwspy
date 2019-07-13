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

lisa = User('lisa',"su",43)
lisa.describe_user()
lisa.greet_user()