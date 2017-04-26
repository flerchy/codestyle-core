'''
Author: Muhammad Aman (therefore the "MA" in "MAthecoder")
Project Name: Python made File Organiser
'''
#----------------------------------------------
from os import listdir, makedirs, remove
from os.path import exists as pathExists
from sys import exit as sysExit
from os.path import join , isfile
from shutil import copy
#----------------------------------------------
class OrganiserSystem():

    def __init__(self):
        global executables
        global jars
        global images
        global misc
        global compressed
        global sounds
        global docs
        global torrents
  

    def StartSorting(self,path):
        #check if path exists
        if pathExists(path):
            #filter non-files
            files = listdir(path)
            print files
            filtered=[]
            for f in files:
                if isfile(join(path,f)):
                    filtered.append(f)
            print filtered
                    
        else:
            print 'WARNING: PATH DOES NOT EXIST PROGRAM WILL NOW EXIT'
            raw_input('press <enter> to continue')
            sysExit()
        self.CheckFolders(path)
        #define some lists
        self.executables=[]
        self.jars=[]
        self.images=[]
        self.misc=[]
        self.compressed=[]
        self.sounds=[]
        self.docs=[]
        self.torrents=[]
        #sorting
        for f in filtered:
            s = f.split('.')
            #check if the file has an extension. If not, it is probably a folder and will not be sorted
            if len(s) < 2:
                continue
            if f.endswith('.exe'):
                self.executables.append(".".join(s))
                print 'sorting "%s" into executables...' % '.'.join(s)
            elif f.endswith('.jar'):
                self.jars.append(".".join(s))
                print 'sorting "%s" into jars...' % '.'.join(s)
            elif f.endswith('.png') or f.endswith('.jpg') or f.endswith('.bmp') or f.endswith('.gif'):
                self.images.append(".".join(s))
                print 'sorting "%s" into images...' % '.'.join(s)
            elif f.endswith('.zip') or f.endswith('.rar') or f.endswith('.7z') or f.endswith('.tar.gz'):
                self.compressed.append(".".join(s))
                print 'sorting "%s" into compressed...' % '.'.join(s)
            elif f.endswith('.wav') or f.endswith('.mp3') or f.endswith('.mp4') or f.endswith('.ogg') or f.endswith('.it') or f.endswith('.midi'):
                self.sounds.append(".".join(s))
                print 'sorting "%s" into compressed...' % '.'.join(s)
            elif f.endswith('.doc') or f.endswith('.odt') or f.endswith('.rtf') or f.endswith('.pdf') or f.endswith('docx') or f.endswith('.html') or f.endswith('.htm') or f.endswith('.xml'):
                self.docs.append(".".join(s))
                print 'sorting "%s" into documents...' % '.'.join(s)
            elif f.endswith('.torrent'):
                self.torrents.append(".".join(s))
                print 'sorting "%s" into torrent...' % '.'.join(s)
            else:
                self.misc.append(".".join(s))
                print 'sorting "%s" into misc...' % '.'.join(s)
            self.Sort(path)
        #some Output
        print '===================Sorted==========================='
        print 'All sorting has finished'
        print '(If error messages are recieved. Please ignore them first, \nand check if your files were sorted)'
        print 'executables: ' + str(self.executables)
        print 'jars: ' + str(self.jars)
        print 'Images: ' + str(self.images)
        print 'compressed: ' + str(self.compressed)
        print 'sounds & music: ' + str(self.sounds)
        print 'Documents: ' + str(self.docs)
        print 'misc: ' + str(self.misc)
        print 'torrent: ' + str(self.torrents)

    #Checks if required folders exist, and if not creates them
    def CheckFolders(self,directory):
        #-------------------------------------------------------------Exe
        if not pathExists(join(directory,'executables')):
            print 'Creating "executables" folder in %s"' % directory
            makedirs(join(directory,'executables'))
        #-------------------------------------------------------------images
        if not pathExists(join(directory,'images')):
            print 'Creating "images" folder in %s"' % directory
            makedirs(join(directory,'images'))
        #-------------------------------------------------------------jars
        if not pathExists(join(directory,'jars')):
            print 'Creating "jars" folder in %s"' % directory
            makedirs(join(directory,'jars'))
        #-------------------------------------------------------------misc
        if not pathExists(join(directory,'misc')):
            print 'Creating "misc" folder in %s"' % directory
            makedirs(join(directory,'misc'))
        #-------------------------------------------------------------compressed
        if not pathExists(join(directory,'compressed')):
            print 'Creating "compressed" folder in %s"' % directory
            makedirs(join(directory,'compressed'))
        #-------------------------------------------------------------sfx
        if not pathExists(join(directory,'sounds-or-music')):
            print 'Creating "sounds-or-music" folder in %s"' % directory
            makedirs(join(directory,'sounds-or-music'))
        #-------------------------------------------------------------docs
        if not pathExists(join(directory,'Documents')):
            print 'Creating "Documents" folder in %s"' % directory
            makedirs(join(directory,'Documents'))
        #-------------------------------------------------------------Torrents
        if not pathExists(join(directory,'torrents')):
            print 'Creating "torrents" folder in %s"' % directory
            makedirs(join(directory,'torrents'))
        #-------------------------------------------------------------


    def Sort(self,directory):
        #define some paths
        exePath=join(directory,'executables')
        #--------------------------------------------
        imagePath=join(directory,'images')
        #--------------------------------------------
        jarPath=join(directory,'jars')
        #--------------------------------------------
        miscPath=join(directory,'misc')
        #--------------------------------------------
        comPath=join(directory,'compressed')
        #--------------------------------------------
        sndPath=join(directory,'sounds-or-music')
        #--------------------------------------------
        docPath=join(directory,'Documents')
        #begin sorting process
        #--------------------------------------------
        torrentPath=join(directory,'torrents')
        #--------------------------------------------
        
        #exes
        for f in self.executables:
            f=join(directory,f)
            try:
                copy(f,exePath)
                remove(f)
            except IOError,e:
                print str(e)
                print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #images
        for f in self.images:
            f=join(directory,f)
            try:
                copy(f,imagePath)
                remove(f)
            except IOError,e:
                 print str(e)
                 print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #jars
        for f in self.jars:
            f=join(directory,f)
            try:
                copy(f,jarPath)
                remove(f)
            except IOError,e:
                print str(e)
                print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #compressed files
        for f in self.compressed:
            f=join(directory,f)
            try:
                copy(f,comPath)
                remove(f)
            except IOError,e:
                 print str(e)
                 print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #sounds
        for f in self.sounds:
            f=join(directory,f)
            try:
                copy(f,sndPath)
                remove(f)
            except IOError,e:
                 print str(e)
                 print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #documents
        for f in self.docs:
            f=join(directory,f)
            try:
                copy(f,docPath)
                remove(f)
            except IOError,e:
                 print str(e)
                 print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #everything else
        for f in self.misc:
            f=join(directory,f)
            try:
                copy(f,miscPath)
                remove(f)
            except IOError,e:
                print str(e)
                print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------
        #Torrents
        for f in self.torrents:
            f=join(directory,f)
            try:
                copy(f,torrentPath)
                remove(f)
            except IOError,e:
                 print str(e)
                 print 'Error copying %s. Ignoring' % f
            continue
        #--------------------------------------------

if __name__ == '__main__': OrganiserSystem()
