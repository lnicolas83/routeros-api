# routeros-api
Mikrotik routerOS api in python (based on the code of the mikrotik's wiki, https://wiki.mikrotik.com/wiki/Manual:API_Python3)

Examples :

``` python
>>> import routeros
>>> api = routeros.Api("192.168.98.2",8728,usessl=False, sslverify=False);
>>> api.login('admin','motdepasse')
True

>>> api.find("/ip/address")
(True, [{'id': '1', 'address': '192.168.98.2/30', 'network': '192.168.98.0', 'interface': 'ether1', 'actual-interface': 'ether1', 'invalid': 'false', 'dynamic': 'false', 'disabled': 'false'}, {'id': '3', 'address': '129.0.0.0/32', 'network': '128.0.0.0', 'interface': '*FFFFFFFF', 'actual-interface': '*FFFFFFFF', 'invalid': 'true', 'dynamic': 'false', 'disabled': 'false'}])

>>> api.find("/ip/address",{"address":"129.0.0.0/32"})
(True, [{'id': '3', 'address': '129.0.0.0/32', 'network': '128.0.0.0', 'interface': '*FFFFFFFF', 'actual-interface': '*FFFFFFFF', 'invalid': 'true', 'dynamic': 'false', 'disabled': 'false'}])

>>> api.find("/ip/address",{"interface":"ether1"}, itemlist="address,interface")
(True, [{'address': '192.168.98.2/30', 'interface': 'ether1'}])

>>> api.add('/ip/address',{"address": "192.168.0.1/24", "interface":"ether4"})
True

>>> api.find_and_set("/ip/address",{"interface":"ether2"},{"address":"129.0.0.0/32"})
True

>>> api.find_and_remove("/ip/address",{"interface":"ether2"})
True
```
    class Api
     |  Routeros api
     |  
     |  Methods defined here:
     |  
     |  __init__(self, host, port, usessl=False, sslverify=True, debug=False)
     |  
     |  add(self, path, params)
     |      add (mikrotik's add)
     |      
     |      path      : api path (eg: /ip/address)
     |      params    : add parameters (eg: {'address': '192.168.0.1','interface':'ether4'})
     |      
     |      Return bool
     |  
     |  close(self)
     |      Close connection
     |  
     |  find(self, path, search={}, itemlist='', operation='AND')
     |      find (mikrotik's print)
     |      
     |      path      : api path (eg: /ip/address)
     |      search    : 
     |                   "key" : "value"  -> key = value
     |                   "key" : "@"      -> key exist
     |                   "key" : "!"      -> key not exist
     |                   "key" : ">value" -> key greater than value
     |                   "key" : "<value" -> key less than value
     |      itemlist  : list of item to get (eg: "address" or "address,network"
     |      operation : AND, OR or NOT
     |      
     |      return (bool, [response])
     |  
     |  find_and_remove(self, path, search={}, operation='AND')
     |      find_and_remove (mikrotik's remove [find...])
     |      
     |      path      : api path (eg: /ip/address)
     |      search    : 
     |                   "key" : "value"  -> key = value
     |                   "key" : "@"      -> key exist
     |                   "key" : "!"      -> key not exist
     |                   "key" : ">value" -> key greater than value
     |                   "key" : "<value" -> key less than value
     |      operation : AND, OR or NOT
     |      
     |      Return bool
     |  
     |  find_and_set(self, path, params, search={}, operation='AND')
     |      find_and_set (mikrotik's set [find...])
     |      
     |      path      : api path (eg: /ip/address)
     |      params    : set parameters (eg: {'address': '192.168.0.1','interface':'ether4'})
     |      search    : 
     |                   "key" : "value"  -> key = value
     |                   "key" : "@"      -> key exist
     |                   "key" : "!"      -> key not exist
     |                   "key" : ">value" -> key greater than value
     |                   "key" : "<value" -> key less than value
     |      operation : AND, OR or NOT
     |      
     |      Return bool
     |  
     |  login(self, username, pwd)
     |      Api login
     |      
     |      Return bool
     |  
     |  remove(self, path, id)
     |      remove (mikrotik's remove)
     |      
     |      path      : api path (eg: /ip/address)
     |      id        : mikrotik item(s) id(s) (eg : "1" or "*1" or "1,a" or "*1,a" or ["1","2"] or ["*1","2"]
     |              
     |      Return bool
     |  
     |  send(self, words)
     |      Send raw api command
     |      
     |      Return (bool, response)
     |      
     |      err,msg = send(["line1","line2",...])
     |  
     |  set(self, path, id, params)
     |      set (mikrotik's set)
     |      
     |      path      : api path (eg: /ip/address)
     |      id        : mikrotik item(s) id(s) (eg : "1" or "*1" or "1,a" or "*1,a" or ["1","2"] or ["*1","2"]
     |      params    : set parameters (eg: {'address': '192.168.0.1','interface':'ether4'})
     |      
     |      Return bool
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  logged
     |      True if logged or False if not

