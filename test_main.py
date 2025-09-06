import json
from main import convert_from_format_1, convert_from_format_2

def test_format_1():
    with open("data-1.json") as f:
        d1 = json.load(f)
    result = convert_from_format_1(d1)

    with open("data-result.json") as f:
        expected = json.load(f)
    assert result == expected

def test_format_2():
    with open("data-2.json") as f:
        d2 = json.load(f)
    result = convert_from_format_2(d2)

    with open("data-result.json") as f:
        expected = json.load(f)
    assert result == expected
