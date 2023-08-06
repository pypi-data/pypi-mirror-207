import sys
import os
import yt_dlp
import json
import time
import requests
import calendar
import logging
from ftplib import FTP
from urlparser import urlparser
from fake_useragent import UserAgent
from ttauto_crawler import utils

filename = "mecord_group.txt"
local_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
def ftpClient():
    ftp = None
    try:
        ftp = FTP('192.168.50.113', 'ftpuser', 'ftpuser')
    except:
        ftp = FTP('192.168.3.220', 'xinyu100', 'xinyu100.com')
    if ftp == None:
        raise Exception("no ftp!")
    return ftp

def groupConfig():
    ftp = ftpClient()
    ftp.cwd("mecord/")
    file_list = ftp.nlst()
    if len(file_list) > 0:
        with open(local_file, 'wb') as f:
            ftp.retrbinary('RETR ' + filename, f.write)
    else:
        with open(local_file, 'w') as f:
            json.dump({}, f)
    ftp.quit()
    
    with open(local_file, 'r') as f:
        data = json.load(f)
    return data

def saveGroupConfig(data):
    ftp = ftpClient()
    ftp.cwd("mecord/")
    file_list = ftp.nlst()
    with open(local_file, 'w') as f:
        json.dump(data, f)
    with open(local_file, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file)
    ftp.quit()

def downloadFile(content_type, name, url, downloadDir):
    timeoutDuration = 3600
    ext = ".mp4"
    # content_type 
    # 1=图片
    # 2=视频
    # 3=音频
    # 4=文字
    if content_type == 1:
        timeoutDuration = 60
        ext = ".jpg"
    savePath = os.path.join(downloadDir, f"{name}{ext}")
    if os.path.exists(savePath):
        os.remove(savePath)
    #download
    requests.adapters.DEFAULT_RETRIES = 2
    s = requests.session()
    s.keep_alive = False
    s.headers.update({'Connection':'close'})
    ua = UserAgent()
    download_start_pts = calendar.timegm(time.gmtime())
    file = s.get(url, verify=False, headers={'User-Agent': ua.random}, timeout=timeoutDuration)
    time.sleep(1)
    with open(savePath, "wb") as c:
        c.write(file.content)
    download_end_pts = calendar.timegm(time.gmtime())
    logging.info(f"download duration={(download_end_pts - download_start_pts)}")
    s.close()

def requestMecord(downloadDir, curGroupId, mecord_group, start_id, request_size = 30):
    param = {
        "group_id": mecord_group,
        "start_id": start_id,
        "size": request_size
    }
    requested_start_id = start_id
    s = requests.session()
    s.keep_alive = False
    s.headers.update({'Connection':'close'})
    res = s.get("https://mecord-beta.2tianxin.com/proxymsg/crawler/post_list", params=param, verify=False)
    if res.status_code == 200 and len(res.content) > 0:
        data = json.loads(res.content)
        if data["code"] == 0:
            post = data["body"]["post"]
            max_id = data["body"]["max_id"]
            idx = start_id
            requested_start_id += len(post)
            for it in post:
                # content_type 
                # 1=图片
                # 2=视频
                # 3=音频
                # 4=文字
                if it["content_type"] == 1 or it["content_type"] == 2:
                    name = it["content"]
                    for it_url in it["content"]:
                        downloadFile(it["content_type"], f"{curGroupId}_{idx}", it_url, downloadDir)
                        idx += 1
            if requested_start_id < max_id:
                size = request_size
                if max_id - requested_start_id < request_size:
                    size = max_id - requested_start_id
                requestMecord(downloadDir, curGroupId, mecord_group, requested_start_id, size)
    return requested_start_id

def download(url, curGroupId, downloadDir):
    urldata = urlparser.urlparse(url)
    mecord_groups = urldata.hostname.split(",")
    groupCacheConfig = groupConfig()
    for g in mecord_groups:
        s = requests.session()
        s.headers.update({'Connection':'close'})
        start_id = 0
        if g in groupCacheConfig:
            start_id = groupCacheConfig[g]
        new_start_id = requestMecord(downloadDir, curGroupId, g, start_id)
        groupCacheConfig[g] = new_start_id
    saveGroupConfig(groupCacheConfig)

# https://mecord-beta.2tianxin.com/proxymsg

# download("mecord://100212", 0, "C:\\Users\\123\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\ttauto_crawler\\.download\\0")
#获取youtube外部数据, 爬取到mecord里
# https://alpha.2tianxin.com/common/admin/mecord/get_auto_crawler
# 更新mecord里的group信息，可以创建新的group
# # https://alpha.2tianxin.com/common/admin/mecord/update_auto_crawler
# # https://mecord-beta.2tianxin.com/proxymsg/crawler/create_group


#爬取mecord里的数据
#https://mecord-beta.2tianxin.com/proxymsg/crawler/post_list?group_id=100212&start_id=0&size=20

