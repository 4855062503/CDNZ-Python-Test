# CDNZ Python Test - Alex

## 1:

The output will read:

```py
Look!\nTest string 1
```

## 2:

A tuple of dictionaries keying a list of strings

## 3:

If the list needs to be mutable, i.e. you'd want to update it, it should be a list, else, if it can be immutable you could use a tuple

## 4:

There is incorrect indentation, so the output will be an error:

```sh
  File "test.py", line 2
    for d in data:
    ^
IndentationError: unexpected indent
```

This is because there should be no indent at `for` (line 2) and where `else` is (line 6)

## 5:
A)
```py
from dir2.foo import foo_class
```
B)

```py
import sys 
sys.path.append('..')
from bar import bar_class
```

## 6:

You may want to use the `ABC` module in Python if you have indentified an instance where an abstract class could be used. Such an example could be when you know several classes share properties, but have functions which should return different data.

## 7:

If you pass immutable objects, i.e. ints, tuples, strings, they are passed by value, the rest is passed by reference

The gotcha is that sometimes you may want a call-by-value instead of call-by-reference, e.g. setting a variable as a list, which the list is later updated, making the variable output not what we want. In this situation, you may want to call the [copy](https://docs.python.org/3/library/copy.html) function to pass the list by value when setting the variable. I have had to use this function before at work when dealing with printing a forever changing list.

An advantage is that call-by-reference allows variables to all update an immutable data object which is referenced.
