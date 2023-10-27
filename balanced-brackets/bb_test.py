import pytest
from bb import isBalanced

def test_bb():

  inputs = []
  outputs = []

  with open('input.txt') as fp:
    inputs = [line.rstrip() for line in fp]
  
  with open("output.txt") as op:
    outputs = [line.rstrip() for line in op]
    
  for i in range(len(inputs)):
    output = isBalanced(inputs[i])
    assert output == outputs[i]
  
