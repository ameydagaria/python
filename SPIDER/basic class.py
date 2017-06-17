Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> class car:
	def __init__(self,make,model):
		self.make = make
		self.model=model
		print("hello")

		
>>> print(self.make)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(self.make)
NameError: name 'self' is not defined
>>> class car :
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def display (self):
		print("yo",self.make)
		print("yo",self.model)
		print("yo",self.year)
car1 = car('a','b',2123)
SyntaxError: invalid syntax
>>> class car :
	def __init__(self,make,model,year):
		self.make = make
		self.model = model
		self.year = year
	def display (self):
		print("yo",self.make)
		print("yo",self.model)
		print("yo",self.year)

		
>>> car1 = car("c","d",214)
>>> car1.display()
('yo', 'c')
('yo', 'd')
('yo', 214)
>>> print (car1.make)
c
>>> 
