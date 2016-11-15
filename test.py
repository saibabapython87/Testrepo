import json, requests
res = requests.get('https://developer.apple.com/videos/play/wwdc2016/')
video_data = json.loads(res.text)
for val in video_data:
    if val['year'] == 2016:
	if val.values() == '':
	    print val.update
            print "Video content for 2016 : ",vals
	

