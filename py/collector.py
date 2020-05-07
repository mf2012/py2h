#!/usr/bin/env python3

import requests
import yaml
import datetime
import sys
import time

if len(sys.argv) != 2:
   print('usage: '+sys.argv[0]+' <conf_file>')
   print('   ex: '+sys.argv[0]+' ./collector_cfg.yml')
   sys.exit(1)

cfg = None
try:
    with open(sys.argv[1], 'r') as conf_file:
        cfg = yaml.load(conf_file, Loader=yaml.FullLoader)
except IOError:
    print("ERROR: Could not open config file (%s)" % sys.argv[1])
except yaml.scanner.ScannerError as e:
    print("ERROR: problem in YAML in config file (%s): %s" % (sys.argv[1], e))


# Get all configuration values form the config file
url = cfg['collector']['url']
test_interval = cfg['collector']['test_interval']
test_timeout = cfg['collector']['test_timeout']
message = cfg['collector']['message']
log = cfg['collector']['log_file']

# POST and PUT can send some info to the server but are not allowed
# GET cannot send any data to the server - so we need a bit of trickery
#    and form url with some message to the server admin
formed_url=url+'/'+message
#print (formed_url)


def url_test():
    timestamp=datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    try:
        r = requests.get(formed_url, verify=False, timeout=int(test_timeout))
        code=r.status_code
        body=r.text
    except requests.exceptions.Timeout:
        code = "001"
        body = "ERR: connection timeout"
    except requests.exceptions.ConnectionError:
        code = "002"
        body = "ERR: No connection to the host"

    result=(timestamp +' '+ str(code)+' '+ str(body))
    return(result)

# Main loop
try:
    print('Press [CTRL+C] to stop')
    while True:
        #print(url_test())
        with open(log, 'a') as file:
            file.write(url_test()+'\n')
            file.close()
        time.sleep(int(test_interval))

except KeyboardInterrupt:
    pass
