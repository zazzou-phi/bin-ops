#!/usr/bin/python

# Test to see if n-th bit is set
def test_set(x, n):
    return (x & (1<<n))

# Set n-th bit
def set_bit(x, n):
    return (x | (1<<n))

# Clear n-th bit
def clear_bit(x, n):
    return (x & ~(1<<n))

# Toggle n-th bit
def toggle_bit(x, n):
    return (x ^ (1<<n))

# Clear rightmost set bit
def clear_right_bit(x):
    return (x & (x-1))

# Isolate rightmost set bit
def isolate_set(x):
    return (x & (-x))

# Isolate rightmost cleared bit
def isolate_cleared(x):
    return (~x & (x+1))

# Set rightmost cleared bit
def set_cleared(x):
    return (x | (x+1))


