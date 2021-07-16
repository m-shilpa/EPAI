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
    "Polygon Sequence",
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
