import sys
import subprocess
import requests
import time
import threading
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def request(url):
    #print(url)
    max_t = 3
    for i in range(0, max_t):
        try:
            response = requests.head(url, verify=False, timeout=5)
            return response.status_code

        except Exception as err:
#        if sys.argv[2] == 's':
#            print(err)
#            exit()
            try:
                requests.head("https://www.google.com/", timeout=5)
                if i < max_t:
                    time.sleep(1)
                    continue
            except:
                if i < max_t:
                    
                    #beep or notify me the connection is gone
                    #(stop program until connecion is back)
                    while True:
                        try:
                            requests.head("https://www.google.com/", timeout=3)
                            break
                        except:
                            subprocess.getoutput("play -n synth 0.3 sin 1000")
                            time.sleep(2)
                            #continue

    return 0

def write(line, code=200):
    print(f"{line} => {code} \t\t\t ")
    print()
    if _write:
        with open(output_file_path, 'a') as output_file:
            output_file.write(line+'\n')
        output_file.close()

print("start dirsearch tool")

path = "/sdcard/download/dirs.txt"
if '-api' in sys.argv:
    path = "/sdcard/download/Wordlist/api-endpoints.txt"
    print("You choose API Endpoints list")

for i in sys.argv:
    if i.startswith("-w:"):
        path = i.split(":", 1)[1]
        break

output_file_path = "/sdcard/dirsearch_200.txt"
url = sys.argv[1] 

for i in sys.argv:
    if "-h" in i:
        print("\nUSAGE:\n")
        print("python dirsearch.py <url> [-start -code -ext -nex -w -exclude -exc -t -find -nofind -all -no -api]")
        print("<-start:int> \t\t resume from number")
        print("<-code:int> \t\t Status code to be shown alongside with 200")
        print("<-ext:str or list> \t Extension to be chosed (will use this list only in scan)")
        print("<-nex:str> \t\t replace extention with yours (like php with jsp)")
        print("<-w:path> \t\t wordlist path to use")
        print("<-exclude:str> \t\t Exclude Extension from wordlist (like server reject 'php')")
        print("<-exc:int> \t\t Exclude Status Code To Be Shown")
        print("<-t:float> \t\t Time between requests default=0")
        print("<-find:str> \t\t find And Include Those In Wordlist")
        print("<-nofind:str> \t\t Don't Include Those In Wordlist")
        print("-all \t\t\t show all status_code except 404")
        print("-no \t\t\t no write in log file")
        print("-api \t\t\t use special default api wordlist")
        print()
        print("Ex: python dirsearch.py http://example.com/ -s:400 -code:403 -ext:.js,.php,.json -exclude:html -no")
        sys.exit()
        
if "-no" in sys.argv:
    _write = False
else:
    _write = True

try:
    for i in sys.argv:
        if i.startswith("-exclude:"):
            exclude = i.split(":", 1)[1]
            break
    exclude
except:
    exclude = None

try:
    for i in sys.argv:
        if i.startswith("-start:"):
            start = i.split("-start:")[1]
            start = int(start)
            break
    start
except:
    start = 0

try:
    for i in sys.argv:
        if i.startswith("-code:"):
            user_code = i.split(":", 1)[1]
            user_code = int(user_code)
            break
    user_code
except:
    user_code = 0

try:
    for i in sys.argv:
        if i.startswith("-ext:"):
            ext = i.split(":", 1)[1]
            if "," in ext:
                ext = ext.split(",")
                ext = [i for i in ext if i]
            break
    ext
except:
   ext = None

if ext:
    try:
        for i in sys.argv:
            if i.startswith("-nex:"):
                nex = i.split("-nex:")[1]
                break
        nex
    except Exception as err:
        nex = None
        print(err)
else:
    nex = None

try:
    for i in sys.argv:
        if i.startswith("-find:"):
            find = i.split("-find:")[1]
            break
    find
except:
    find = None

try:
    for i in sys.argv:
        if i.startswith("-nofind:"):
            nofind = i.split("-nofind:")[1]
            break
    nofind
except:
    nofind = None

try:
    for i in sys.argv:
        if i.startswith("-exc:"):
            exc = int(i.split(":")[1])
            break
    exc
except:
    exc = None

try:
    for i in sys.argv:
        if i.startswith("-t:"):
            sec = float(i.split("-t:")[1])
            break
    sec
except:
    sec = None

if url.endswith("="):
    pass
else:
    if not url.endswith("/"):
        url += "/"
print(url)

if '-all' in sys.argv:
    print("All Status Code Except 404")

if "-no" in sys.argv:
    print("No Write is Enable")

if sec:
    print(f"Sleep Set To {sec}")

if exc:
    print(f"Exclude Status Code {exc}")

if nex:
    print(f"Replace '{ext}' with '{nex}'")

if find:
    print(f"Include '{find}' On Search")

if nofind:
    print(f"Do Not Include '{nofind}' On Search")

with open(path) as file:
    data1 = file.read().split('\n')
    file.close()
    data = []

    if ext:
        if type(ext) == list:
            for ex in ext:
                for i in data1:
                    if i.endswith(ex):
                        data.append(i)
        else:
            data = [i for i in data1 if i.endswith(ext)]
    else:
        data = [i for i in data1]

    if find:
        data1 = data
        data = [i for i in data1 if find in i]

    if nofind:
        data1 = data
        data = [i for i in data1 if nofind not in i]

    if exclude:
        data1 = data
        data = [i for i in data1 if exclude not in i]

    if nex:
        data1 = data
        data = [i.replace(ext,nex) for i in data1]

    del data1
    data = data[start:]
    print(f"found {len(data)}")
    #print(data)
    for i, dir in enumerate(data):
        i += start
        line = url + dir.strip()
        #print(line)
        time.sleep(0.01)
        code = request(line)
#        if exc:
#            if code == exc:
#                continue
        if user_code:
            if code == user_code:
                   write(line, code=user_code)
#                   print(line,user_code)
        if "-all" in sys.argv:
            if code and code != 200 and code != 404:
                if exc:
                    if exc != code:
                        write(line, code)
                else:
                    write(line, code)

        if code == 200:
            write(line)

        while len(dir)>30:
            dir = '...' + dir[10:]
        print(f"\tTesting: {i} of {len(data)} {dir} {code}"," "*7,end="\r")
        if sec:
            time.sleep(sec)

print('\n\n')
try:
   if i >= 1:
      pass
except:
    i = -1
print(f"done {i+1} / {len(data)}")


