Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets
a={2,3.4,"tulasi",True,False,5+6j}
a
{False, True, 'tulasi', 3.4, 2, (5+6j)}
#add
a={2,3,4,5,6,7}
a.add(8)
a
{2, 3, 4, 5, 6, 7, 8}
#subset
a={2,3,4,5,6,7,8,9}
b={2,3,4}
b.issubset(a)
True
#superset()
a.issuperset(b)
True
b.issuperset(a)
False
#duplicate
a={3,4,5,6,7,4}
a
{3, 4, 5, 6, 7}
#union()
a={2,3,4,5,6,7,8,9}
b={4,5,6,7,8}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 9}
b.union(a)
{2, 3, 4, 5, 6, 7, 8, 9}
#intersection()
a={2,3,4,5,6,7,8,9}
b={4,5,6,7,8}
a.intersection(b)
SyntaxError: multiple statements found while compiling a single statement
a.intersection(b)a.intersection(b)
SyntaxError: invalid syntax
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax
a={2,3,4,5,6}
b={3,4,5,6,7}
a.intersection(b)
{3, 4, 5, 6}
b.intersection(a)
{3, 4, 5, 6}
a
{2, 3, 4, 5, 6}
#update()
a={2,3,4,5,6}
b={4,5,6,7,8}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8}
#difference()
a={2,3,4,5,6}
b={7,8,9,10,11}
a.difference(b)
{2, 3, 4, 5, 6}
a={2,3,4,5,6,7,8}
b={4,5,6,7,8,9,10}
a.difference(b)
{2, 3}
b.difference(a)
{9, 10}
a.difference(a)
set()
#symmetric()
a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10}
a.symmetric_difference(b)
{2, 3, 4, 10}
b.symmetric_difference(a)
{2, 3, 4, 10}
a={3,4,5,6,7,8,9,10}
b={5,6,7,8,9,10,11}
a.intersection_update(b)
a
{5, 6, 7, 8, 9, 10}
b
{5, 6, 7, 8, 9, 10, 11}
b.intersection_update(a)
b
{5, 6, 7, 8, 9, 10}
#copy()
a={1,2,3,4}
a.copy()
{1, 2, 3, 4}
a.clear()
a
set()
a.add(5)
a
{5}
a={1,2,3,4}
a.pop()
1
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(4)
a
{2, 3}
#discard()
a={1,2,3,4}
a.discard(1)
a
{2, 3, 4}
a={1,2,3,4,5}
b={6,7,8,9,10}
a.isdisjoint(b)
True
a={1,2,3,4}
b={2,3,4,5}
a.isdisjoint(b)
False
len(a)
4
a={3,4,5,6}
b={7,8,9,10,11}
a.update(b)
a
{3, 4, 5, 6, 7, 8, 9, 10, 11}
b
{7, 8, 9, 10, 11}
#list task
a=[9,1,5,2,8,4,6,3,7,0]
a1=a[0:5]
a1
[9, 1, 5, 2, 8]
a2=a[5:10]
a2
[4, 6, 3, 7, 0]
a1.sort()
a1
[1, 2, 5, 8, 9]
a1.reverse()
a1
[9, 8, 5, 2, 1]
a2.sort()
a2
[0, 3, 4, 6, 7]
a2.reverse()
a2
[7, 6, 4, 3, 0]
c=a1+a2
c
[9, 8, 5, 2, 1, 7, 6, 4, 3, 0]
d=a2+a1
d
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
#dictionary
a={"name":"tulasi","year":2026,"month":"may"}
type(a)
<class 'dict'>
a
{'name': 'tulasi', 'year': 2026, 'month': 'may'}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['tulasi', 2026, 'may'])
a.items()
dict_items([('name', 'tulasi'), ('year', 2026), ('month', 'may')])
a{"name"}
SyntaxError: invalid syntax
a.update({"year":2026})
a
{'name': 'tulasi', 'year': 2026, 'month': 'may'}
#set default()
a={"city":"vij"}
a.setdefault("name":"tulasi")
SyntaxError: invalid syntax
a.setdefault("name","tulasi")
'tulasi'
a
{'city': 'vij', 'name': 'tulasi'}
a={"name":"tulasi","branch":"bsc"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("branch")
'bsc'
a
{'name': 'tulasi'}
a.popitems()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.popitems()
AttributeError: 'dict' object has no attribute 'popitems'. Did you mean: 'popitem'?
a={"name":"tulasi","branch":"bsc"}
a.popitem()
('branch', 'bsc')
a
{'name': 'tulasi'}
#copy()
a={"city":"vij","state":"ap"}
a.copy()
{'city': 'vij', 'state': 'ap'}
#get()
a.get()
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    a.get()
TypeError: get expected at least 1 argument, got 0
a.get("city")
'vij'
a
{'city': 'vij', 'state': 'ap'}
>>> #clear()
>>> a.clear()
>>> a
{}
>>> b={]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> b={}
>>> b.update({"name":"tulasi"})
>>> b
{'name': 'tulasi'}
>>> a={"idos":[10,20,30],"names":["ganesh","suresh","mahesh"],"marks":[60,70,80]}
>>> print(a)
{'idos': [10, 20, 30], 'names': ['ganesh', 'suresh', 'mahesh'], 'marks': [60, 70, 80]}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['ganesh', 'suresh', 'mahesh'], [60, 70, 80]])
>>> a.items()
dict_items([('idos', [10, 20, 30]), ('names', ['ganesh', 'suresh', 'mahesh']), ('marks', [60, 70, 80])])
>>> #duplicate values does't allowed
>>> a={"name":"tulasi","year":2026,"name":"raji"}
>>> print(a)
{'name': 'raji', 'year': 2026}
>>> a={"name":"tulasi","year":2026,"name1":"raji"}
>>> print(a)
{'name': 'tulasi', 'year': 2026, 'name1': 'raji'}
>>> a={"name":"tulasi","mailid":"tulasi@gmail.com"}
>>> a.popitem("maild")
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    a.popitem("maild")
TypeError: dict.popitem() takes no arguments (1 given)
>>> a.popitem()
('mailid', 'tulasi@gmail.com')
