import json, requests
res = requests.get('https://developer.apple.com/videos/play/wwdc2016/')
video_data = json.loads(res.text)
obj_final = {}
for val in video_data:
    if val['year'] == 2016:
	if val.values() == '':
	    null_obj = None
	    obj_final.update(null_obj)
	    print "Video content for 2016 if null : ",obj_final
	else:
	    print "Video content for 2016 : ",vals

# Clone the repositary
# To run the script - python test.py
# Here I have written the code how we can make it for sudo code, Kindly check for the same.
