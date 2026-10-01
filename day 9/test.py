def test_function(number_type):
    value = number_type("5")
    print(value)
    print(type(value))

test_function(int)
test_function(float)