import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from irispy.data import sample
from irispy.sji import SJICube

import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np
from astropy.io import fits
from scipy import misc
from matplotlib.cm import get_cmap

mc=SJICube(sample.SJI_CUBE_1330)
cmap = get_cmap('irissji1330')
map = mc.percentile(97)
rgba = cmap(map.data)
rgb_img = rgba[:,:,0:3]
pil_img = Image(misc.toimage(rgb_img))


class FullImage(Image):
    pass

helloKivy = FullImage()

helloKivy.run()