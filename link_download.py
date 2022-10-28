import os

import requests

import file_move

download_list = []


def download(url, dst_path, file):
    file = file
    display_id = file['Display ID']
    url = url

    if 'landsat_product_id' in url:

        str_index = url.index('landsat_product_id=')
        s_index = str_index + 19
        end_index = url.index('&')
        e_index = end_index
        global res
        res = ''

        for _ in range(s_index, e_index):
            res = res + url[_]
        if res in list(display_id):

            if res not in list(set(download_list)):

                if res in list(os.listdir(dst_path)):
                    pass
                elif (res + '.tif') in list(os.listdir(dst_path)):
                    pass
                else:

                    print('downloading tail : ', res)

                    r = requests.get(url)

                    print('downloaded completed.')

                    open(res, "wb").write(r.content)

                    download_list.append(res)

                    file_move.file_mov(dst_path, file)
            else:
                pass
    else:
        pass
