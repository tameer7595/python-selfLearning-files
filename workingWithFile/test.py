import os
from RenameFile import *


if __name__ == '__main__':
    deleteExtension(path)
    try:
        TypeRecovery(path)
    except IsADirectoryError as ex:
        print(ex.args)