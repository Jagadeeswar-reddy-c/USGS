import os

import pandas as pd

import download_data
import file_handle
import tar_tiff

def Main_pro():
    username = input("enter your username :")
    password = input("enter your password :")


    path_csv = r'/home/jr/Desktop/test'
    dst_path = r'/home/jr/Desktop/test/test'

    csv_file = os.listdir(path_csv)
    dst_file = os.listdir(dst_path)

    for _ in range(0, len(csv_file)):
        file_csv = path_csv + '/' + csv_file[_]
        if file_csv[-4:] == '.csv':
            file = pd.read_csv(file_csv, encoding='latin1')
            directory = str(csv_file[_])
            directory = directory[:-4]
            if directory in dst_file:
                pass
            else:
                path = os.path.join(dst_path, directory)
                os.mkdir(path)

            dst = dst_path + '/' + directory
            dst_lst = os.listdir(dst)

            product_id = file['Landsat Product Identifier L2']

            lat1 = file['Corner Lower Left Latitude']
            lat2 = file['Corner Lower Left Longitude']

            lon1 = file['Corner Upper Right Latitude']
            lon2 = file['Corner Upper Right Longitude']

            start_date = file['Date Acquired']
            end_date = file['Date Acquired']

            file_chk = file_handle.file_check(dst)

            print(directory)
            temp = os.listdir(dst)

            for i in range(0, len(product_id)):
                file_chk = file_handle.file_check(dst)
                print("The latitude for lower left is : ", lat1[i])
                print("The longitude for lower left is : ", lat2[i])

                print("The latitude for upperright: ", lon1[i])
                print("The longitude is upperright: ", lon2[i])
                
                if product_id[i] in file_chk:
                    print('\n\n')
                    print('tile completed : ' + product_id[i])
                    print('\n\n')
                    dst_lst = os.listdir(dst)
                    file_handle.file_handle(dst, dst_lst, file)
                    try:
                        tar_tiff.tar_tiff(dst)
                    except:
                        shutil.rmtree(dst)
                        pass
                        #
                    tar_tiff.tar_del(dst)
                    pass
                else:
                    download_data.main(username,password,'Landsat 8-9 OLI/TIRS C2 L2', lat1[i], lat2[i], lon1[i], lon2[i], start_date[i],
                                    end_date[i], dst, file)
                    dst_lst = os.listdir(dst)
                    file_handle.file_handle(dst, dst_lst, file)
                
                    dst_lst = os.listdir(dst)
                    file_handle.file_handle(dst, dst_lst, file)
                    dst_lst = os.listdir(dst)
                
                    tar_tiff.tar_tiff(dst)
                    tar_tiff.tar_del(dst)
                
                
            try:
                dst_lst = os.listdir(dst)
                file_handle.file_handle(dst, dst_lst, file)
            except Exception as e:
                pass
            dst_lst = os.listdir(dst)
            try:
                tar_tiff.tar_tiff(dst)
                tar_tiff.tar_del(dst)
            except Exception:
                pass
            
        else:
            pass
