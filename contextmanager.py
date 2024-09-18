import csv
from collections import namedtuple

# contextmanager in class

class DataIterator:
    def __init__(self, fname): 
        self._fname = fname
        self._f = None
        self._reader = None
        self._Row = None
    
    @staticmethod
    def sanitize_header(header):
        return header.replace(" ", "_").replace("-", "_")
                
    def __enter__(self):
        self._f = open(self._fname, 'r')
        self._reader = csv.reader(self._f)
        headers = next(self._reader)  # Extract the header row
        # print("headers", headers)
        sanitized_headers = [DataIterator.sanitize_header(header) for header in headers]
        # Create the named tuple class
        self._Row = namedtuple('Row', sanitized_headers)
        # print("Row", self._Row)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        row = next(self._reader)
        return self._Row(*row)
    
with DataIterator('nyc_parking_tickets_extract.csv') as data: 
    for row in data:
        print(row)
        break




# context manager as decorator
import csv
from collections import namedtuple
from contextlib import contextmanager

def sanitize_header(header):
    return header.replace(" ", "_").replace("-", "_")

@contextmanager
def CSVreader(fname):
    file = open(fname, 'r')
    try:
        _reader = csv.reader(file)
        headers = next(_reader)  # Extract the header row
        sanitized_headers = [sanitize_header(header) for header in headers]
        _Row = namedtuple('Row', sanitized_headers)
        yield _reader, _Row
    finally:
        file.close()

with CSVreader('nyc_parking_tickets_extract.csv') as (reader, Row):
    for row in reader:
        print(Row(*row))
