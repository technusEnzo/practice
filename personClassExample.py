class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Method function
  def myfunc(self):
    print("Hello my name is " + self.name + " and my age is " + str(self.age))

p1 = Person("John", 36)
p1.age = 40

p1.myfunc()
