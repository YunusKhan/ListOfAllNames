from staticurl import staticurl
from filelist import filelist
from nameslist import nameslist
from conn import conn

if __name__ == "__main__":
    # get all links first per directory and per gender
    # per directory, go to gender file
    # per gender, add in list all names
    # return global list and insert into db
    listofdir = staticurl().listofdir
    f = filelist()
    n = nameslist()
    dbconn = conn()
    for allitems in listofdir:
        if 'indian' in allitems:
            indianboyfilelist = f.getfilelist(allitems + '/Boy')
            indiangirlfilelist = f.getfilelist(allitems + '/Girl')
        if 'german' in allitems:
            germanboyfilelist = f.getfilelist(allitems + '/Boy')
            germangirlfilelist = f.getfilelist(allitems + '/Girl')
        if 'french' in allitems:
            frenchboyfilelist = f.getfilelist(allitems + '/Boy')
            frenchgirlfilelist = f.getfilelist(allitems + '/Girl')
        if 'arabic' in allitems:
            arabicboyfilelist = f.getfilelist(allitems + '/Boy')
            arabicgirlfilelist = f.getfilelist(allitems + '/Girl')
        if 'english' in allitems:
            englishboyfilelist = f.getfilelist(allitems + '/Boy')
            englishgirlfilelist = f.getfilelist(allitems + '/Girl')
        if 'australian' in allitems:
            australianboyfilelist = f.getfilelist(allitems + '/Boy')
            australiangirlfilelist = f.getfilelist(allitems + '/Girl')

    australiangirl = n.getnames(australiangirlfilelist)
    australianboy = n.getnames(australianboyfilelist)
    indiangirl = n.getnames(indiangirlfilelist)
    indianboy = n.getnames(indianboyfilelist)
    arabicgirl = n.getnames(arabicgirlfilelist)
    arabicboy = n.getnames(arabicboyfilelist)
    germangirl = n.getnames(germangirlfilelist)
    germanboy = n.getnames(germanboyfilelist)
    frenchgirl = n.getnames(frenchgirlfilelist)
    frenchboy = n.getnames(frenchboyfilelist)
    englishgirl = n.getnames(englishgirlfilelist)
    englishboy = n.getnames(englishboyfilelist)

    # this below is for mongo database inserts
    # if mongo is not installed, please consider just printing the variables 
    # print englishboy, indiangirl
    # alternatively you can pass them to another existing function to consume that values
    
    dbconn.insertintodb("arabicgirl", arabicgirl)
    dbconn.insertintodb("arabicboy", arabicboy)
    dbconn.insertintodb("indiangirl", indiangirl)
    dbconn.insertintodb("indianboy", indianboy)
    dbconn.insertintodb("germangirl", germangirl)
    dbconn.insertintodb("germanboy", germanboy)
    dbconn.insertintodb("frenchgirl", frenchgirl)
    dbconn.insertintodb("frenchboy", frenchboy)
    dbconn.insertintodb("englishgirl", englishgirl)
    dbconn.insertintodb("englishboy", englishboy)
    dbconn.insertintodb("australiangirl", australiangirl)
    dbconn.insertintodb("australianboy", australianboy)
 
