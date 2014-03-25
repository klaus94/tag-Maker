#!/ usr/binenv python
# -*- coding : utf -8 -*-

#This program should edit the meta-data of a mp3, which is in the same directory
#It takes the name of the file and gives the metadata a title and an artist
#possible tags: COMM TCMP TPE1(artist) TDRC TIT2(titel) TENC TRCK COMM TPOS TALB(album) COMM COMM TCON UFID

#unfortunately the program does not move the files to a certaint directory yet :/				 	    				   	 

#Imports:
import sys
import os
from mutagen.id3 import ID3, TRCK, TIT2, TPE1, TALB, TDRC, TCON, COMM

#get right direction:
if (len(sys.argv) > 1):
    fpath = sys.argv[1]
else:
    fpath = os.path.abspath(os.path.dirname(sys.argv[0]))	#print os.listdir(fpath)

for fn in os.listdir(fpath):
	fname = os.path.join(fpath, fn)
	if fname.lower().endswith('.mp3'):		#print fn - songname
	
		#get name of the song (filename) and split it up into title and artist
		print "extracting artist and title ..."
		os.system("sleep 1")
		name = fn.replace("_"," ")				#delete "_" from title
		content = name.split(" - ")			#print content - [artist, titel.mp3]
		artist = content[0]					#get Artist
		artist.replace(" _ ", "")			#delete "_" from artist
		title = content[1].strip(".mp3")	#get title (delete '.mp3')
		title.replace(" _ ","")				#delete " _ " from title

		#make screenshot
		print "make a photo!!!"
		os.system("import screenshot.png")
		os.system("sleep 5")

		#make audio-object from current song and add tags
		print "set tags to the right values ..."
		os.system("sleep 1")
		audio = ID3(fname)
		audio.add(TIT2(encoding=3, text=title))
		audio.add(TPE1(encoding=3, text=artist))
		audio.add(
			APIC(
				encoding=3, # 3 is for utf-8
				mime='image/png', # image/jpeg or image/png
				type=3, # 3 is for the cover image
				desc=u'Cover (front)',
				data=open('screenshot.png').read()
			)
		)
		audio.save()
		
		#move title to /home/...
		print "sending " + fn + " to home/ ..."
		os.system("sleep 1")
		sendTitle = fn.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")	#identify special characters
		fname = os.path.join(fpath, sendTitle)
		os.system("mv " + fname + " /home/")
		
		#remove screenshot
		os.system("rm screenshot.png")

		#Informationen
		os.system("sleep 1")
		print "all tasks were successfully finished :)"
		os.system("sleep 2")
