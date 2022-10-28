import os


def file_handle(dst_path, dst_lst, file):
    file = file
    product_id = file['Landsat Product Identifier L2']
    for i in range(0, len(dst_lst)):
        files = os.listdir(dst_path)
        lst = files[i]
        if str(lst[-4:]) == '.tar':
            pass
        else:
            if lst not in dst_lst:
                pass
            else:
                dst = dst_path + '/' + str(dst_lst[i])
                my_file = str(dst)
                base = os.path.splitext(my_file)[0]
                temp = my_file[-40:]
                isDirectory = os.path.isdir(my_file)
                if temp in dst_lst:
                    if lst not in files:
                        pass
                    else:
                        if isDirectory:
                            pass
                        else:
                            os.rename(my_file, base + '.tar')
                else:
                    pass


def file_check(dst):
    dst = os.listdir(dst)
    lst = []
    for _ in range(0, len(dst)):
        dirt = str(dst[_])
        if str(dirt[-4:]) == '.tar':
            dirt = dirt[:-4]
            lst.append(dirt)
        elif str(dirt[-4:] == '.tif'):
            dirt = dirt[:-4]
            lst.append(dirt)
        elif str(dirt):
            lst.append(dirt)
        else:
            lst.append(dirt)
    return lst
