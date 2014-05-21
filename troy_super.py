import json
import time
import urllib
import urllib2
import cookielib

def reservation():
	resultArray = ['08206','08263','08258','08257','08236','08176','08153','08219','08217','08149','08145','08131','08121','08082','08111','08042','08018','08014']
	again = True
	for x in xrange(0,len(resultArray)):
		car_num = resultArray[x]
		reservation_params = car_num + '.' + reservation_date + '.' + want_type + '.'
		reservation_request_data = urllib.urlencode({'xxzh':'YOUR_ID','jlcbh':'','isJcsdYyMode':'5','trainType':'','zip':'false','osname':'android','params':reservation_params})
		raw_ret_json = opener.open(reservation_request_url,reservation_request_data).read()
		print raw_ret_json
		reservation_resp_json = json.loads(raw_ret_json)
		if reservation_resp_json['code'] == 0:
			again = False
			pass
	if again:
		print 'again'
		reservation()
		
		
if __name__ == '__main__':

	want_type = '812'
	want_date = '2013/12/29'

	reservation_date = want_date.replace('/','-');
	print want_type
	print want_date
	reservation_request_url = 'http://haijia.bjxueche.net:8001/KM2/ClYyAddByMutil'

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #url = r'http://haijia.bjxueche.net:8001/System/Login?username=bjcsxq&password=bjcsxq2012'
	login_url = r'http://haijia.bjxueche.net:8001/System/Login'	
	login_data = urllib.urlencode({'username':'bjcsxq','password':'bjcsxq2012'})  
	print opener.open(login_url,login_data).read()
	reservation()
	
