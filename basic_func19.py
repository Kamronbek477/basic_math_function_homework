# Create a function called main.
# Create function arguments a and b.
# Return the absolute value of the difference between a and b.
from operator import sub


def main(a,b):
    return abs(sub(a,b))
print(main(4,9))