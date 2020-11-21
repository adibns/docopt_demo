# author: Aditya
# date: 2020-11-21

"This script prints out docopt args.
Usage: demo.R <arg1> --arg2=<arg2> [<arga>] [--arg3=<arg3>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[<arga>]          Takes any value (this is a optional positional argument)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)
opt <- docopt(doc)
print(opt)
print(typeof(opt))
print(opt[4])
