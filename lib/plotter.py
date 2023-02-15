import matplotlib.pyplot as plt
import numpy as np
import os


class Lineplot:

    def grapher(datafile,outputfile,delimiter=None,title="",xlabel="",ylabel="",label=None,xscale=1,yscale=1,xrange=None,yrange=None,xticks=None,yticks=None,grid=None,linewidth=None):
        data_array = np.genfromtxt(datafile,dtype=float,delimiter=delimiter)
        print(np.shape(data_array))
        xdata = data_array[:,0]

        xlist = []
        for x in xdata:
            x = x*xscale
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
                label_current = label[col]
            else:
                label_current = None

            ax.plot(xlist,ylist,label=label_current,linewidth=linewidth)

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