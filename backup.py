import os, sys, shutil
# import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)

from termcolor import colored as c
from datetime import datetime as dt


# match passed params
SCRIPTFILE = sys.argv[0]
SRC_PATH = sys.argv[1]
DEST_PATH = sys.argv[2]
ORIGIN_DIR = os.path.dirname(os.path.abspath(SCRIPTFILE))
STORAGE_DIR = 'storage'
DATE_FORMAT = '%d%m%Y-h%Hm%Ms%S'
FULLPATH_STORAGE = DEST_PATH + STORAGE_DIR # full path of the storage zip folder

# change dir in the passed destination path
os.chdir(DEST_PATH)
try:
	# create standard dir folder 'storage'
	os.mkdir(STORAGE_DIR, 0755)
	print c('WELLDONE, CREATED SUCCESSFULLY!!', 'yellow')
except:
	# handle OSError exception
	print c('Folder already exists!!', 'yellow')
	pass

os.chdir(STORAGE_DIR)

print c('START: running compress mode','cyan')

# create an archive file
ZIP_NAME = 'WorkzoneBAK-{}'.format(dt.now().strftime(DATE_FORMAT))
try:
	shutil.make_archive(ZIP_NAME,'zip', SRC_PATH, verbose=True)
except:
	print 'large zip file'
	print c('Files count would require ZIP64 extensions!!','red')



print c('END: File compression completed!!', 'cyan')


# print os.listdir('.') # or os.system('ls')
# print os.path.getsize(os.listdir('.')[0])
# print os.getcwd()
