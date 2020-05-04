#!/bin/bash
## DEBUG
# set -x

# Rate of test in seconds
TEST_RATE=5
# Total time for query operation in seconds
TOTAL_TIME=10
# VARIABLE to change
URL="http://localhost:12345/"
# Message to send to the logs in JSON format, edit the VALUE 'Check challenge' to more meaningful message
PAYLOAD='{"text":"Check challenge"}'

## Please do not change below
CONTENT_TYPE='Content-type: application/json'
LOG="test_service.log"
TIMESTAMP="`date +"%F-%H-%M"`"

# Function to test the server and write result with the code (add timestamp later to limit search only to ex. last 5min.)
test_url() {
  result=$(curl -X GET -H "${CONTENT_TYPE}" --connect-time ${TEST_RATE} --max-time ${TOTAL_TIME} --data "${PAYLOAD}" -s -w "~%{http_code}\n" "${URL}")
  RESPONSE="$(echo ${result}|sed 's/~.*$//')"
  CODE="$(echo ${result}|sed 's/^.*~//')"
  echo "${CODE} ${RESPONSE}" >> ${LOG}
}

## Main Service
echo "Press [CTRL+C] to stop"
while :
do
  test_url
  sleep ${TEST_RATE}
done
