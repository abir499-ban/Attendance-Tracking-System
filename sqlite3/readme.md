## sqlite3


This doc explores using the [sqllite3](https://docs.python.org/3/library/sqlite3.html) library in Python.

-------------------
Creating a database sample.db and connecting to it:
```sh
    import sqlite3
    con = sqlite3.connect("sample.db")
```

The returned Connection object con represents the connection to the on-disk database.
In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor:
```sh
    cur = con.cursor()
```

Execcuting  sql commands:

CREATE:
```sh
    cur.execute("CREATE TABLE student(id, name, isCR)")
```
INSERT:
```sh
    cur.execute("""
    INSERT INTO student VALUES
        (1, "Student1", False),
        (2, "Student2", True)
""")
```

QUERY:
```sh
    res = cur.execute("""
                    SELECT name FROM students
    """)
    res.fetchall()
```

MULTIPLE INSERTIONS:
```sh
    data = [
        (1, "Student1", False),
        (2, "Student2", True)
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()   ## required for multiple SQL commands
```

ITERATIN OVER QUERY RESULT(s):
```sh
    for row in cur.execute('SELECT id,name FROM student'):
        print(row)    ## the row is a list of tuples of (id, name)
```

UPDATE:
```sh
    curr.execute("UPDATE student 
                SET name=?, isCR=?
                WHERE id=?", (new_name, new_isCR, id))
    con.commit()
```


DELETE:
```sh
    curr.execute("DELETE FROM student
                WHERE id=?" , (id) )
```


CLOSING THE CONNECTION:
```sh
    con.close()
```
