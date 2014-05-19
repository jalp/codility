def string_reverse(input):
# String in Python are immutable, so to reverse it, a new one is created. You can not modify the original one
# There are three solutions:
# 1) Using slicing
# return input[::-1]
# 2) Using built-in reversed
# return "".join(reversed(input))
# 3) Using a generator
    return "".join(input[i] for i in range(len(input) - 1, -1, -1))

print string_reverse("This is amazing")
