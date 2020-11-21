# author: Aditya
# date: 2020-11-21

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [<arga>] [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[<arga>]          Takes any value (this is a optional positional)
[--arg3=<arg3>]   Takes any value (this is an optional option)
"""

from docopt import docopt
opt = docopt(__doc__)
print(opt)
print(type(opt))

def main():
    print("Red")
    print("Green")
    print("Blue")

if __name__ == "__main__":
    main()
