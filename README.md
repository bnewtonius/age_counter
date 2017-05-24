# Simple Age Occurrence Counter

This is a very simple and quick age occurrence counter. It takes a csv file containing:

`userid,age`

And outputs:

`age,occurrence`

There are currently two versions, one using awk and another using python.

# Awk example

To run this call ageCount with the csv file as the first argument. For example:

```
./ageCount test/MOCK_DATA.csv
```

# Python example

To run the python example, use the .py version:

```
./ageCount.py test/MOCK_DATA.csv
```
