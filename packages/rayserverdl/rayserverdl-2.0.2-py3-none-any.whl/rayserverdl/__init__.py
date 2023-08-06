from requests_html import HTMLSession
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pyshortext
from bs4 import BeautifulSoup
import sys
import time
import platform
from colorama import init, Fore, Style
init()

_SESSION = None

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def convert_speed(speed):
    if speed >= 1024 * 1024:
        return f"{speed / (1024 * 1024):.2f} MB/s"
    else:
        return f"{speed / 1024:.2f} KB/s"

def make_file(url):
    global _SESSION
    print(Style.BRIGHT + Fore.BLUE + "Procesando ." + Style.RESET_ALL)
    values = str(url).split('https://rayserver.downloader/')[1].split('/')
    filesize = int(values[0])
    filename = values[3]
    parts = str(pyshortext.unshort(values[2])).split('|')
    ids = str(parts[1]).split(' ')
    data = str(parts[0]).split(' ')
    host = data[0]
    user = data[1]
    passw = data[2]
    up_id = data[3]
    #login
    session = HTMLSession()
    resp = session.get(host + "login",verify=False)
    soup = BeautifulSoup(resp.text, 'html.parser')
    csrfToken = soup.find("input", attrs={"name": "csrfToken"})['value']
    os.system('cls' if os.name=='nt' else 'clear')
    print(Style.BRIGHT + Fore.BLUE + "Procesando .." + Style.RESET_ALL)
    if _SESSION:
        session = _SESSION
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.BRIGHT + Fore.BLUE + "Procesado" + Style.RESET_ALL)
    else:
        url_post = host + 'login/signIn'
        payload = {}
        payload["csrfToken"] = csrfToken
        payload["source"] = ""
        payload["username"] = user
        payload["password"] = passw
        payload["remember"] = "1"
        resp = session.post(url_post, data=payload,verify=False)
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.BRIGHT + Fore.BLUE + "Procesado" + Style.RESET_ALL)
        _SESSION = session
    download_file(host,filename,filesize,ids,up_id,session)

def download_file(host,filename,filesize,ids,up_id,session):
    os.system('cls' if os.name=='nt' else 'clear')
    print(Style.BRIGHT + Fore.RED + f"{filename}\n" + Style.RESET_ALL)
    chunks = 0
    start_time = time.time()
    f = open('/storage/emulated/0/Download/'+filename, 'wb')
    for id in ids:
        try:
            url = f"{host}$$$call$$$/api/file/file-api/download-file?submissionFileId={id}&submissionId={up_id}&stageId=1"
            resp = session.get(url,verify=False)
            for chunk in resp.iter_content(2048):
                f.write(chunk)
                chunks+=len(chunk)
                current_time = time.time()
                download_speed = chunks / (current_time - start_time)
                text = f"\r[{convert_speed(download_speed)}] {sizeof_fmt(chunks)} de {sizeof_fmt(filesize)}"
                print(text, end="")
        except:
            pass

def main():
    print(Style.BRIGHT + Fore.YELLOW + "Welcome to RayServer.CLi\n" + Style.RESET_ALL)
    url = input("Introduce la URL del archivo que deseas descargar:\n\n> ")
    os.system('cls' if os.name=='nt' else 'clear')
    make_file(url)
    v = input("\nDesea realizar otra operación? (y/n):\n> ")
    if v=="y":
        os.system('cls' if os.name=='nt' else 'clear')
        main()
    else:
        print(Style.BRIGHT + Fore.YELLOW + "Gracias por usar RayServer.Cli" + Style.RESET_ALL)
        sys.exit()

main()