
import csv
from collections import namedtuple
from contextlib import contextmanager
import pandas as pd

class CSV_Reader_contextmanager:
    def __init__(self, fname,named_tuple_name):
        self._fname = fname
        self._file = None
        self._reader = None
        self._header = None
        self.named_tuple_name = named_tuple_name

    def header_cleaner(self, header):
        return [item.replace(" ", "_") for item in header]

    def named_tuple(self):
        Car_Details = namedtuple(self.named_tuple_name, self._header)
        return Car_Details
    
    def column_datatype_cleaning(self, row):
        for column, value in zip(self._header, row):
            if column in ['Summons_Number', 'Violation_Code']:
                yield pd.to_numeric(value, errors='coerce')
            elif column == 'Issue_Date':
                yield pd.to_datetime(value, errors='coerce')
            else:
                yield value

    @contextmanager
    def csv_reader(self):
        try:
            self._file = open(self._fname, 'r', encoding='ISO-8859-1')
            self._reader = csv.reader(self._file)
            self._header = next(self._reader)  # Extract the header row
            self._header = self.header_cleaner(self._header)  # Clean the header row
            self.Car_details_named_tuple = self.named_tuple()  # Create named tuple
            yield self
        finally:
            if self._file:
                self._file.close()
    
    def __iter__(self):
        return self

    def __next__(self):
        """self.csv_reader() initializes the reader if it hasn't been done yet. This way, the CSV reader is set up only when it’s needed, avoiding unnecessary initialization
            With Context Manager:
            When using a context manager, the file handling and initialization are managed by the context manager itself. 
            By the time you call __next__, the reader should have already been initialized within the context of the with statement. 
            Hence, if self._reader is None, it indicates an error or that you're outside the context manager’s scope, so you raise StopIteration immediately:"""
        
        if self._reader is None:
            raise StopIteration  # Ensure reader is initialized in the context manager 
            # When not using context manager, here instead of raise stopiteration it will be self.csv_reader() being called. explained above
        try:
            current_row = next(self._reader)
            cleaned_row = tuple(self.column_datatype_cleaning(current_row))
            return self.Car_details_named_tuple(*cleaned_row)  # Return a named tuple
        except StopIteration:
            raise StopIteration

# Example usage
file_path = r'/Users/indu/EPAi/assignments/context_manager_assignment/personal_info.csv'

with CSV_Reader_contextmanager(file_path, 'Personal_Details').csv_reader() as csv_data:
    for row in csv_data:
        print(row)
