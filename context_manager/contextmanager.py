import csv
from collections import namedtuple

# contextmanager in class setup
import csv
from collections import namedtuple
import pandas as pd

class CSV_Reader_contextmanager:
    def __init__(self, fname):
        self._fname = fname
        self._file = None
        self._reader = None
        self._header = None

    def header_cleaner(self, header):
        return [item.replace(" ", "_") for item in header]
    
    def named_tuple(self):
        Car_Details = namedtuple('Car_Details', self._header)
        return Car_Details
    
    def column_datatype_cleaning(self, row):
        for column, value in zip(self._header, row):
            if column in ['Summons_Number', 'Violation_Code']:
                yield pd.to_numeric(value, errors='coerce')
            elif column == 'Issue_Date':
                yield pd.to_datetime(value, errors='coerce')
            else:
                yield value
    
    def enter(self):
        self._file = open(self._fname, 'r', encoding='ISO-8859-1')
        self._reader = csv.reader(self._file)
        self._header = next(self._reader)  # Extract the header row
        self._header = self.header_cleaner(self._header)  # Clean the header row
        self.Car_details_named_tuple = self.named_tuple()  # Create named tuple
        return self
    
    def __iter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._reader is not None:  # Checks if csv reader has been read or not
            self._file.close()  # Close the file when done

    def __next__(self):
        if self._reader is None: # checks if csv reader has been read or not
            self.enter() #is a CSV reader object that iterates over the rows of the file.
        try:
            current_row = next(self._reader)
            cleaned_row = tuple(self.column_datatype_cleaning(current_row))
            return self.Car_details_named_tuple(*cleaned_row)  # Return a named tuple
        except StopIteration:
            self._file.close()  # Close the file when done
            raise StopIteration

# Example usage
file_path = r'/Users/indu/EPAi/generator_Assignment/nyc_parking_tickets_extract-1.csv'
csv_data = CSV_Reader_contextmanager(file_path)

for car_details in csv_data:
    print(car_details)



# context manager as decorator

        """1. removed enter and added @content manegr on original code. open file in try and close it in finally
        2. used with statement to ensure proper context management. """

import csv
from collections import namedtuple
from contextlib import contextmanager

import csv
from collections import namedtuple
from contextlib import contextmanager
import pandas as pd

class CSV_Reader_contextmanager:
    def __init__(self, fname):
        self._fname = fname
        self._file = None
        self._reader = None
        self._header = None

    def header_cleaner(self, header):
        return [item.replace(" ", "_") for item in header]

    def named_tuple(self):
        Car_Details = namedtuple('Car_Details', self._header)
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
        if self._reader is None:
            raise StopIteration  # Ensure reader is initialized in the context manager
        try:
            current_row = next(self._reader)
            cleaned_row = tuple(self.column_datatype_cleaning(current_row))
            return self.Car_details_named_tuple(*cleaned_row)  # Return a named tuple
        except StopIteration:
            raise StopIteration

# Example usage
file_path = r'/Users/indu/EPAi/generator_Assignment/nyc_parking_tickets_extract-1.csv'

with CSV_Reader_contextmanager(file_path).csv_reader() as csv_data:
    for car_details in csv_data:
        print(car_details)

