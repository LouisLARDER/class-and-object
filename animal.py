class Animal:
  #initialize
   def __init__(self, name , age):
     #instance variable
      self.name = name
      self.age = age


  # instance meathod
   def speak(self):
     return f'my name is {self.name} and i am {self.age} years old'
     