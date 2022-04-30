import os
import git
import time
import datetime

config = """[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	ignorecase = true
[remote "origin"]
	url = {0}
	fetch = +refs/heads/*:refs/remotes/origin/*"""

# f = open('document.txt', 'a')
# f.writelines('changed')

class AutoTest:
    def __init__(self, r):
        self.__cached_stamp = 0
        self.r = r
        self.filename = 'document.txt'

    def changedTest(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self.__cached_stamp:
            url = 'https://github.com/vishnuteja2424/gitAutoTest.git'
            branch = 'master'
            self.__cached_stamp = stamp
            self.r.index.add([self.filename])
            self.r.index.commit(str(datetime.datetime.now()))
            configFile = open('.git/config', 'w')
            configFile.write(config.format(url))
            self.r.


repo_dir = os.getcwd()
r = git.Repo.init(repo_dir)
a = AutoTest(r)
while True:
    time.sleep(1)
    a.changedTest()