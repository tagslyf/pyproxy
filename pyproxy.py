import pprint, re, requests, socket
from lxml import etree
from requests.packages.urllib3.poolmanager import PoolManager
from urllib import request, parse


"""
	Script that will scrap http://www.xicidaili.com/nn/1
	for ip and port to check if proxy is working or not
"""


# url = "http://my-ip.herokuapp.com/"
# s = requests.session()

# html = s.get(url)
# print(html, html.content)

# headers = {
# 	'User-agent': 'Mozilla/5.0', 
# 	'referer': ''
# }
# s.cookies.clear()
# s.close()

# s = requests.session()
# proxy = '122.72.32.72:80'
# proxies = {
# 	'http' : 'http://{}'.format(proxy),
# 	'https' : 'https://{}'.format(proxy),
# 	'ftp' : proxy
# }

# html = s.get(url, headers=headers, proxies=proxies)
# html = s.get(url)
# print(html, html.content, "PROXIES: {}".format(proxies))
# s.cookies.clear()
# s.close()

# socket.setdefaulttimeout(180)

# url = "http://my-ip.herokuapp.com/"
# r = request.Request(url)
# sock = request.urlopen(r)
# print(sock.read())

# s = requests.session()

# headers = {
# 	'User-agent': 'Mozilla/5.0', 
# 	'referer': ''
# }

# 'http://spys.ru/free-proxy-list/PH/'
#  html.xpath("//font[@class='spy14']")
# html = s.get('http://proxylist.hidemyass.com/', headers=headers)
# html = s.get('http://www.gatherproxy.com/proxylist/country/?c=Philippines', headers=headers)
# html_tree = etree.HTML(html.content)
# proxys = [
# 	'112.199.65.190:3128',
# 	'120.28.45.202:8090',
# 	'112.119.79.106:8080',
# 	'120.72.26.131:8080',
# 	'43.250.227.94:8080',
# 	'146.88.71.67:8080',
# 	'203.160.172.163:8090',
# 	'202.57.48.102:80',
# 	'122.54.20.214:8090',
# 	'49.150.107.185:80',
# 	'112.199.79.106:8080'
# ]

# print(html_tree.xpath("//table[@id='listable']/tbody"))

# for trs in html_tree.xpath("//table[@id='listable']/tbody"):
# 	for i, tr in enumerate(trs):
# 		print(tr)
# 		for td in tr:
# 			print(td, td.text)

# for i, tr in enumerate(html_tree.xpath("//table[@id='listable']/tr")):
# 	print(i, tr, tr[1].text, tr[2].text)

# s.cookies.clear()
# s.close()

# user_agents = ['Mozilla/5.0', '(Windows NT 6.1; Win64; x64)', 'AppleWebKit/537.36', '(KHTML, like Gecko)', 'Chrome/55.0.2883.87', 'Safari/537.36']
# proxys = [
# 	'122.54.3.171:45554',
# 	'122.53.178.100:1080'
# ]
# print(59, html_tree.xpath("//table[@id='tblproxy']/tbody"))
# for i, tr in enumerate(html_tree.xpath("//table[@id='tblproxy']")):
# 	# print(i, tr, tr[1].text, tr[2].text)
# 	for td in tr:
# 		print(63, td.text.strip())
	
# print(proxys)
# s.cookies.clear()
# s.close()

# def is_bad_proxy(ip_port):    
# 	try:
# 		proxy_handler = request.ProxyHandler({'http': ip_port})
# 		opener = request.build_opener(proxy_handler)
# 		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# 		request.install_opener(opener)
# 		req = request.Request('http://www.google.com')  # change the url address here
# 		sock = request.urlopen(req)
# 	except request.HTTPError as e:
# 		print('Error code: {}'.format(e.code))
# 		return e.code
# 	except Exception as detail:
# 		print("ERROR: {}".format(detail))
# 		return 1
# 	return 0

