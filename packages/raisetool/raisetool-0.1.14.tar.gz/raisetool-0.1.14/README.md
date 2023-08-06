# RaiseTool

The project contains small class for formatting thrown exception messages.

The message can be formatted with information about the class, method, and line number where the exception was thrown.

## Usage examples

```
import inspect
from raisetool.formatter import Raise

class Example:

    def __init__(self):
        print("1: " + Raise.message("example message 1"))
        print("2: " + Raise.message("example message 2", self.__class__.__name__))
        print("3: " + Raise.message("example message 3", self.__class__.__name__, inspect.currentframe()))

obj = Example()
```
Output:
```
1: example message 1
2: Example: example messace 2
3: Example.__init__ [line:9]: example message 3
```
