from urllib.request import urlopen
from bs4 import BeautifulSoup
import bs4
from urllib.parse import urljoin
import requests
import urllib

session = requests.Session()
ofptr = open("electric_dataset.txt", "a+", encoding="cp949")

default_url = "http://www.11st.co.kr"
m_url = "/product/SellerProductDetail.tmall?method=getProductReviewList&prdNo=2378728074&page=1&pageTypCd=first&reviewDispYn=Y&isPreview=false&reviewOptDispYn=Y&optSearchBtnAndGraphLayer=Y&reviewBottomBtn=Y&openDetailContents=Y&pageSize=10&isIgnoreAuth=false&lctgrNo=1001428&leafCtgrNo=0&groupProductNo=0&groupFirstViewPrdNo=0&selNo=45084215"

html = urlopen(default_url + m_url)
bsObject = BeautifulSoup(html, "html.parser")

form = bsObject.find("form", id="pageForm")
fields = form.findAll('input')

form_data = dict((field.get('name'), field.get('value')) for field in fields)
post_url = urljoin(default_url, form['action'])

for page_num in range(1, 10):
    form_data['page'] = page_num
    data = urllib.parse.urlencode(form_data)
    req = urllib.request.Request(post_url, data.encode(encoding='cp949'))
    response = urllib.request.urlopen(req)
    filter_bsObject = BeautifulSoup(response, "html.parser")

    reviewCon = filter_bsObject.findAll("a", id="reviewContTxt")
    for review in reviewCon:
        str_data = "0\t"
        str_data += review.contents[0].strip()
        str_data += "\t\n"
        ofptr.write(str_data)

ofptr.close()
