import matplotlib.pyplot as plt
import numpy as np
import os
import math


class Lineplot:

    def grapher(datafile,outputfile,delimiter=None,title="",xlabel="",ylabel="",label=None,xscale=1,yscale=1,xrange=None,yrange=None,xticks=None,yticks=None,grid=None,linewidth=None,color=None):

        data_file = open(datafile, "r")
        if delimiter is not None:
            delim_str = delimiter
        else:
            delim_str = " "
        
        datalist = []
        filelist = []

        for line in data_file:
            if delim_str in line:
                datalist.append(line)
            filelist.append(line)
        
        if datalist == filelist:

            data_array = np.genfromtxt(datafile,dtype=float,delimiter=delimiter)
            
            xdata = data_array[:,0]

            xlist = []
            for x in xdata:
                if type(xscale) == float or type(xscale) == int:
                    x = x*xscale
                elif type(xscale) == list:
                    if "log" in xscale:
                        base = xscale[1]
                        x = math.log(x,base)

                xlist.append(x)

                ydata = np.delete(data_array,0,1)
                ydatadim = ydata.ndim
                fig,ax = plt.subplots(1,1)

            for col in range(len(ydata[0,:])):
                if ydatadim != 1:
                    ycol = ydata[:,col]
                else:
                    ycol = ydata

                ylist = []

                for y in ycol:
                    y = y*yscale
                    ylist.append(y)
                if label is not None:
                    if len(label) == len(ydata[0,:]):
                        label_current = label[col]
                    elif len(label) > len(ydata[0,:]):
                        print("WARNNING: Number of labels xcedes the number of datasets")
                        label_current = label[col]
                    else:
                        print("ERROR: Number of labels is less than the number of datasets")
                        label_current = None     
                else:
                    label_current = None
                
                if color is not None:
                    if len(color) == len(ydata[0,:]):
                        color_current = color[col]
                    elif len(color) > len(ydata[0,:]):
                        print("WARNING: Number of specified colors excedes the number of datasets")
                        color_current = color[col]
                    else:
                        print("ERROR: Number of specified colors is less than the number of datasets")
                        color_current = None
                else:
                    color_current = None

                ax.plot(xlist,ylist,label=label_current,linewidth=linewidth,color=color_current)

            ax.set_ylabel(ylabel)
            ax.set_xlabel(xlabel)
            if xrange is not None:
                if type(xrange) == type([]) or type(xrange) == type(np.array([0,0])):
                    ax.set_xlim(xrange[0],xrange[1])
                else:
                    print("Invalid Type for X Range")
                    print("X Range Must be list or array")

            if yrange is not None:
                if type(yrange) == type([]) or type(yrange) == type(np.array[0,0]):
                    ax.set_ylim(yrange[0],yrange[1])
                else:
                    print("Invalid Type for Y Range")
                    print("Y Range Must be list or array")

            if xticks is not None:
                if type(xticks) == type(np.array[0,0]):
                    ax.set_xticks(xticks)
                else:
                    print("Invalid Type for X Ticks")
                    print("X Ticks Must be an array")
            
            if yticks is not None:
                if type(yticks) == type(np.array([0,0])):
                    ax.set_yticks(yticks)
                else:
                    print("Invalid Type for Y Ticks")
                    print("Y Ticks Must be an array")

            if grid is not None:
                if grid == "h":
                    ax.grid(axis="y")
                elif grid == "v":
                    ax.grid(axis="x")
                elif grid == "hv":
                    ax.grid()
                else:
                    print("Invald option for grid")
                    print("Valid Grid Options: h,v,hv")
            if label is not None:
                ax.legend()
                                
            ax.set_title(title)
            fig.tight_layout(pad=2)
            fig.savefig(os.path.join(outputfile),dpi=1000,bbox_inches="tight")
            plt.clf()
            plt.cla()
        
        else:

            print("ERROR: INVALID DELIMITER")