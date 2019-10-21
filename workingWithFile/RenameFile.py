import os

path = r'C:\Users\tamee\PycharmProjects\workingWithFile\pictures'
magic_numbers = {'jpg': bytes([0xFF, 0xD8, 0xFF]),
                 'png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A]),
                 'bmp': bytes([0x4D, 0x42]),
                 'tif': bytes([0x49, 0x49, 0x2A, 0x00]),
                 'gif': bytes([0x47, 0x49, 0x46, 0x38])}


def TypeRecovery(path):
    if not os.path.isdir(path):
        raise IsADirectoryError("directory not found!!!")
    fileNames = os.listdir(path)

    # each file start with its signature,key:type value:signature
    max_read_size = max(len(m) for m in magic_numbers.values())  # get max size of magic numbers of the dict
    i = 0
    for file in fileNames:
        file = path + "\\" + file
        with open(file, "rb") as fd:
            file_head = fd.read(max_read_size)
        for magic in magic_numbers:
            if file_head.startswith(magic_numbers[magic]):
                filename = os.path.splitext(file)[0][-1]
                dst = path + f"\\{filename}.{magic}"
                os.rename(file, dst)


def deleteExtension(path):
    fileNames = os.listdir(path)
    for file in fileNames:
        file = path + "\\" + file

        filename = os.path.splitext(file)[0][-1]
        dst = path + f"\\{filename}"
        os.rename(file, dst)



