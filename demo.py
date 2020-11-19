# author: Aditya
# date: 2020-11-19

"This script prints out docopt args.
Usage: demo.R <arg1> [<arg4>] --arg2=<arg2> [--arg3=<arg3>]
Options:
<arg>             Takes any value (this is a required positional argument)
[<arg4>]          Takes any value (this is an optional positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
" -> doc

library(docopt)
opt <- docopt(doc)
print(opt)
print(typeof(opt))
