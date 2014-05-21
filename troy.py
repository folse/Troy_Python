import json
import time
import urllib
import urllib2
import cookielib
import sys   
sys.setrecursionlimit(1000000)

def reservation(resultArray):
	for x in xrange(0,len(resultArray)):
		car_num = resultArray[x]['CNBH']
		reservation_params = car_num + '.' + reservation_date + '.' + want_type + '.'
		reservation_request_data = urllib.urlencode({'xxzh':'51137361','jlcbh':'','isJcsdYyMode':'5','trainType':'','zip':'false','osname':'android','params':reservation_params})
		print time.time()
		print opener.open(reservation_request_url,reservation_request_data).read()

def get_car():
	car_request_url = 'http://haijia.bjxueche.net:8001/KM2/ClYyCars2'
	car_request_data = urllib.urlencode({'filters[jlcbh]':'','filters[xxzh]':'51137362','filters[trainType]':'','zip':'false','osname':'android','filters[xnsd]':want_type,'filters[yyrq]':want_date}) 
	running = True
	try:
		while running:
			resp = opener.open(car_request_url,car_request_data, timeout = 3).read()
			print time.time() 
			resp_json = json.loads(resp)
			data = resp_json['data']
			resultArray = data['Result']
			if len(resultArray) > 0:
				running = False
	except:
		print 'exception'
		get_car()

	reservation(resultArray)
	get_car()
		
if __name__ == '__main__':

	want_type = '15'
	want_date = '2013/12/28'
	
	print want_type
	print want_date

	reservation_date = want_date.replace('/','-');
	reservation_request_url = 'http://haijia.bjxueche.net:8001/KM2/ClYyAddByMutil'

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	login_url = r'http://haijia.bjxueche.net:8001/System/Login'	
	login_data = urllib.urlencode({'username':'bjcsxq','password':'bjcsxq2012'})  
	opener.open(login_url,login_data).read()
	get_car()
