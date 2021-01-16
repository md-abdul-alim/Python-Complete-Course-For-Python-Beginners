import math_func
import pytest
#pytest test_math_func.py::test_add ##for specific function run
#pytest -v -k "add" ##run those function who have add key word
#pytest -v -k "add or string" ## run those function who have add or string key words
#pytest -v -k "add and string" ## run those function who have add and string key words

def test_add():
	assert math_func.add(7,3) == 10
	assert math_func.add(7) == 9
	assert math_func.add(5) == 7

def test_product():
	assert math_func.product(5,5) == 25
	assert math_func.product(5) == 10
	assert math_func.product(7) == 14

def test_add_strings():
	result = math_func.add('Hello', ' World')
	assert result == 'Hello World'
	assert type(result) is str
	assert 'Heldlo' not in result

def test_product_strings():
	assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
	result = math_func.product('Hello ')
	assert result == 'Hello Hello '
	assert type(result) is str
	assert 'Hello ' in result 
