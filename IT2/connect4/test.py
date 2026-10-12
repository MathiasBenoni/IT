import pytest
from my_functions import *

def test_create_board():
  assert create_board(7, 6) == 