# Python program to shutdown your computer
# Make sure to save all your works before execute this program

import os

shutdown = input("Do you want to shut down your computer? (y/n) ")

if shutdown == 'y':
    os.system('shutdown /s /t 1')
else:
    print('Shutdown is not requested.')
