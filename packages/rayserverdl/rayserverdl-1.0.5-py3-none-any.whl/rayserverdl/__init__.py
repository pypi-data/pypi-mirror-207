import aiohttp
import asyncio
import os
import pyshortext
from bs4 import BeautifulSoup
import sys
import time
import platform
from colorama import init, Fore, Style
init()

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

async def make_file(url):
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
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(host + "login") as resp:
            html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')
        csrfToken = soup.find("input", attrs={"name": "csrfToken"})['value']
        #print(csrfToken)
        os.system('cls' if os.name=='nt' else 'clear')
        print(Style.BRIGHT + Fore.BLUE + "Procesando .." + Style.RESET_ALL)
        url_post = host + 'login/signIn'
        payload = {}
        payload["csrfToken"] = csrfToken
        payload["source"] = ""
        payload["username"] = user
        payload["password"] = passw
        payload["remember"] = "1"
        async with session.post(url_post, data=payload) as resp:
            os.system('cls' if os.name=='nt' else 'clear')
            print(Style.BRIGHT + Fore.BLUE + "Procesado" + Style.RESET_ALL)
            await download_file(host,filename,filesize,ids,up_id,session)

async def download_file(host,filename,filesize,ids,up_id,session):
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        print(Style.BRIGHT + Fore.RED + f"{filename}\n" + Style.RESET_ALL)
        chunks = 0
        start_time = time.time()
        f = open("/storage/emulated/0/Download/"+filename, 'wb')
        for id in ids:
            url = f"{host}$$$call$$$/api/file/file-api/download-file?submissionFileId={id}&submissionId={up_id}&stageId=1"
            async with session.get(url,ssl=False,timeout=999999999999) as resp:
                async for chunk in resp.content.iter_chunked(2048):
                    f.write(chunk)
                    chunks+=len(chunk)
                    current_time = time.time()
                    download_speed = chunks / (current_time - start_time)
                    text = f"\r[{convert_speed(download_speed)}] {sizeof_fmt(chunks)} de {sizeof_fmt(filesize)}"
                    print(text, end="|")
        f.close()
    except Exception as ex:
        print(str(ex))

async def main():
    print(Style.BRIGHT + Fore.YELLOW + "Welcome to RayServer.CLi\n" + Style.RESET_ALL)
    url = input("Introduce la URL del archivo que deseas descargar:\n\n> ")
    os.system('cls' if os.name=='nt' else 'clear')
    await make_file(url)
    v = input("Desea realizar otra operación? (y/n):\n> ")
    if v=="y":
        os.system('cls' if os.name=='nt' else 'clear')
        await main()
    else:
        print(Style.BRIGHT + Fore.YELLOW + "Gracias por usar RayServer.Cli" + Style.RESET_ALL)
        sys.exit()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())