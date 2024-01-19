Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=56
type(a)
<class 'int'>
b=0
type(b)
<class 'int'>
c=-78
type(c)
<class 'int'>
d=int()
d
0
bool(0)
False
bool(-9)
True
a=2.3
type(a)
<class 'float'>
b=-7.8
type(b)
<class 'float'>
c=0.24
type(c)
<class 'float'>
d=0.0
type(d)
<class 'float'>
bool(d)
False
bool(a)
True
a=2+3j
type(a)
<class 'complex'>
b=4+6J
type(b)
<class 'complex'>
c=2+4i
SyntaxError: invalid decimal literal
print(c)
0.24
c=2+j5
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    c=2+j5
NameError: name 'j5' is not defined
c=2+j5
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    c=2+j5
NameError: name 'j5' is not defined
c
0.24
typecal
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    typecal
NameError: name 'typecal' is not defined
a=bool()
a
False
a='fghjkiu'
a
'fghjkiu'
b="fghjkiu"
b
'fghjkiu'
d="'fghjk"'
SyntaxError: unterminated string literal (detected at line 1)
print(d)
0.0
a=12
b=30
print(a,b)
12 30
b=str()
b
''
bool(b)
False
a=['a','str','eifi']
a
['a', 'str', 'eifi']
c=[1,2,'sn',[1,2]]
c
[1, 2, 'sn', [1, 2]]
c=list[]
SyntaxError: invalid syntax
c
[1, 2, 'sn', [1, 2]]
a=(1,2,3,4)
type(a)
<class 'tuple'>
b=4,5,8,9
type(b)
<class 'tuple'>
r=tuple()
r
()
bppl(r)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    bppl(r)
NameError: name 'bppl' is not defined
bool(r)
False
d={1,2,'a',(4,5),-9}
d
{1, 2, (4, 5), 'a', -9}
type(d)
<class 'set'>
r={1,2,3,4,2,6,-2}
type(r)
<class 'set'>
w=[1,2,1,2,4]
w
[1, 2, 1, 2, 4]
t={'a','b',1,true,'a','abc'}
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t={'a','b',1,true,'a','abc'}
NameError: name 'true' is not defined. Did you mean: 'True'?
t
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    t
NameError: name 't' is not defined
type(t)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    type(t)
NameError: name 't' is not defined
