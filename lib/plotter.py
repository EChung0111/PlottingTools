import matplotlib.pyplot as plt
import numpy as np
import os


class Lineplot:

    def grapher(datafile,outputfile,delimiter=None,title="",xlabel="",ylabel="",label="",xscale=1,yscale=1):
        data_array = np.genfromtxt(datafile,dtype=float,delimiter=delimiter)
        xdata = data_array[:,0]

        xlist = []
        for x in xdata:
            x = x*xscale
            xlist.append(x)

            data_array = np.delete(data_array,0,1)
            ydata = data_array
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
                
                ax.plot(xlist,ylist,label=label)
                ax.set_ylabel(ylabel)
                ax.set_xlabel(xlabel)
                ax.legend()
                            
        fig.suptitle(title)
        fig.tight_layout(pad=2)
        fig.savefig(os.path.join(outputfile),dpi=1000,bbox_inches="tight")