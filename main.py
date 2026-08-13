# Imports util.py from the same project (needs Termux to run multi-file)
from util import greet

def main():
    name = input("Enter your name: ")
    print(greet(name))

if __name__ == "__main__":
    main()
