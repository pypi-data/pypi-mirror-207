import requests
import re
import bingImageSpiderCreatedByHanXu as spider
# the_headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'}
# the_url="https://www4.bing.com/images/async?q=%e7%a7%8b%e5%b1%b1%e6%be%aa&first=36&count=35&cw=1177&ch=826&relp=35&datsrc=I&layout=RowBased&apc=0&mmasync=1&dgState=x*132_y*1140_h*183_c*1_i*36_r*7&IG=0C94316B7376496583F4BDEFE386FB3D&SFX=2&iid=images.5554"
# url_xml = requests.get(the_url, headers=the_headers).text
# f1 = open("URL_text.xml", mode="w+",encoding="utf-8")
# f1.write(url_xml)
# # pattern = re.compile('[a-zA-z]+:[^&]*.jpg')
# # url_list = re.findall(pattern=pattern,string=url_xml)
# # f2 = open("image_url.txt", mode="w+", encoding="utf-8")
# # for i in url_list:
# #     f2.write(i)
# #     f2.write("\n")
# #     print(i)
#
# f1.close()
ex=spider.Spider_bing_image()
ex()
