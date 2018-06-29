
from get_meta_tags import extractMetas

from flask import request

shareableFolder = "static/share"

def processURL(vidURL, siteURL):
	urlparts = vidURL.split('?');
	vidID = urlparts[1][2:]
	# print 'vid id is :' + vidID
	# print 'site is '+siteURL

	vidImgURL = 'https://img.youtube.com/vi/' + vidID + '/0.jpg'
	print 'vid img link is :' + vidImgURL

	metaTags = extractMetas(vidURL)

	urlToShare = prepareURLfromVidID(vidID, siteURL)

	html = '''
	<html>
	<head>
		<script type="text/javascript" src="../js/pagecontrol.js"></script>
		<script type="text/javascript">
			function caller()
			{
				redirect("''' + vidID + '''");
			}
		</script>
		
		<link rel="canonical" href="''' + urlToShare + '''" />
		<meta property="og:locale" content="en_US" />
		<meta property="og:type" content="article" />
		<meta property="og:title" content="''' + metaTags['title'] + '''" />
		<meta property="og:description" content="''' + metaTags['description'] + '''" />
		<meta property="og:url" content="''' + urlToShare + '''" />
		<meta property="og:site_name" content="ThumbMaximizer" />
		
		<meta property="og:image" content="''' + vidImgURL + '''" />
		<meta property="og:image:secure_url" content="''' + vidImgURL + '''" />
		<meta property="og:image:width" content="1280" />
		<meta property="og:image:height" content="720" />
		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:description" content="''' + metaTags['description'] + '''" />
		<meta name="twitter:title" content="''' + metaTags['title'] + '''" />
		<meta name="twitter:image" content="''' + vidImgURL + '''" />

		<title> Link - ''' + metaTags['title'] + '''</title>

		<meta name="description" content="''' + metaTags['description'] + '''"/>


		<meta itemprop="name" content="''' + metaTags['title'] + '''">

		<meta itemprop="description" content="''' + metaTags['description'] + '''">

		<meta itemprop="image" content="''' + vidImgURL + '''">

		<meta property="og:title" content="''' + metaTags['title'] + '''"/>
		<meta property="og:description" content="''' + metaTags['description'] + '''"/>
		<meta property="og:image" content="''' + vidImgURL + '''"/>
		<meta property="og:image:url" content="''' + vidImgURL + '''"/>
		<meta property="og:image:width" content="470"/>
		<meta property="og:image:height" content="265"/>
		<meta property="og:site_name" content="ThumbMaximizer"/>

		<meta name="twitter:card" content="summary_large_image" />
		<meta name="twitter:site" content="fbshare" />
		<meta name="twitter:title" content="''' + metaTags['title'] + '''" />
		<meta name="twitter:description" content="''' + metaTags['description'] + '''" />
		<meta name="twitter:image" content="''' + vidImgURL + '''"/>

	</head>

	<body onload=caller()>
		<h4>you will be redirected in a few seconds</h4>
		Screenshot
		<img src="''' + vidImgURL + '''">
	</body>

</html>'''
	
	filePath = shareableFolder + '/' + vidID + '.html'
	f= open(filePath,"w")
	f.write(html)
	f.close()


	return vidID



def prepareURLfromVidID(vidID, siteURL):
	print(vidID)
	return siteURL + shareableFolder + "/" + vidID + ".html"