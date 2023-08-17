
class Person:

    # A name attribute for the person.  
    def __init__(self,name):
        self.name=name

    # A method for someone talking.
    def talk(self):
        print("Hi my name is "+self.name)


person1=Person("Jonathan")
person1.talk()

person2=Person("Dimitri")
person2.talk()