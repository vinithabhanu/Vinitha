Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'22'>'2'
True
ord('2')
50
ord('22')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ord('22')
TypeError: ord() expected a character, but string of length 2 found
ord('hai')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ord('hai')
TypeError: ord() expected a character, but string of length 3 found
'hai'>'hello'
False
ord(h)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ord(h)
NameError: name 'h' is not defined
ord('h')
104
ord('e')
101
ord('i')
105
ord('l')
108
ord('8')
56
ord('9')
57
ord('H')
72
ord('a')
97
ord('j')
106
ord('@')
64
ord('67')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    ord('67')
TypeError: ord() expected a character, but string of length 2 found
[1,2,4,]
[1, 2, 4]
[1,2,4,]>[1,2,3,4]
True
[1,2,3]>[4]
False
(1,2,3)>[-1]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    (1,2,3)>[-1]
TypeError: '>' not supported between instances of 'tuple' and 'list'
{1,2,3,4,5,6}>{6,5,4,3}
True
[1,2,3,'a']>[1,2,3,1]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    [1,2,3,'a']>[1,2,3,1]
TypeError: '>' not supported between instances of 'str' and 'int'
bin(6)
'0b110'
bin(10)
'0b1010'
bin(24)
'0b11000'
bin(36)
'0b100100'
24&36
0
24\36
SyntaxError: unexpected character after line continuation character
4|6
6
12|11
15
~~12
12
~12
-13
~-12
11
8^9
1
18^23
5
bin(-12)
'-0b1100'
-12^2
-10
bin(-2)
'-0b10'
10<<2
40
-8<<2
-32
>>> 6<<3
48
>>> 10>>18
0
>>> 18>>10
0
>>> 6>>4
0
>>> 10>>2
2
>>> 34>>3
4
>>> 'hello'
'hello'
>>> 'e' in 'hello'
True
>>> 'E' in 'hello'
False
>>> 3 in 343
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    3 in 343
TypeError: argument of type 'int' is not iterable
>>>  4 in {1:,2:4
...        
SyntaxError: unexpected indent
>>> 

>>> 

>>> 

... 
>>> 
>>> 
>>> 
>>> 4 in {1:2,2:4}
...        
False
>>> 
>>> 
>>> 
>>> 2 not in(1,2,3,4)
...        
False
