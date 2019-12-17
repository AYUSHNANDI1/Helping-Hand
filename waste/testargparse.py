import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-v')

args = parser.parse_args()

print(args.v)