# for i in proxys:
# 	oks = True
# 	print("Checking {}".format(i))
# 	try:
# 		proxy_handler = request.ProxyHandler({'http': i})
# 		opener = request.build_opener(proxy_handler)
# 		opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# 		request.install_opener(opener)
# 		req = request.Request('http://my-ip.herokuapp.com/')  # change the url address here
# 		sock = request.urlopen(req)
# 		print("{} is working".format(i), sock.getcode())

# 		# proxy_handler = request.ProxyHandler({'http': i})
# 		# opener = request.build_opener(proxy_handler)
# 		# opener.addheaders = [('User-agent', 'Mozilla/5.0'), ('Referer', '')]
# 		# request.install_opener(opener)
# 		# accounts = [
# 		# 	('mmkronald', '123qwe!!'),
# 		# 	('mmktest00', '123qwe!!'),
# 		# 	('mmktest01', '123qwe!!'),
# 		# 	('mmktest02', '123qwe!!'),
# 		# ]
# 		# headers = {
# 		# 	'User-agent': 'Mozilla/5.0', 
# 		# 	'referer': ''
# 		# }
# 		# url = 'https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F'
# 		# for account in accounts:
# 			# data = {
# 			# 	'username': account[0].strip(),
# 			# 	'password': account[1].strip()
# 			# }
# 			# proxys = {
# 			# 	'http': 'http://{}'.format(i),
# 			# 	'https': 'https://{}'.format(i),
# 			# 	'ftp': '{}'.format(i),
# 			# }


# 			# html = requests.post(url, data, headers = headers, proxies=proxys)
# 			# html_tree = etree.HTML(html.content)
# 			# print(html, i, html.status_code, data, html_tree.xpath("//div[@class='dropdown-footer']"), html_tree.xpath("//div[@class='captcha']"))
# 	except request.HTTPError as e:
# 		oks = False
# 		print('{} Error code: {}'.format(i, e.code))
# 	except Exception as detail:
# 		oks = False
# 		print("{} ERROR: {}".format(i, detail))

# 	if oks:
# 		print("REQUESTING FOR {}".format(i))
# 		# data = {
# 		# 	'username': 'mmkronald',
# 		# 	'password': '123qwe!!'
# 		# }
# 		# data = parse.urlencode(data)
# 		# data = data.encode('ascii')

# 		# req = request.Request('https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F', data=data)
# 		# sock = request.urlopen(req)
# 		# print(sock.read())

# 		accounts = [
# 			('mmkronald', '123qwe!!'),
# 			('mmktest00', '123qwe!!'),
# 			('mmktest01', '123qwe!!'),
# 			('mmktest02', '123qwe!!'),
# 		]
# 		# headers = {
# 		# 	'User-agent': 'Mozilla/5.0', 
# 		# 	'referer': ''
# 		# }
# 		# url = 'https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F'
# 		# for account in accounts:
# 		# 	# data = {
# 		# 	# 	'username': account[0].strip(),
# 		# 	# 	'password': account[1].strip()
# 		# 	# }
# 		# 	# data = parse.urlencode(data)
# 		# 	# data = data.encode('ascii')

# 		# 	req = request.Request(url)
# 		# 	with request.urlopen(req) as response:
# 		# 		print(response.read())

# 		# url = 'http://my-ip.herokuapp.com/'
# 		url = 'https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F'
# 		# url = 'http://httpbin.org/ip'
# 		xheaders = {
# 			'User-agent': 'Mozilla/5.0', 
# 			'referer': ''
# 		}
# 		proxys = {
# 			'http': 'http://{}'.format(i),
# 		}
# 		for account in accounts:
# 			data = {
# 				'username': account[0],
# 				'password': account[1]
# 			}
			
# 			s = requests.session()
# 			html = s.post(url, data=data, headers=xheaders)
# 			html_tree = etree.HTML(html.content)
# 			print("XPROXY", html, i, html.status_code, data, html_tree.xpath("//div[@class='dropdown-footer']"), html_tree.xpath("//div[@class='captcha']"))
# 			s.cookies.clear()
# 			s.close()

