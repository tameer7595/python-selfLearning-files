import os
path = r'C:\Users\tamee\PycharmProjects\workingWithFile\pictures'

def TypeRecovery(path):
    fileNames = os.listdir(path)
    #each file start with its signature,key:type value:signature
    magic_numbers = {'jpg': bytes([0xFF, 0xD8, 0xFF]),
                     'png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
                     'bmp' : bytes([0x4D, 0x42]),
                     'tif' : bytes([0x49 ,0x49 ,0x2A , 0x00]),
                     'gif' : bytes([0x47 ,0x49, 0x46, 0x38])}
    max_read_size = max(len(m) for m in magic_numbers.values())  # get max size of magic numbers of the dict
    i=0
    for file in fileNames :
        file = path + "\\" + file
        with open(file,"rb") as fd:
            file_head = fd.read(max_read_size)

        if file_head.startswith(magic_numbers['jpg']):
            filename = os.path.splitext(file)[0][-1]
            dst = path + f"\\{filename}.jpg"
            os.rename(file,dst)


def deleteExtension(path):
    fileNames = os.listdir(path)
    for file in fileNames :
        file = path + "\\" + file

        filename = os.path.splitext(file)[0][-1]
        dst = path+f"\\{filename}.bbb"
        os.rename(file,dst)

if __name__ == '__main__':
    deleteExtension(path)
    TypeRecovery(path)
