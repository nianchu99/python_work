import requests
class Spider:

	def __init__(self, url):
		self.__uid = ''
		self.__real_base_url = ''
		self.__base_url = url
		self.__headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
	}
		self.session = requests.Session()


	def set_real_url(self):
		request = self.session.get(self.__base_url, headers=self.__headers)
		real_url = request.url
		self.__real_base_url = real_url[:len(real_url) - len('default2.aspx')]
		return request




mySpider = Spider("https://www.cqut.edu.cn/")
print(mySpider.set_real_url())