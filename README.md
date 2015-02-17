# Dict.py 
#####A python module for easy manipulation of a dictionary
<br />
## Getting started
***
To start import the module into a python script `from dict import *`.

Then initiate a new dictionary `x = dictionary()`

You can then use these methods to manipulate the dictionary: 

| Option | Description |
| ------ | ----------- |
| append()  | Adds a new key if there is no other key of the same name that exists, otherwise it will update the key that already exists.|
| remove() | Removes the selected key from the dictionary.|
| get() | Retrieves the dictionary and prints it to console. |
| test() | Starts a unit test for all of the methods. |

## Examples
***

### append()
```python
 x = dictionary()
 x.append("example", "abcd")
 # Result: {"example", "abcd"}
```

### remove()
```python
 x = dictionary()
 x.append("example", "abcd")
    # Result: {"example", "abcd"}
 x.remove("example")
    # Result: {}
```
### get()
```python
 x = dictionary()
 x.append("example", "abcd")
 x.get()
 # Result to console: {"example", "abcd"}
```

### test()
```python
 x = dictionary()
 x.test()
 """ 
    Result: 
        Append test passed!
        Remove test passed!
        Get test passed!
        3 tests passed, 0 tests failed
 """" 
```











