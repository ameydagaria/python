Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print ("hello lets start this journey")
hello lets start this journey
>>> print ("forever and ever ") #comment
forever and ever 
>>> number = 1
>>> print(type(number))
<type 'int'>
>>> print ("""hello  """)
hello  
>>> num = "hard"
>>> print(num[0])
h
>>> hello = [1,2,3,4]
>>> print(hello[-1])
4
>>> dict = {'key1':'montreal','key2':'abc'}
>>> print (dict('key1'))

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print (dict('key1'))
TypeError: 'dict' object is not callable
>>> print (dict['key1'])
montreal
>>> hello = input("enter")
enterhello
>>> hello = input("")
12
>>> print(hello)
12
>>> number = 2
>>> if(number==2):
	print("ola")

	
ola
>>> number = (int (input (""))
	  if(number==2) : print("two")
	  
SyntaxError: invalid syntax
>>> number = int (input())
2
>>> print (number)
2
>>> number = int(input())
23
>>> if(number==2) : print("two")
       elif (number==23) : print("yes")
       
  File "<pyshell#25>", line 3
    elif (number==23) : print("yes")
    ^
IndentationError: unexpected indent
>>> if(number==2) : print("two")
elif (number==23) : print("yes")
else : print("holla")

yes
>>> if (number==2):
	print("d")
else:
	print("no")

	
no
>>> x = true

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x = true
NameError: name 'true' is not defined
>>> x = 'true'
>>> y = 'true'
>>> z = x or y
>>> print'z'
z
>>> print z
true
>>> number = 10
>>> whime (number<=10):
	
SyntaxError: invalid syntax
>>> while (number<=10):
	print (number)
	number++;
	
SyntaxError: invalid syntax
>>> while (number<=10):
	print (number)
	number++
	
SyntaxError: invalid syntax
>>> while (number<=10):
	print (number)
	number=number+1

	
10
>>> for number in range (0,100,1):
	print(number)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
>>> number = 100
>>> while (number<=100):
	number=number-1
	if (number==50):
		break
	else
	
SyntaxError: invalid syntax
>>> number = 100
>>> while (number<=100):
	number=number-1
	if (number==50):
		break
	else :
		
>>> continue
SyntaxError: 'continue' not properly in loop
>>> 
>>> number = 100
>>> while (number<=100):
	number=number-1
	if (number==50):
		break
	else : continue
	
>>> 
>>> number = 100
>>> while (number<=100):
	number=number-1
	if (number==50):
		print(number)
		
		break
	else : continue

	
>>> 
>>> number = 0
>>> while (number<=)
SyntaxError: invalid syntax
>>> 
>>> number = 10
>>> while(number<=50):
	number=number+1
	if(number==40):
		print(number)

		
40
>>> while(number<=50):
	number=number+1
	 print(number)
	if(number==40):
		
  File "<pyshell#73>", line 4
    print(number)
    ^
IndentationError: unexpected indent
>>> while (number<=50):
	number=number+1
	print(number)
	if(number==40):
		break

	
>>> number = 11
>>> while (number>=1)
SyntaxError: invalid syntax
>>> while number>=1 :
	number=number-1
	print number

	
10
9
8
7
6
5
4
3
2
1
0
>>> while number>=1 :
	number=number-1
	if number == 5:
		continue
	
	print number

	
>>> number= 11
>>> while number>=1 :
	number=number-1
	if number==5:
		continue
	print number

	
10
9
8
7
6
4
3
2
1
0
>>> 
