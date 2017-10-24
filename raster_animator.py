import matplotlib.colors as colors
import matplotlib.pyplot as plt
from irispy.sji import SJIMap

from sunpy.image.coalignment import calculate_shift

from irispy.spectrograph import IRISSpectrograph

plt.rcParams.update({'figure.dpi': 100,'font.size':10})

#testfile='/Users/shelbe/sunpy/data/sample_data/iris_l2_20170502_095734_3620250135_raster_t000_r00000.fits'
#sg=IRISSpectrograph(testfile)
#sg.spectral_windows
#mg=sg.data['mg ']
#mg.animate(cmap='irissji1330',norm=colors.PowerNorm(.5))
#plt.show()


import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.style as style
import sunpy.cm as cm
import sunpy.instr.iris
import sunpy.map
import numpy as np
import matplotlib.colors as colors
import astropy.units as u
from astropy.visualization.mpl_normalize import ImageNormalize
from astropy import visualization
import sunpy.physics.differential_rotation as diff_rot

from astropy.io import fits
plt.rcParams['animation.ffmpeg_path'] = '/Users/shelbe/anaconda/bin/ffmpeg'
plt.rcParams.update({'font.size': 4})
#style.use( 'dark_background')
writer = animation.FFMpegWriter(fps=30, metadata=dict(artist='SunPy'), bitrate=100000)

iris_dir = '/net/md5/Volumes/kale/iris/data/level2/'
import os
#raster_list=[]
#for file in os.listdir(iris_dir):
#    if file.endswith(".fits"):
#        raster_list.append(os.path.join(iris_dir, file))
# raster_list=[]
# date = datetime.datetime(2017,8,8)
# obs = 3640106077
# for d in range(0,8):
#     print(date)
#     for root,dir,file in os.walk(iris_dir+date.strftime('%Y/%m/%d')):
#         if (str(obs) in dir):
#             for i in file:
#                 if ('raster' in i):
#                     raster_list.append(os.path.join(root,i))
#
#     date += datetime.timedelta(days=1)
# raster_list.sort()
# print('Contains ', len(raster_list), ' files')

raster_list=['/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00005.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00006.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00007.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00008.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_081931_3640106077/iris_l2_20170808_081931_3640106077_raster_t000_r00009.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_125420_3640106077/iris_l2_20170808_125420_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_125420_3640106077/iris_l2_20170808_125420_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00005.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00006.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_135830_3640106077/iris_l2_20170808_135830_3640106077_raster_t000_r00007.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_174429_3640106077/iris_l2_20170808_174429_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_174429_3640106077/iris_l2_20170808_174429_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00005.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00006.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/08/20170808_204031_3640106077/iris_l2_20170808_204031_3640106077_raster_t000_r00007.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_002120_3640106077/iris_l2_20170809_002120_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_002120_3640106077/iris_l2_20170809_002120_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_002120_3640106077/iris_l2_20170809_002120_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_002120_3640106077/iris_l2_20170809_002120_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_021950_3640106077/iris_l2_20170809_021950_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_021950_3640106077/iris_l2_20170809_021950_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_052301_3640106077/iris_l2_20170809_052301_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_052301_3640106077/iris_l2_20170809_052301_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_052301_3640106077/iris_l2_20170809_052301_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_070931_3640106077/iris_l2_20170809_070931_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_070931_3640106077/iris_l2_20170809_070931_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_083911_3640106077/iris_l2_20170809_083911_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_083911_3640106077/iris_l2_20170809_083911_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_133341_3640106077/iris_l2_20170809_133341_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_133341_3640106077/iris_l2_20170809_133341_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_133341_3640106077/iris_l2_20170809_133341_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_133341_3640106077/iris_l2_20170809_133341_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_133341_3640106077/iris_l2_20170809_133341_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_160651_3640106077/iris_l2_20170809_160651_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_160651_3640106077/iris_l2_20170809_160651_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_160651_3640106077/iris_l2_20170809_160651_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_174856_3640106077/iris_l2_20170809_174856_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_174856_3640106077/iris_l2_20170809_174856_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_192731_3640106077/iris_l2_20170809_192731_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_192731_3640106077/iris_l2_20170809_192731_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_210221_3640106077/iris_l2_20170809_210221_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_210221_3640106077/iris_l2_20170809_210221_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_210221_3640106077/iris_l2_20170809_210221_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00005.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00006.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/09/20170809_223731_3640106077/iris_l2_20170809_223731_3640106077_raster_t000_r00007.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_022340_3640106077/iris_l2_20170810_022340_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_022340_3640106077/iris_l2_20170810_022340_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_022340_3640106077/iris_l2_20170810_022340_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_061437_3640106077/iris_l2_20170810_061437_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_061437_3640106077/iris_l2_20170810_061437_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_072731_3640106077/iris_l2_20170810_072731_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_072731_3640106077/iris_l2_20170810_072731_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00005.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_104131_3640106077/iris_l2_20170810_104131_3640106077_raster_t000_r00006.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_135530_3640106077/iris_l2_20170810_135530_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_135530_3640106077/iris_l2_20170810_135530_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_135530_3640106077/iris_l2_20170810_135530_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_135530_3640106077/iris_l2_20170810_135530_3640106077_raster_t000_r00003.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_135530_3640106077/iris_l2_20170810_135530_3640106077_raster_t000_r00004.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_162901_3640106077/iris_l2_20170810_162901_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_162901_3640106077/iris_l2_20170810_162901_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_162901_3640106077/iris_l2_20170810_162901_3640106077_raster_t000_r00002.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_212331_3640106077/iris_l2_20170810_212331_3640106077_raster_t000_r00000.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_212331_3640106077/iris_l2_20170810_212331_3640106077_raster_t000_r00001.fits',
 '/net/md5/Volumes/kale/iris/data/level2/2017/08/10/20170810_212331_3640106077/iris_l2_20170810_212331_3640106077_raster_t000_r00002.fits']

