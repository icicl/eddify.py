### fix issues:
##### when passing named arguments to a function don't rename (ex. `sorted(q, key=func)` don't replace `key`). When fixing check whether or not this should be done to functions declared locally (pretty sure replace arg. keywords with renamed equivalent for functions declared with the file.)
##### split comma separated import statements (ex. `from random import randrange, random` should become `from random import randrange as _` + `from random import random as __`).
