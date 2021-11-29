import os
import requests
import lxml.html
  
from dotenv import load_dotenv
from zippyshare_downloader import Zippyshare

load_dotenv()

z_url = os.getenv('URL')
sub_url_1 = os.getenv('DIV_PART_1')
sub_url_2 = os.getenv('DIV_PART_2')
start = int(os.getenv('START'))
end = int(os.getenv('END'))


z = Zippyshare(verbose=True, progress_bar=True, replace=True)

URLS = []

# requesting url
web_response = requests.get(z_url)


# building
element_tree = lxml.html.fromstring(web_response.text)

for i in range(start,end):
    url = sub_url_1 + str(i) + sub_url_2
    tree_title_element = element_tree.xpath(url)[0]
    (element, attribute, link, pos) = list(tree_title_element.iterlinks())[0]
    print(i, link)
    if (link[0:4] == "http"):
        URLS.append(link)
    else:
        URLS.append("https:" + link)

z.download(URLS)
