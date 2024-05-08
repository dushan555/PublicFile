import requests
import re
import os


url = "https://mirror.ghproxy.com/https://raw.githubusercontent.com/Fairy8o/IPTV/main/DIYP-v4.txt"
r = requests.get(url)
open('iptv.txt', 'wb').write(r.content)
