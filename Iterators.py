# using print statements. 
class MyNumber:
    def __iter__(self,):
        self.n = 1
        return self
    def __next__(self):
        n = self.n
        self.n += 1
        return n
myclass = MyNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
# using for loop
class MyNumber:
    def __iter__(self,):
        self.n = 1
        return self
    def __next__(self):
        n = self.n
        self.n += 1
        return n
myclass = MyNumber()
myiter = iter(myclass)
for n in myiter:
    
# using StopIteration 
#class MyNumber:
    def __iter__(self,):
        self.n = 1
        return self
    def __next__(self):
        if self.n > 100:
            n = self.n
            self.n += 1
            return n
        else:
            raise StopIteration
myclass = MyNumber()
myiter = iter(myclass)
#for n in myiter:
    #print(n)
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
