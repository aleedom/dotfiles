import os

from socket import gethostname
hostname = gethostname()
username = os.environ['USER']
pwd = os.getcwd()
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)
path_dirs = pwd.split('/')
if os.path.isabs(pwd):
    path_dirs[1] = "/"+path_dirs[1]
    path_dirs = path_dirs[1:]
if len(path_dirs) > 2:
    pwd = "{}/ ... /{}".format(path_dirs[0], path_dirs[-1])
print(pwd)
