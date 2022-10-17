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
