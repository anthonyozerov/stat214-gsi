import os
import requests
import skimage as ski
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
# please don't do import * in production code :)
from pyhdf.SD import *

dates = pd.read_html('all_date_page.html')[0]['Name']
dates = dates[~pd.isna(dates)]

TOKEN = "put NASA Earthdata token here"

# path where files will temporarily be stored. It should probably be
# a ramdisk to reduce the number of writes to the disk.
TMP_PATH = '/tmp/ramdisk'

# the MISR blocks we want
blocks = [22, 23, 24]
# the MISR path which we want
misr_path = 'P026'
# the bands we want
colors = ['NIR', 'Red', 'Green', 'Blue']
# the angles we want
angle_names = ['DA', 'CA', 'BA', 'AA', 'AN', 'AF', 'BF', 'CF', 'DF']

# for each date, download, process, and save the MISR data.
for date in dates:

    # download the html page containing the files for that date
    dir_path = f"https://asdc.larc.nasa.gov/data/MISR/MI1B2T.003/{date}"
    html_page = requests.get(dir_path,
                        headers={'Authorization': f'Bearer {TOKEN}'}).text

    # get the list of files which are .hdf terrain-projected
    # files for the MISR path we want
    soup = BeautifulSoup(html_page)
    links = []
    for element in soup.findAll('a'):
        link = element.get('href')
        if (misr_path in link) and ('.hdf' in link) and ('TERRAIN' in link) and (not 'xml' in link):
            links.append(link)
    links = np.unique(links)

    # if there are no files for that date, skip
    if len(links) == 0:
        continue
    print(date)

    # for each angle, download the .hdf file, extract the data in the different
    # bands, downsample if needed, stack them into a numpy matrix, then save it
    # with compression
    angles = []
    for angle_name in angle_names:
        print(f'downloading and processing {angle_name}')

        # get the link for the file with the angle we want
        link = [l for l in links if f'_{angle_name}_' in l][0]
        # the full remote path to the file
        path = dir_path+link

        # use wget to download the file to the temporary storage location
        os.system(f'wget -4 --compression=gzip --header "Authorization: Bearer {TOKEN}" --no-parent --reject "index.html*" "{path}" -P {TMP_PATH} -q')
        # load the file as a scientific dataset object
        f = SD(f'{TMP_PATH}/{link}')

        imgs = []
        # for each color, extract the data and downsample if needed
        for color in colors:
            imgs_color = []
            # extract the data for each block, then stack them vertically
            for block in blocks:
                imgs_color.append(f.select(f'{color} Radiance/RDQI')[block-1])
            img = np.vstack(imgs_color)
            # mask the values which are above 65500
            img = np.ma.masked_where(img>65500, img)

            # downsample if needed (the AN angle has higher resolution)
            if img.shape[1]==2048:
                img = ski.measure.block_reduce(img, block_size=4, func=np.mean)
            imgs.append(img)
        # stack the 4 different color bands
        rgb = np.dstack(imgs)
        # convert to uint8
        rgb = (rgb//256).astype(np.uint8)
        # append to the list of angles
        angles.append(rgb)
        # remove the downloaded file
        os.remove(f'{TMP_PATH}/{link}')
    # create a 4D masked array from the list of 3D masked arrays for each angle
    to_save = np.ma.masked_array(angles)
    # get the orbit number of the file
    orbit_num = links[0].split('_')[6]
    # save the 4D masked array with compression
    np.savez_compressed(f'../data/{orbit_num}.npz',to_save)
