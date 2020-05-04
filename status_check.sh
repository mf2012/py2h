#!/bin/bash
## DEBUG
# set -x

# How to use the check
usage() {
  echo "Usage: $0 <log_file_name>"
  echo "   Ex. $0 test_service.log"
}


# Check if log_file has been provided (add if file exist check later)
if [ "$1" == "" ]; then
    usage
    exit 1
fi
LOG_FILE="$1"

# read file and provide insignts
# total requests:
t_checks=$(wc -l ${LOG_FILE} |awk '{print $1}')
# 200_checks=$(grep ^200 ${LOG_FILE} |wc -l| awk '{print $1}' )
# 500_checks=$(grep ^500 ${LOG_FILE} |wc -l| awk '{print $1}' )




echo "Total checks: ${t_checks}"
#echo "OK(200) checks: ${200_checks}"
#echo "Other checks: ${500_checks}"
#echo ""

cat ${LOG_FILE}| sort|uniq -c |sort -n