def raster(file_list):
    wave_list0 = []
    wave_list1 = []
    wave_list2 = []
    wave_list3 = []
    wave_list4 = []
    wave_list5 = []
    timestamp_list = []

    xmin_list = []
    xmax_list = []
    ymin_list = []
    ymax_list = []

    #ar12661 [(-5, 5), (8, 0), (0, 2), (0, -1), (16,-1), (-12,0), (13,0), (-12, 0), (0, -3), (5, 0),
    #          (12, 0), (-10, 0), (12, 0), (-8, -1), (3, 0), (0, -1), (2,3), (0, 0), (5, 2), (0, 0),
    #          (2, 0), (0, 0), (0, 0), (0, 5), (0, 0), (0, 0), (0, 0), (0, 0)]
    cmap = cm.get_cmap(name='irissji2832')
    cmap2 = cm.get_cmap(name='irissji1330')
    cmap3 = cm.get_cmap(name='irissji1600')
    cmap4 = cm.get_cmap(name='irissji1400')
    cmap5 = cm.get_cmap(name='irissji2796')
    cmap6 = cm.get_cmap(name='sohoeit171')
    fig, ax = plt.subplots(2, 3, sharex=True, sharey=True)
    plt.subplots_adjust(bottom=0.07, left=0.07, top=.98, right=.98, wspace=0, hspace=0)
    writer.setup(fig, '/Users/shelbe/Documents/IRIS/raster_test.mp4', dpi=120)
    plt.style.use('dark_background')

    j = 0

    for n,i in enumerate(file_list):

        #hdulist = fits.open(i)
        #hdulist.info()
        print( 'Getting FITS data from ' + i)
        #Mg_data1 = fits.getdata(i, ext=0)
        #Mg_data2 = fits.getdata(i, ext=1)
        main_header = fits.getheader(i, ext=0)

        exptime = main_header.get('exptime')

        Mg_header = None
        for h in range(1,9):
            tdesc='TDESC' + str(h)
            twave = 'TWAVE' + str(h)
            if main_header.get(tdesc) != None:
                #print(tdesc, main_header.get(tdesc))
                if '2832' in main_header.get(tdesc):
                    wing_data = fits.getdata(i, ext=h)
                    wing_header = fits.getheader(i, ext=h)
                    wing_header['naxis1']=wing_header['naxis3']
                    wing_header['crpix1'] = wing_header['crpix3']
                    wing_header['crval1'] = wing_header['crval3']
                    wing_header['cdelt1'] = wing_header['cdelt3']
                    wing_header['ctype1'] = wing_header['ctype3']
                    wing_header['cunit1'] = wing_header['cunit3']

                if 'Mg' in main_header.get(tdesc):
                    Mg_data = fits.getdata(i, ext=h)
                    Mg_header = fits.getheader(i, ext=h)
                    print(twave, int(main_header.get(twave)),Mg_data[0].shape)



        if Mg_header == None:
            print('Header not found')
            return
        #plt.imshow(wing_data[0])
        #plt.show()
        naxis1 = Mg_header.get('NAXIS1')
        naxis2 = Mg_header.get('NAXIS2')
        naxis3 = Mg_header.get('NAXIS3')
        crpix1 = Mg_header.get('CRPIX1')
        crpix2 = Mg_header.get('CRPIX2')
        crpix3 = Mg_header.get('CRPIX3')
        crval1 = Mg_header.get('CRVAL1')
        crval2 = Mg_header.get('CRVAL2')
        crval3 = Mg_header.get('CRVAL3')
        cdelt1 = Mg_header.get('CDELT1')
        cdelt2 = Mg_header.get('CDELT2')
        cdelt3 = Mg_header.get('CDELT3')
        ctype3 = Mg_header.get('CTYPE3')
        cunit3 = Mg_header.get('CUNIT3')



        Mg_header['naxis1'] = naxis3
        Mg_header['crpix1'] = crpix3
        Mg_header['crval1'] = crval3
        Mg_header['cdelt1'] = cdelt3
        Mg_header['ctype1'] = ctype3
        Mg_header['cunit1'] = cunit3
        Mg_header['naxis'] = 2
        Mg_header.remove('crpix3')
        Mg_header.remove('crval3')
        Mg_header.remove('cdelt3')
        Mg_header.remove('ctype3')
        Mg_header.remove('cunit3')
        Mg_header.set('wavelnth', twave)
        print(Mg_header)
        #2796.4 A & 2803.5 A, 124
        date_start = datetime.datetime.strptime(main_header.get('STARTOBS'), '%Y-%m-%d' + 'T' + '%H:%M:%S.%f')
        date_end = datetime.datetime.strptime(main_header.get('ENDOBS'), '%Y-%m-%d' + 'T' + '%H:%M:%S.%f')
        dt = main_header.get('RASNRPT')
        nt = main_header.get('RASRPT')
        time_delta = (date_end - date_start) / dt
        timestamp = date_start+(time_delta*(nt-.5))
        print(str(nt)+' of '+str(dt))

        frame = 37
        xcen = (crval3 ) * u.arcsec
        ycen = (crval2 ) * u.arcsec
        print(crval3, crval2)




        wavmin = crval1 - crpix1 * cdelt1
        wavmax = crval1 + (naxis1 - crpix1) * cdelt1
        title = []
        wavelength = round(2832.0, 1)

        title.append('$' + str(wavelength) + '\AA$')
        #for lam in wave_idx:
        wave_idx2 = []
        wavelength=np.arange(0,naxis1)*(cdelt1) + wavmin
        if j >= 95:
            wave_idx = [2795.68, 2798.68, 2796.08, 2796.35, 2796.48]
        else:
            wave_idx = [2795.75, 2798.75, 2796.15, 2796.35, 2796.55]
        print(Mg_header)
            #plt.imshow()


        print(type(wavelength[0]),type(wave_idx[0]))
        for i in wave_idx:
            wave=np.where(wavelength >= i)[0]
            print(wavelength[wave[0:5]])
            wave_idx2.append(wave[0])

            title.append(str('$'+ str(round(wavelength[wave[0]],1)) + '\AA$'))
        print(title)
        mg_wing_image = (Mg_data.T[wave_idx2[0]]/exptime)
        mg_triplet_image = (Mg_data.T[wave_idx2[1]]/exptime)
        mg_k2v_image = (Mg_data.T[wave_idx2[2]]/exptime)
        mg_k3_image = (Mg_data.T[wave_idx2[3]]/exptime)
        mg_k2r_image = (Mg_data.T[wave_idx2[4]]/exptime)
        #wing_image = wing_data.T[15]/exptime

        # if j == 94 or j == 95:
        #     fig=plt.figure()
        #     plt.plot((Mg_data[wave_idx2[3]][0]/exptime),'bo', fig)
        #     plt.show()
        #wave_list0.append(())

        mg_wing =SJIMap(mg_wing_image, Mg_header)
        mg_triplet = SJIMap(mg_triplet_image, Mg_header)
        mg_k2v = SJIMap(mg_k2v_image, Mg_header)
        mg_k3 = SJIMap(mg_k3_image, Mg_header)
        mg_k2r = SJIMap(mg_k2r_image, Mg_header)
        if n == 0:
            # Set Starting Coordinates (arcsec)

            layer = mg_k3.data[crpix2 - 250:crpix2 + 250, crpix1 - 80:crpix1 + 80]

            st = datetime.datetime.strptime(mg_k3.meta['DATE-OBS'], '%Y-%m-%d' + ' ' + '%H:%M:%S.%f')
            et = datetime.datetime.strptime(mg_k3.meta['DATE-OBS'], '%Y-%m-%d' + ' ' + '%H:%M:%S.%f')
            xshift = 0.*u.arcsec
            yshift = 0.*u.arcsec
            xcen = (crval1 - xshift.value) * u.arcsec
            ycen = (crval2 - yshift.value) * u.arcsec
            cen = SC(xcen, ycen, frame='helioprojective', obstime=st)

            xlength = 50  # Cropping dimensions
            ylength = 50

            x0 = (cen.data._lon.arcsec - .5 * xlength)
            y0 = (cen.data._lat.arcsec - .5 * ylength)
            bl = SC(x0 * u.arcsec, y0 * u.arcsec, frame='helioprojective',
                    obstime=st)  # Bottom Left and Top Right coordinates
            tr = SC((x0 + xlength) * u.arcsec, (y0 + ylength) * u.arcsec, frame='helioprojective', obstime=st)

        elif n > 0:
            # Get new start time
            st = datetime.datetime.strptime(mg_k3.meta['DATE-OBS'], '%Y-%m-%d' + ' ' + '%H:%M:%S.%f')

            # Rotate Helio Projective Coordinates from end-start time (time elapsed between obs)
            if rotate == True:
                cen = diff_rot.solar_rotate_coordinate(cen, st, frame_time='synodic', rot_type='snodgrass')


            ycrop = 225
            xcrop = 45
            yoffset = 25
            xoffset = 35
            template = mg_k3.data[crpix2 - ycrop:crpix2 + ycrop, crpix1 - xcrop:crpix1 + xcrop]
            shift = calculate_shift(layer, template)
            # if xyshift hits shift boundaries, resize template, rerun calculate shift
            while (shift[0].value >= 2. * yoffset) or (shift[1].value >= 2. * xoffset):
                if shift[0].value == 2. * yoffset:
                    ycrop -= 10
                    yoffset += 10
                if shift[1].value == 2. * xoffset:
                    xcrop -= 10
                    xoffset += 10
                    template = mg_k3.data[crpix2 - ycrop:crpix2 + ycrop, crpix1 - xcrop:crpix1 + xcrop]
                    shift = calculate_shift(layer, template)

            print(shift)
            xshift += (shift[1] - xoffset * u.pix) * mg_k3.scale[0]
            yshift += (shift[0] - yoffset * u.pix) * mg_k3.scale[1]
            print(i, ' Xcorr: ', (xshift.round(0), yshift.round(0)))
            layer = mg_k3.data[crpix2 - 250:crpix2 + 250, crpix1 - 80:crpix1 + 80]
            print('New layer created')
        xcen = (crval1 - xshift.value) * u.arcsec
        if rotate == True:
            ycen = cen.data._lat
        else:
            ycen = (crval2 - yshift.value) * u.arcsec
        print(xcen, ycen)
        cen = SC(xcen, ycen, frame='helioprojective', obstime=st)

            # New Submap Boundaries
        x0 = (cen.data._lon.arcsec - .5 * xlength)
        y0 = (cen.data._lat.arcsec - .5 * ylength)
        print(x0, y0)
        print(i, crval1 - .5 * xlength, crval2 - .5 * xlength)
            # Bottom Left and Top Right coordinates
        bl = SC(x0 * u.arcsec, y0 * u.arcsec, frame='helioprojective', obstime=st)
        tr = SC((x0 + xlength) * u.arcsec, (y0 + ylength) * u.arcsec, frame='helioprojective', obstime=st)

        # Get new end time
        et = datetime.datetime.strptime(mg_k3.meta['DATE-OBS'], '%Y-%m-%d' + ' ' + '%H:%M:%S.%f')
   # wing = SJIMap(wing_image,wing_header)
        mg_k3 = mg_k3.submap(bl,tr)
        mg_wing.plot(axes=ax[0, 1], cmap = cmap6, norm = colors.PowerNorm(.3, 1, 80))
        mg_triplet.plot(axes=ax[0, 2], cmap = cmap2, norm = colors.PowerNorm(.5, 1, 40))
        mg_k2v.plot(axes=ax[1, 0], cmap = cmap4 ,norm = colors.PowerNorm(.7, 5, 200))
        mg_k3.plot(axes=ax[1, 1], cmap = cmap3 ,norm = colors.PowerNorm(.7, 5, 200))
        mg_k2r.plot(axes=ax[1, 2], cmap = cmap5 ,norm = colors.PowerNorm(.7, 5, 200))
        #wing.plot(axes=ax[0, 0], cmap = cmap, norm = colors.PowerNorm(.9, 1, 220))

        ax[0, 0].set_title(title[0], visible=False)
        ax[0, 1].set_title(title[1], visible=False)
        ax[0, 2].set_title(title[2], visible=False)
        ax[1, 0].set_title(title[3], visible=False)
        ax[1, 1].set_title(title[4], visible=False)
        ax[1, 2].set_title(title[5], visible=False)
        ax[0, 0].set_xlabel('X [Arcsec]', visible=False)
        ax[0, 0].set_ylabel('Y [Arcsec]', color='white')
        ax[0, 0].set_xlim(xmin, xmax)
        ax[0, 0].set_ylim(ymin, ymax)
        plt.setp(ax[0, 1].get_yticklabels(), visible=False)
        plt.setp(ax[0, 2].get_yticklabels(), visible=False)
        plt.setp(ax[1, 1].get_yticklabels(), visible=False)
        plt.setp(ax[1, 2].get_yticklabels(), visible=False)

        ax[0, 1].set_xlabel('X [Arcsec]', visible=False)
        ax[0, 1].set_ylabel('Y [Arcsec]', visible=False)
        #
        ax[0, 2].set_xlabel('X [Arcsec]', color='white')
        ax[0, 2].set_ylabel('Y [Arcsec]', visible=False)

        ax[1, 0].set_xlabel('X [Arcsec]', visible=False)
        ax[1, 0].set_ylabel('Y [Arcsec]', color='white')

        ax[1, 1].set_xlabel('X [Arcsec]', color='white')
        ax[1, 1].set_ylabel('Y [Arcsec]', visible=False)

        ax[1, 2].set_xlabel('X [Arcsec]', visible=False)
        ax[1, 2].set_ylabel('Y [Arcsec]', visible=False)

        ax[1, 0].annotate('IRIS' + ' ' + timestamp.strftime('%Y/%m/%d %H:%M:%S'),
                          xy=(xmin + 1, ymin + 1), color='white', fontsize=5, zorder=1)
        ax[0, 0].annotate(title[0], xy=(xmin + 1, ymin + 2), color='black', fontsize=6, zorder=1)
        ax[0, 1].annotate(title[1], xy=(xmin + 1, ymin + 5), color='white', fontsize=6, zorder=1)
        ax[0, 2].annotate('Mg II Triplet ', xy=(xmin + 1, ymin + 5), color='white', fontsize=6, zorder=1)
        ax[1, 0].annotate('Mg II k$_{2v}$ ', xy=(xmin + 1, ymin + 5), color='white', fontsize=6, zorder=1)
        ax[1, 1].annotate('Mg II k$_{3}$ ', xy=(xmin + 1, ymin + 5), color='white', fontsize=6, zorder=1)
        ax[1, 2].annotate('Mg II k$_{2r}$ ', xy=(xmin + 1, ymin + 5), color='white', fontsize=6, zorder=1)
        # print(crval3, ymin)


        writer.grab_frame()
        # plt.show()
        ax[0, 0].cla()
        ax[0, 1].cla()
        ax[0, 2].cla()
        ax[1, 0].cla()
        ax[1, 1].cla()
        ax[1, 2].cla()

raster(raster_list)