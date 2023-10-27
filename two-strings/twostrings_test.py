import pytest
from twostrings import twoStrings

def test_twostrings():

  inputs = []
  outputs = []

  with open('input.txt') as fp:
    inputs = [line.rstrip() for line in fp]
  
  with open("output.txt") as op:
    outputs = [line.rstrip() for line in op]
    
  for i in range(0, len(inputs), 2):
    output = twoStrings(inputs[i], inputs[i+1])
    assert output == outputs[int(i/2)]
  
