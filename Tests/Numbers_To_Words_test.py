import pytest
from Intermediate import Numbers_To_Words

def test_num_split():
    assert Numbers_To_Words.num_split(123456) == [123,456]

def test_block_to_sting():
    assert Numbers_To_Words.block_to_sting(123) == "one hundred and twenty three"
