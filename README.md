18_price_format
===================

The script format_price.py formats prices to pretty form. It has two interfaces: programming and command line.

How to run
---------- 

**In order to use programming interface**:

Clone this repository. Copy format_price.py to your project.

Import get_formatted_price():

```
from format_price import get_formatted_price
```

**In order to use command line interface:**

Clone this repository. Then go to the repository directory.

Run the script (price_string is required parameter):

```
python3 format_price.py [-h]  price_string
```

Usage
-----

```
~$ python3 format_price.py 1324592.0345
1 324 592.03

~$ python3 format_price.py 1t23.a
Something went wrong! could not convert string to float: '1t23.a'
Exiting...
```

The repository also has tests for function get_formatted_price(). 

To run tests clone this repository. Then go to the repository directory.

Run tests.py:

```
python3 tests.py
```
