import os
import tarfile
import rest_tiff


def tar_tiff(dst):
    file = dst
    dst_list = os.listdir(dst)
    extract_file = dst_list
    lst = []
    for _ in range(0, len(dst_list)):
        dst_file = file + '/' + extract_file[_]
        dir_path = dst_file[:-4]
        lst_file = os.listdir(dst)
        lst_chk = lst_file[_]
        if lst_chk not in lst_file[_]:
            lst.append(lst_file[_])
            pass
        else:
            if lst_file[_].endswith('.tar'):
                if dir_path in dst_list:
                    pass
                else:
                    if str(dst_file[-4:]) == '.tar':
                        os.path.join(file, dir_path)
                        my_tar = tarfile.open(dst_file, "r:")
                        print(dir_path)
                        try:
                            my_tar.extractall(dir_path)
                            my_tar.close()
                        except:
                            pass
                        for i in os.listdir(dir_path):
                            if i.endswith('B2.TIF'):
                                lst.append(i)
                            elif i.endswith('B3.TIF'):
                                lst.append(i)
                            elif i.endswith('B4.TIF'):
                                lst.append(i)
                            else:
                                os.remove(dir_path + '/' + i)

                    img_check = rest_tiff.rest_tiff(dir_path)
                    img_check = img_check[-44:]
                    for i in os.listdir(dir_path):
                        if img_check in i:
                            pass
                        else:
                            os.remove(dir_path + '/' + i)
            else:
                pass


def tar_del(dst):
    file = dst
    dst_list = os.listdir(dst)
    extract_file = dst_list
    lst = []
    for _ in range(0, len(dst_list)):
        dst_file = file + '/' + extract_file[_]
        dir_path = dst_file
        if str(dst_file[-4:]) == '.tar':
            os.remove(dst_file)
            print('removed')
        elif os.path.isdir(dst):
            if str(dst_file[-4:]) == '.tif':
                pass
            else:
                temp = dst + '/' + extract_file[_]
                os.rmdir(temp)
                print('removed')
        else:
            print('not done')

#dst = r'/home/jr/Downloads/test'
#tar_tiff(dst)