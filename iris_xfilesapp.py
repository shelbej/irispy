from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os
import datetime
from irispy.sji import SJICube



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
        try:
            self.label.text = args[1][0]
            mc = SJICube(args[1][0])
            mc[0].peek()
        except: pass

class iris_xfilesApp(App):
    def build(self):
        #iris_xfiles.filter(self,datetime.datetime(2017,8,8),datetime.datetime(2017,8,9),3640106077)
        return iris_xfiles()

if __name__ == '__main__':
    iris_xfilesApp().run()