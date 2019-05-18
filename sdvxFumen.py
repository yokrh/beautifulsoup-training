# coding: UTF-8
import re
import json
import urllib2
from bs4 import BeautifulSoup

# 各難易度に対してスクレイピング
for i in range(15, 21):
  level = str(i)

  # 譜面サイトからhtmlを取得
  url = "http://www.sdvx.in/sort/sort_" + level + ".htm"
  html = urllib2.urlopen(url)
  soup = BeautifulSoup(html, "html.parser")
  body = str(soup.body)
  # htmlを保存
  f = open(level + ".html" + ".txt", "w")
  f.write(body)
  f.close()

  # htmlから必要なデータを抽出
  f = open(level + ".html" + ".txt", "r")
  flines = f.readlines()
  f.close()
  data = {}
  for fline in flines:
    k = re.search("SORT(.+?)\(\)", fline)
    n = re.search("<!--(.+?)-->", fline)
    if k and n:
      key = k.group(1).lower()
      name = n.group(1)
      ver = key[0:2]
      if "i" in key: ver = "02"
      if "g" in key: ver = "03"
      if "h" in key: ver = "04"
      path = "/" + ver + "/" + key

      value = {
        "id": key,
        "name": name,
        "ver": ver,
        "path": path
      }
      data[key] = value
  # json形式で保存
  jsonstr = json.dumps(data, ensure_ascii=False)
  f = open(level + ".json", "w")
  f.write(jsonstr)
  f.close()
