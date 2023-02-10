import numpy as np
import matplotlib.pyplot as plt
import os
import lib.plotter as plot
import sys

if "--help" not in sys.argv or "-h" not in sys.argv:
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
        output_file_list = list(filein.split("."))
        output_file_head = output_file_list[0]
        output_file = f"{output_file_head}.png"

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
            xticks = np.arange(xrange_list[0],xrange_list[1]+xtick,xtick)
        else:
            print("You Must Specify the Axes Range")
            print("Please be sure to follow the proper format of <min>,<max>")
    else:
        xticks = None

    if "--yticks" in sys.argv:
        if yrange_list is not None:
            ytick_index = sys.argv.index("--yticks") +1
            ytick = float(sys.argv[ytick_index])
            yticks = np.arange(yrange_list[0], yrange_list[1]+ytick, ytick)
        else:
            print("You Must Specify the Axes Range")
            print("Please be sure to follow the proper format of <min>,<max>")
    else:
        yticks = None
    
    if "--graph" in sys.argv:
        graph_index = sys.argv.index("--graph") +1
        graph_type = str(sys.argv[graph_index])
    else:
        print("You Must Specify a graph type")
        print("USe --graph <line>")
    
    if "--grid" in sys.argv:
        grid_index = sys.argv.index("--grid") +1
        grid_option = str(sys.argv[grid_index])
    else:
        grid_option = None

    if graph_type == "line":
        plot.Lineplot.grapher(datafile=os.path.join(working_directory,filein),outputfile=os.path.join(working_directory,output_file),delimiter=delim,title=graph_title,xlabel=xlabel,ylabel=ylabel,xrange=xrange_list,yrange=yrange_list,xticks=xticks,yticks=yticks,xscale=xscale,yscale=yscale,grid=grid_option)

else:
    help_message = """
    About This Program:
    This is a command line based graphing software developed my Eugene Chung in collaboration with Dr. Junyong Choi. This program can be usefull for data analysis of bulk data that needs to be graphed.
    You can use -h or --help to see this page. Below you find some information regarding how to use the program and how to format your data.

    Input and Output:
    -i <input Filename>                             Input file with data to graph (.dat, .csv, etch)
    -o <Output Filename>                            Output file of graph (Default will have the same name as the inputfile) (.png, .jpg)
    --pwd <Working Directory>                       Working Directory location of imput and outfiles (Default is Current Directory)

    Graphing Options:
    --graph <line>                                  Type of graph to be used       
    --title <Graph Title>                           Title for the graph (Default is No Title)
    --xlabel <X Axis Label>                         X axis label for the graph (Default is No Label)
    --ylabel <Y Axis Label>                         Y axis label for the graph (Default is No Label)
    --xrange <xmin,xmax>                            Specify the range of the x axis (Default is automated range selection)
    --yrange <ymin,ymax>                            Specify the range of the y axis (Default is automated range selection)
    --xticks <X Increment>                          Specify the increment of the tickmarks on the x axis (Default is automated increment selection)
    --yticks <Y Increment>                          Specify the increment of the tickmarks on the y axis (Default is automated increment selection)
    --grid <h,v, or hv>                             Add horizontal and or vertical grids to the graph (Default is no grid)

    Data Format Optioms:
    --delimiter <delimiter option>                  Specify delimiter to seperate data enetries in data file (Default is whiteshpace)

    Data Format Example
    This is an example of how you should format your data to graph it.

    X   Y1  Y2  Y3  ... Yn
    x1  y11 y21 y31 ... yn1
    x2  y12 y22 y32 ... yn2
    x3  y13 y23 y33 ... yn3
    .   .   .   .   ... .
    .   .   .   .   ... .
    .   .   .   .   ... .
    xm  y1m y2m y3m ... ynm

    """
    print(help_message)