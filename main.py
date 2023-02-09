import numpy as np
import matplotlib.pyplot as plt
import os
import lib.plotter as plot
import sys

if "-i" in sys.argv:
    input_index = sys.argv.index("-i") +1
    filein = str(sys.argv[input_index])
else:
    print("No Input File Denoted.")
    print("Please use -i <filename> to denote an input file")

if "--delimiter" in sys.argv:
    delim_index = sys.argv.index("--delimiter") +1
    delim = str(sys.argv[delim_index])
else:
    delim = None

if "-o" in sys.argv:
    output_index = sys.argv.index("-o") +1
    output_file = str(sys.argv[output_index])
else:
    print("No Output File Denoted")
    print("Please use -o <filename> to denote an output file")

if "--title" in sys.argv:
    title_index = sys.argv.index("--title") +1
    graph_title = str(sys.argv[title_index])
else:
    graph_title = None

if "--pwd" in sys.argv:
    directory_index = sys.argv.index("--pwd") +1
    working_directory = str(sys.argv[directory_index])
else:
    working_directory = os.path.abspath('')

if "--xscale" in sys.argv:
    xscale_index = sys.argv.index("--xscale") +1
    xscale = float(sys.argv[xscale_index])
else:
    xscale = 1

if "--yscale" in sys.argv:
    yscale_index = sys.argv.index("--yscale") +1
    yscale = float(sys.argv[yscale_index])
else:
    yscale = 1

if "--xlabel" in sys.argv:
    xlabel_index = sys.argv.index("--xlabel") +1
    xlabel = str(sys.argv[xlabel_index])
else:
    xlabel = None

if "--ylabel" in sys.argv:
    ylabel_index = sys.argv.index("--ylabel")
    ylabel = str(sys.argv[ylabel_index])
else:
    ylabel = None

if "--xrange" in sys.argv:
    xrange_index = sys.argv.index("--xrange") +1
    xrange_str = str(sys.argv[xrange_index])
    if "," in xrange_str:
        xrange_list = list(xrange_str.split(","))
        for xindx, xrg in enumerate(xrange_list):
            xrg = float(xrg)
            xrange_list[xindx] = xrg
    else:
        print("Range Formated Incorrectly")
        print("Please be sure to follow the proper format of <min>,<max>")    
else:
    xrange_list = None

if "-yrange" in sys.argv:
    yrange_index = sys.argv.index("--yrange") +1
    yrange_str = str(sys.argv[yrange_index])
    if "," in yrange_str:
        yrange_list  = list(yrange_str.split(','))
        for yindx, yrg in enumerate(yrange_list):
            yrg = float(yrg)
            yrange_list[yindx] = yrg
    else:
        print("Range Formated Incorrectly")
        print("Please be sure to follow the proper format of <min>,<max>")
else:
    yrange_list = None

if "--xticks" in sys.argv:
    if xrange_list is not None:
        xtick_index = sys.argv.index("--xticks") +1
        xtick = float(sys.argv[xtick_index])
        xticks = np.arange(xrange_list[0],xrange_list[1],xtick)
    else:
        print("You Must Specify the Axes Range")
        print("Please be sure to follow the proper format of <min>,<max>")
else:
    xticks = None

