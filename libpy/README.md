# MySQL Basic usage

```python
from libpy.mysql import MySQL

db = MySQL('dbname', 'dbuser', 'dbpass', show_warnings=True)
# Insert raw strings
# Using tuple is safe though not all cases tuple is applicable so you have to use MySQL.escape instead.
db.query('INSERT INTO users (name, surname) VALUES {}'.format(('Mark', 'Sagal')))

# Escaping raw values
name = db.escape('Mark')
surname = db.escape('Sagal')
db.query('INSERT INTO users (name, surname) VALUES ({}, {})'.format(name, surname))

# Rollback changes
db.rollback()

# Fetching data
datas = db.query('SELECT id, name, surname FROM users')
for data in datas:
    id, name, surname = data
    print('Id: %d' % id)
    print('Name: %s' % name)
    print('Surname: %s' % surname)

db.close()
```


# MySQL Usage with with

```python
from libpy.mysql import MySQL

with MySQL('dbname', 'dbuser', 'dbpass', show_warnings=True) as db:
    # Insert raw strings
    # Using tuple is safe though not all cases tuple is applicable so you have to use MySQL.escape instead.
    db.query('INSERT INTO users (name, surname) VALUES {}' . format(('Mark', 'Sagal')))

    # Escaping raw values
    name = db.escape('Mark')
    surname = db.escape('Sagal')
    db.query('INSERT INTO users (name, surname) VALUES ({}, {})' . format(name, surname))

    # Rollback changes
    db.rollback()

    # Fetching data
    datas = db.query('SELECT id, name, surname FROM users')
    for data in datas:
        id, name, surname = data
        print('Id: %d' % id)
        print('Name: %s' % name)
        print('Surname: %s' % surname)
```
