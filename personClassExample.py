class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name + " and my age is " + str(abc.age))

p1 = Person("John", 36)
p1.age = 40

p1.myfunc()
