class Person:

    def say(self, message):
        print(message)
    def say_hello(self):
        self.say("Hello work")

tom = Person()
tom.say_hello("hello work")