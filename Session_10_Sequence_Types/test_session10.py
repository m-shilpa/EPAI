import polygon
import polygon_sequence
from polygon import *
from polygon_sequence import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import re

README_CONTENT_CHECK_FOR = [
    "Polygon_sequence",
    "Polygon",
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(polygon_sequence)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session9, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_polygon_incorrect_params():
    assert any(['Error' in Polygon(0,0)])

def test_polygon_incorrect_param_types():
    output = Polygon(0,"0")
    assert any(['Error' in output])
    
def test_Polygon_sequence_incorrect_param_types():
    output = Polygon_sequence('10',15)
    assert any(['Error' in output])

def test_Polygon_sequence_incorrect_param_types1():
    poly = Polygon_sequence(10,15)
    output = poly['1']
    assert any(['Error' in output])

def test_Polygon_sequence_incorrect_params():
    output = Polygon_sequence(10,0)
    assert any(['Error' in output])
