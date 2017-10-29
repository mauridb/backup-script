import os, sys, shutil
# import logging
# logging.basicConfig(filename='example.log',level=logging.DEBUG)

from termcolor import colored as c
from datetime import datetime as dt


# match passed params
SCRIPTFILE = sys.argv[0]
SRC_PATH = sys.argv[1]
SRC_PATH_SPLITTED = SRC_PATH.split('/')
DEST_PATH = sys.argv[2]
ORIGIN_DIR = os.path.dirname(os.path.abspath(SCRIPTFILE))
STORAGE_DIR = 'storage'
DATE_FORMAT = '%d%m%Y-h%Hm%Ms%S'
FULLPATH_STORAGE = DEST_PATH + STORAGE_DIR # full path of the storage zip folder

print c('APP LAUNCHED..','green')

# change dir in the passed destination path
os.chdir(DEST_PATH)
try:
	# create standard dir folder 'storage'
	os.mkdir(STORAGE_DIR, 0755)
	print c('Welldone, storage folder created succesfully!!', 'yellow')
except:
	# handle OSError exception
	print c('Storage folder already exists!!', 'yellow')
	pass

os.chdir(STORAGE_DIR)
specific_dir_name = '{}_BACKUPS'.format(SRC_PATH_SPLITTED[len(SRC_PATH_SPLITTED)-2]) # specific dir name
try:
	os.mkdir(specific_dir_name,0755)
	print c('Welldone, specific folder created succesfully!!', 'yellow')
except:
	print c('Specific folder already exists!!', 'yellow')

os.chdir(specific_dir_name)
	
print c('START: running compress mode','cyan')

# create an archive file
# ZIP_NAME = 'WorkzoneBAK-{}'.format(dt.now().strftime(DATE_FORMAT))
ZIP_NAME = '{}BAK-{}'.format(SRC_PATH_SPLITTED[len(SRC_PATH_SPLITTED)-2],dt.now().strftime(DATE_FORMAT))
try:
	shutil.make_archive(ZIP_NAME,'zip', SRC_PATH, verbose=True)
except:
	print 'large zip file'
	print c('Files count would require ZIP64 extensions!!','red')



print c('END: File compression completed!!', 'cyan')
print c('APP TERMINATED CORRECTLY..','green')


# print os.listdir('.') # or os.system('ls')
# print os.path.getsize(os.listdir('.')[0])
# print os.getcwd()
