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
LOG_FILE="${1}"

# read file and provide insignts
# total requests:
CHECKS_TOTAL="$(wc -l ${LOG_FILE}|awk '{print $1}')"
CHECKS_200="$(grep ^200 ${LOG_FILE}|wc -l| awk '{print $1}')"




echo "Last check at: $(stat ${LOG_FILE}|grep ^Modify| sed 's/^Modify: //')"
echo "Total   checks: ${CHECKS_TOTAL}"
echo "OK(200) checks: ${CHECKS_200}"
echo ""
#echo "Other checks: ${500_checks}"
echo "#----"
echo "Amount  Code Body"
echo "#----"
cat ${LOG_FILE}| sort|uniq -c |sort -n
