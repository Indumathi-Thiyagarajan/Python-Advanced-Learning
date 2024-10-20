import csv
from collections import namedtuple
import pandas as pd

class CSV_Reader:
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
    
    def csv_reader(self):
        self._file = open(self._fname, 'r', encoding='ISO-8859-1')
        self._reader = csv.reader(self._file)
        self._header = next(self._reader)  # Extract the header row
        self._header = self.header_cleaner(self._header)  # Clean the header row
        self.Car_details_named_tuple = self.named_tuple()  # Create named tuple
        return self
    
    def __iter__(self):
        return self

    def __next__(self):
        if self._reader is None: # checks if csv reader has been read or not
            self.csv_reader() #is a CSV reader object that iterates over the rows of the file.
        try:
            current_row = next(self._reader)
            cleaned_row = tuple(self.column_datatype_cleaning(current_row))
            return self.Car_details_named_tuple(*cleaned_row)  # Return a named tuple
        except StopIteration:
            self._file.close()  # Close the file when done
            raise StopIteration

# Example usage
file_path = r'/Users/indu/EPAi/generator_Assignment/nyc_parking_tickets_extract-1.csv'
csv_data = CSV_Reader(file_path)

for car_details in csv_data:
    print(car_details)


# to calculate vioolations made by car make with generator

# default dict is used to avoid key error while initializing, errors out whne key is empty

from collections import defaultdict
def violation_made_by_make(file_path):
    csv_reader = CSV_Reader(file_path)
    violation_made = defaultdict(int)

    for car_row in csv_reader:
        violation_made[car_row.Vehicle_Make] += 1
        yield car_row.Vehicle_Make, violation_made[car_row.Vehicle_Make]

file_path = r'/Users/indu/EPAi/generator_Assignment/nyc_parking_tickets_extract-1.csv'

for make, count in violation_made_by_make(file_path):
    print(f"{make}: {count} violations")


# to calculate same without using default dict and non generator

from collections import defaultdict
def violation_made_by_make(file_path):
    csv_reader = CSV_Reader(file_path)
    violation_made = defaultdict(int)

    for car_row in csv_reader:
        violation_made[car_row.Vehicle_Make] += 1
    return violation_made    
file_path = r'/Users/indu/EPAi/generator_Assignment/nyc_parking_tickets_extract-1.csv'
violation = violation_made_by_make(file_path)

print(violation)
