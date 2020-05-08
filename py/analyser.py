import sys
from datetime import datetime,timedelta
import yaml
from collections import Counter

if len(sys.argv) != 2:
   print('usage: '+sys.argv[0]+' <conf_file>')
   print('   ex: '+sys.argv[0]+' ./analyser_cfg.yml')
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
log = cfg['analyser']['log_file']
time_window = cfg['analyser']['time_window']

def get_datetime_from_line(s):
    return datetime.strptime(s[:19], '%Y-%m-%d_%H:%M:%S')

def get_return_code(c):
    return c[20:23]

with open(log, 'r') as file:
  # Get last line from the file to capture last time it was used
  # use os.SEEK_END for bug files
  num_lines=0
  list_codes=[]
  for line in file:
      num_lines=num_lines+1
      list_codes.append(get_return_code(line))
      pass
  last_line=line

# older_than_5m = (datetime.now() - timedelta(minutes=5))
older_than_Xm = (get_datetime_from_line(last_line) - timedelta(minutes=int(time_window)))
list_codes_in_Xm=[]
with open(log, 'r') as file:
  for line in file:
     if get_datetime_from_line(line) >= older_than_Xm:
       list_codes_in_Xm.append(get_return_code(line))
       print(line.rstrip())

# use tailhead or tailer for line management if necessary for now it is time based
print('\n  Last check: '+str(get_datetime_from_line(last_line)))
print('    Time now: '+str(datetime.now())[:19])
print('Total checks: '+str(num_lines))
print('Totals per code: ', Counter(list_codes),'\n')
print('Totals per code in last '+str(time_window)+' min: ', Counter(list_codes_in_Xm),'\n')

file.close()
