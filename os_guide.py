# init python backup script

#builtin libs
import os

print os.name, os.environ['HOME']



# os.chdir('..')
print type(os.getcwd())
print type(os.getcwdu())
print os.listdir('.')
os.mkdir('backup', 0755)
os.rename('backup', 'CACCCCCCCCCAAAAAA')


statinfo = os.stat('backup.py')
print statinfo
print statinfo.st_size


os.system('echo "caccone"')


print os.curdir, os.pardir

print os.path.abspath(os.curdir)
print os.path.basename(os.path.abspath(os.curdir))
print os.path.dirname(os.path.abspath(os.curdir))


print os.path.abspath('backup.py')
print os.path.getsize('backup.py')


print os.path.join(os.path.abspath('backup.py'), 'templates')
print os.path.join(os.path.dirname(os.path.abspath('backup.py')), 'templates')

print os.path.split(os.path.abspath('backup.py'))
