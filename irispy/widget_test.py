import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, CheckButtons, Cursor, TextBox

from ipywidgets import widgets, interactive


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)



class Index(object):

    cursor=widgets.BoundedFloatText


    ind = 0
    def set_directory(self,event):
        self.directory = input.value

    def search(self, event):
        # grab all .fits in directory
        import os
        sji_list = []
        for file in os.listdir(self.directory):
            if self.filter in file:
                sji_list.append(os.path.join(self.directory, file))


    def select(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

filter =''
callback = Index()
axdir = plt.axes([0.1, 0.7, 0.5, 0.075])
axfiletype = plt.axes([0.65, 0.7, 0.05, 0.05])
axsearch = plt.axes([0.7, 0.05, 0.1, 0.075])
axselect = plt.axes([0.81, 0.05, 0.1, 0.075])
input_dir = TextBox(axdir,'Search Directory', initial_text='')
bsearch = Button(axsearch, 'Search')
bsearch.on_clicked(callback.search)
bselect = Button(axselect, 'Select')
bselect.on_clicked(callback.select)
input_dir.on_submit(callback.search)
#cursor.on_clicked(callback.cursor)

plt.show()