from strcalc import add

assert add("") == 0
assert add("1") == 1
assert add("1,2") == 3
assert add("1\n2,3") == 6
assert add("//;\n1;2") == 3
assert add("//***\n1***2***3") == 6
assert add("//[*][%]\n1*2%3") == 6
assert add("//[***][%%%]\n1***2%%%3") == 6

try:
    add("-1,2,-3")
except Exception as e:
    assert str(e) == "negatives not allowed: -1,-3"
