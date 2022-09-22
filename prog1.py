# this is a comment
# program that prints hello world

print('Hello World!')

# create a class named MyClass (starts with capital), with a property named x
class MyClass:
    x = 5

# now create an instance of that class
p1 = MyClass()
print(p1.x)

# the built in __init()__ function of every class
class Person:
    def __init__(self, name, age): #the self parameter always goes in there
        # but during usage, there is only two parameters
        # to change the value of the class's own attributes,
        # use the self.variableName syntax
        # PS the 'self' can be called anything, as long as it is
        # the first parameter, python will recognise it as 'self'
        self.name = name
        self.age = age

p2 = Person("John", 36) # this is like a C++ constructor

print(p2.name)
print(p2.age)

# methods inside class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name + " and I am " +
                self.age + " years old")

p3 = Person("John", 36)
p3.myfunc()