# 			for user_agent in user_agents:
# 				try:
# 					wheaders = {
# 						'User-agent': user_agent
# 					}
# 					html = s.post(url, data=data, headers=wheaders, proxies=proxys)
# 					html_tree = etree.HTML(html.content)
# 					print("WPROXY", html, i, html.status_code, data, wheaders, html_tree.xpath("//div[@class='dropdown-footer']"), html_tree.xpath("//div[@class='captcha']"))
# 					s.cookies.clear()
# 					s.close()
# 				except Exception as e:
# 					print("WPROXY", i, e)

# 				if html_tree.xpath("//div[@class='dropdown-footer']"):
# 					break
# 		# break
# 		# if is_bad_proxy(i):
# 		# 	print("{} bad proxy.".format(i))
# 		# else:
# 		# 	print("{} is working".format(i))
# # r = request.Request('https://www.xicidaili.com/nn/1')
# # sock = request.urlopen(r)
# # html = sock.read()
# # print(html)
# # html_tree = etree.HTML(html.content)

url = "http://httpbin.org/ip"
response = requests.get(url)
print(response.text)

socket.setdefaulttimeout(180)
user_agents = [
	'Mozilla/5.0', 
	'(Windows NT 6.1; Win64; x64)', 
	'AppleWebKit/537.36', 
	'(KHTML, like Gecko)', 
	'Chrome/55.0.2883.87', 
	'Safari/537.36'
]
accounts = [
	('mmkronald', '123qwe!!'),
	('mmktest00', '123qwe!!'),
	('mmktest01', '123qwe!!'),
	('mmktest02', '123qwe!!'),
]

# Get proxy
proxys = []
# url = "https://www.sslproxies.org/"
# url = "http://www.xicidaili.com/nn/"
url = "http://haoip.cc/tiqu.htm"
headers = {
	'User-agent': user_agents[0]
}
response = requests.get(url, headers=headers)
# html_etree = etree.HTML(response.content)
# proxys = ["{}:{}".format(tr[1].text, tr[2].text) for index, tr in enumerate(html_etree.xpath("//table[@id='ip_list']/tr"))][1:]
proxys = [ip.strip() for ip in re.findall(r'r/>(.*?)<b', response.text, re.S)]
proxy_good_counter = 0
print(proxys)

for proxy in proxys:
	print("CHECKING FOR {}".format(proxy))
	oks = True

	try:
		# proxy_handler = request.ProxyHandler({'http': proxy})
		# opener = request.build_opener(proxy_handler)
		# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
		# request.install_opener(opener)
		# req = request.Request('http://httpbin.org/ip')  # change the url address here
		# sock = request.urlopen(req)
		# print("{} is working".format(proxy), sock.getcode())

		url = 'http://httpbin.org/ip'
		s = requests.session()
		headers = {
			'User-agent': user_agents[0]
		}
		proxies = {
			'http': 'http://{}'.format(proxy),
			'https': 'https://{}'.format(proxy),
			'ftp': '{}'.format(proxy),
		}
		response = s.get(url, headers=headers, proxies=proxies, timeout=180)
		proxy_good_counter += 1
		print("{} is working".format(proxy), response, response.content if response.status_code == 200 else '')

	except request.HTTPError as e:
		oks = False
		print('{} Error code: {}'.format(proxy, e.code))
	except Exception as detail:
		oks = False
		print("{} ERROR: {}".format(proxy, detail))

print("{}/{} proxy checked.".format(proxy_good_counter, len(proxys)))
	
	# if oks:
	# 	print("REQUESTING FOR {}".format(proxy))

	# 	url = 'https://imgur.com/signin?redirect=http%3A%2F%2Fimgur.com%2F'

	# 	for account in accounts:
	# 		data = {
	# 			'username': account[0],
	# 			'password': account[1]
	# 		}

