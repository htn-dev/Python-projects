# This program will shutdown your computer when executed. Make sure to save all your works before execute it

import os

shutdown = input("Do you want to shut down your computer? (Y/N) ")

if shutdown == 'Y':
    os.system('shutdown /s /t 1')
else:
    print('Shutdown is not requested.')