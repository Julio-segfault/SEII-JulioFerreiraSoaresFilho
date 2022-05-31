
import os
from datetime import datetime

#print(dir(os))
#os.chdir('/home/')

#os.mkdir('Os-Demo-2')
#os.makedirs('OS-Demo-2/Sub-Dir-1')
#os.rmdir('OS-Demo-2/Sub-Dir-1')
#os.removedirs('OS-Demo-2/Sub-Dir-1')
#os.rename('text.txt', 'demo.txt')

print(os.getcwd())
print(os.listdir())

print(os.stat('demo.txt'))
mod_time = os.stat('demo.txt').st_mtime
print(datetime)
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print('-----')

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'teste.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isfile('/tmp/fgfg'))
print(os.path.isdir('/tmp/fgfg'))
print(os.path.splitext('/tmp/test.txt'))