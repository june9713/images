
from bs4 import BeautifulSoup
import bs4
import flask

# Network 및 HTTP 요청:
import urllib
import urllib.parse
import requests
import urllib3
from requests_toolbelt import MultipartEncoder
import requests_toolbelt
from PySide6.QtWidgets import QMessageBox,QApplication
# Image Processing:
import PIL
from PIL import Image
import numpy
import cv2
# Cryptography:
import cryptography
from cryptography.fernet import Fernet as fxnetwork

# Data Processing:
import json , copy
import glob
import xml.etree.ElementTree as ET
import xml
import pickle
import ctypes
import pynput
import mss
import socket
import subprocess
import io
import shutils,base64,os,traceback
import datetime
from github import Github


def mkhdr(hds):
    x = {}
    for hd in hds.strip().split("\n"):
        if len(hd.strip()) > 0:
            tmp = hd.split(":")
            key = tmp[0].strip()
            data = ":".join(hd.split(":")[1:]).strip()
            x[key] = data
    return x       



def lsitOfFilesOnGithub(key ="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"  , githubname = "june9713" , reponame ="images" , folderpath ="links" ):
    # GitHub 토큰 또는 username, password를 사용하여 객체 생성
    g = Github(key)

    # "aa"라는 리포지토리를 찾습니다.
    repo = g.get_repo(f"{githubname}/{reponame}")

    # "bb" 폴더 내의 모든 컨텐츠를 가져옵니다.
    contents = repo.get_contents(folderpath)

    # 폴더와 파일 목록을 출력합니다.
    results = []
    for content in contents:
        results.append(content.name)
    return results


def getVersion(key ="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"  , githubname = "june9713" , reponame ="images" ):
    versions = lsitOfFilesOnGithub(key , githubname , reponame , "/deadpool/executable")
    newversion = max(versions)
    return newversion


def updateServerFunc(xpkxkky):
    try:
        pys = glob.glob("./pys/n_*.py")
        print("pys"  ,len(pys))
        if len(pys) == 0:
            newv = getVersion()
            if os.path.isfile("./datas/version.pkl") :
                with open("./datas/version.pkl" , "r") as f:
                    v = f.read().strip()
            else:
                v = "0"
            
            if newv != v:
                app = QApplication([])
                # QMessageBox 생성 및 설정
                QMessageBox.information(None, "업데이트가 시작됩니다", "잠시만 기다려 주세요")
                #app.exec_()
                print("???")
                updatefiles = lsitOfFilesOnGithub(folderpath= "/deadpool/executable/" + newv)
                try:
                    os.mkdir("./tmp")
                except:
                    pass
                try:
                    os.mkdir("./tmp/download")
                except:
                    pass
                removefiles = glob.glob("./tmp/download/*.*")
                for rmf in removefiles:
                    try:
                        os.remove(rmf)
                    except:
                        pass
                
                githubhdr = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'''
                for file in sorted(updatefiles):
                    addr = "https://raw.githubusercontent.com/june9713/images/main/deadpool/executable/" + newv + "/" + file
                    r = requests.get(addr , headers = mkhdr(githubhdr) )
                    with open("./tmp/download/" + file, "wb") as f:
                        f.write(r.content)  
                updatefile  = list(sorted(updatefiles))
                
                subprocess.Popen([os.path.abspath('./tmp/download/updater.exe') , os.path.abspath(os.getcwd())  ,updatefile[0] , newv], start_new_session=True)
                
            
        serverAddress = 'http://183.97.32.52:9699'
        try:
            os.mkdir('./adb')
        except:
            pass
            
        print("update!")
        updateServer = None
        print("progrma started")
        check = False
        if os.path.isfile("./datas/server.inx"):
            with open("./datas/server.inx" , "r" , encoding="utf8") as f:
                updateServer = f.read().strip()
        else:
            updateServer = 'http://183.97.32.52:9699/updatecheck/'
            
        adbaddr = "http://" + updateServer.split("//")[1].split("/")[0] + "/getadb/"
            
        print("updateServer"  ,updateServer)
            
        if os.path.isdir("./pys"):
            pathhead = "./example"
            
        else:
            pathhead = "."
        print("pathhead"  ,pathhead)
        #for userv in updateServer.split("\n"):
        userv = updateServer.split("\n")[0].strip()
        addr = userv
        cipsit131 = fxnetwork(xpkxkky)
        tmptime = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H:%M:%S").encode()
        cipxx131_text = cipsit131.encrypt(tmptime)  # 암호화된 문자열
        datastr = cipxx131_text
        json_data = {"data": cipxx131_text.decode("utf-8")}     
        try:
            r = requests.post(addr , json = json_data , timeout = 3 , verify=False)
            cipsit131 = fxnetwork(xpkxkky)
            code = cipsit131.decrypt(json.loads(r.content)['response']) 
            
            filesDecoded = json.loads(code)
            for finfo in filesDecoded:
                ftmppath = pathhead + finfo
                print("finfo"  ,ftmppath)
                fdata = filesDecoded[finfo]
                fdataDecoded = base64.b64decode(fdata)
                try:
                    if os.path.isdir(os.path.dirname(ftmppath)) == False:
                        os.makedirs(os.path.dirname(ftmppath))
                except:
                    pass
                try:
                    with open(ftmppath , "wb") as f:
                        f.write(fdataDecoded)
                except:
                    pass
            
            httpstype = addr.split("//")[0]
            serverAddress = httpstype + "//" +  userv.split("//")[1].split("/")[0]
            check = True
            print("update complete!")
        
        except:
            print(traceback.format_exc())
        
        try:
            print(">>?>0")
            if os.path.isfile("./adb/adb.exe") == False:
                r2 = requests.post(adbaddr, json = json_data , timeout = 3 , verify=False)
                cipsit131 = fxnetwork(xpkxkky)
                print("r2.content" , r2.content)
                code = cipsit131.decrypt(json.loads(r2.content)['response']) 
                print(">>?>1")
                filesDecoded = json.loads(code)
                if os.path.isdir("./pys"):
                    pathhead = "./example/adb"
                else:
                    pathhead = "./adb"
                for finfo in filesDecoded:
                    ftmppath = pathhead + finfo
                    pass#print("finfo"  ,ftmppath)
                    fdata = filesDecoded[finfo]
                    fdataDecoded = base64.b64decode(fdata)
                    print("fdataDecoded" , ftmppath , fdataDecoded)
                    try:
                        if os.path.isdir(os.path.dirname(ftmppath)) == False:
                            os.makedirs(os.path.dirname(ftmppath))
                    except:
                        print(traceback.format_exc())
                    try:
                        with open(ftmppath , "wb") as f:
                            f.write(fdataDecoded)
                    except:
                        print(traceback.format_exc())
                print(">>?>3")

            
        except:
            print(traceback.format_exc())
            
            
                    
                    
        return serverAddress ,updateServer
    except:
        print(traceback.format_exc())