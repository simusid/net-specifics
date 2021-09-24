import shutil
class NSImage():
    def __init__(self, name, fname):
        self.name= name
        self.count= 0
        self.filename = fname


def makeNewClass(index):
    src = "app/static/array/{}.jpg".format(index)
    dst = "app/static/test{}.jpg".format(index)
    fname = "test{}.jpg".format(index)
    shutil.copyfile(src, dst)
    return [index,fname, 0]
