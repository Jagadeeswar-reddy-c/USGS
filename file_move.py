import shutil
import os

import pandas as pd

import file_handle


def file_mov(dst_path, file):
    file = file
    product_id = file['Display ID']
    src_path = os.path.dirname(os.path.abspath(__file__))
    src_path = src_path + '/'
    dst_path = dst_path
    dst_path = dst_path + '/'
    lst = []

    for path in os.listdir(src_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(src_path, path)):
            lst.append(path)
    mov = []
    for _ in range(0, len(lst)):
        if lst[_] in list(product_id):
            mov.append(lst[_])
        else:
            pass
    for _ in mov:
        shutil.move(src_path + _, dst_path + _)
        print('Moved')
