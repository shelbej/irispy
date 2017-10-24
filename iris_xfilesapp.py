from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.filechooser import FileChooserListView
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.core.window import Window
Config.set("input", "mouse", "mouse, enable_multitouch")

import os
import datetime
import matplotlib.pyplot as plt
from irispy.sji import SJICube
from irispy.spectrograph import IRISSpectrograph



class iris_xfiles(BoxLayout):

    # def filter(self, start_date, end_date, obsid):
    #     search_list = []
    #     delta = end_date - start_date
    #     date = start_date
    #     for d in range(0, delta.days + 1):
    #         print(date)
    #         for root, dir, file in os.walk(self.filechooser.path + date.strftime('%Y/%m/%d')):
    #             if (str(obs) in dir):
    #                 # print(dir)
    #                 for i in file:
    #                     if ('SJI_1330' in i):
    #                         search_list.append(root + '/' + i)
    #
    #         date += datetime.timedelta(days=1)
    #     search_list.sort()
    #     results = '\n'.join(search_list)
    #     try: self.label.text = results
    #     except: pass

    def select(self,*args):
        file = args[1][0]
        try:
            self.label.text = file
            print(file)
        except: pass

        if 'SJI' in file:
            mc = SJICube(file)
            mc.percentile(97).peek()
        elif 'raster' in file:
            nd = IRISSpectrograph(file)
            mg = nd.data['Mg II k 2796']
            mg.index_by_raster[0:,:].plot()
            plt.show()

class iris_xfilesApp(App):
    def build(self):
        #iris_xfiles.filter(self,datetime.datetime(2017,8,8),datetime.datetime(2017,8,9),3640106077)
        return iris_xfiles()


if __name__ == '__main__':
    iris_xfilesApp().run()