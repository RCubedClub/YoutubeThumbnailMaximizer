
shareableFolder = "static/share"

def processURL(vidURL):
	urlparts = vidURL.split('?');
	vidID = urlparts[1][2:]
	# print 'vid id is :' + vidID

	vidImgURL = 'https://img.youtube.com/vi/' + vidID + '.jpg'
	print 'vid img link is :' + vidImgURL

	

	return '1'



def prepareURLfromVidID(vidID):
	print(vidID)
	return "." + "/" + shareableFolder + "/" + vidID + ".html"