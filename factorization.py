#!/usr/bin/python3
""""Factorization"""
import math


def factorize_number(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors


def factorize_file(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            number = int(line.strip())
            factors = factorize_number(number)
            f_out.write(f"{number}={'*'.join(map(str, factors))}\n")


if __name__ == '__main__':
    input_file = "input.txt"
    output_file = "output.txt"
    factorize_file(input_file, output_file)
