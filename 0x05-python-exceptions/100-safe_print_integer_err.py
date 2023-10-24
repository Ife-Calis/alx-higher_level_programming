#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Ifechukwu Anyika <calistusifechukwu39@gmail.com>

import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
