#/usr/bin/python3

import routeros
import requests
import sys

USER = "admin"
PASSWORD = "admin"


try:
    host = sys.argv[1]
except:
    print("host requis")
    sys.exit(1)

try:
    api = routeros.Api(host,8728,usessl=False, sslverify=False);
except:
    print("erreur connexion api")
    sys.exit(1)

ret = api.login(USER, PASSWORD)
if not ret:
    print("erreur login api")
    sys.exit(1)

ret, resp = api.find('/system/package/update')
if not ret:
    print("erreur api")
    sys.exit(1)
    
installed_version = resp[0]["installed-version"]
major_version = installed_version.split('.')[0]
channel = resp[0]["channel"]

comp = ""
if channel == "release-candidate":
    comp = "rc"
    
url = "http://download2.mikrotik.com/routeros/LATEST.{}{}".format(major_version,comp)
try:
    httpreq = requests.get(url)
except:
    print("erreur requete http")
    sys.exit(1)

if httpreq.status_code == 200:
    if httpreq.text.split(" ")[0] != installed_version:
        print("1")
        sys.exit(0)
    else:
        print("0")
        sys.exit(0)
else: 
    print("erreur retour http")
    sys.exit(1)
