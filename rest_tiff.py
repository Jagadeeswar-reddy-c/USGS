import os
import glob
import matplotlib.pyplot as plt
import earthpy.plot as ep
import rasterio as rio
import earthpy.spatial as es


def rest_tiff(file):
    file_lst = file + '/*'
    multi_bands = glob.glob(file_lst)

    files = file + '.tif'
    landsat_multi_path = files
    print(landsat_multi_path)

    land_stack, land_meta = es.stack(multi_bands, landsat_multi_path)

    with rio.open(multi_bands[2]) as src:
        landsat_band4 = src.read()

    with rio.open(landsat_multi_path) as src:
        landsat_multi = src.read()
    
    return landsat_multi_path
