#!/usr/bin/python3
if __name__ == "__main__":
    import sys

list_of_args = sys.argv[1:]

int_args = [int(arg) for arg in list_of_args]

sum_of_args = 0
for num in int_args:
    sum_of_args += num

print("{}".format(sum_of_args))
