import os

class filelist:
    def getfilelist(self, path):
        allfilelist = []
        htmlfilelist = []
        #"/home/khany1/Downloads/test/"

        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                allfilelist.append(os.path.join(root, name))
            for name in dirs:
                allfilelist.append(os.path.join(root, name))

        for items in allfilelist:
            if 'html' in items:
                htmlfilelist.append(items)
        return htmlfilelist