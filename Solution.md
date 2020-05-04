# Understanding of the challenge

- Build test probe to the service which can intercept return code and information body (return message)
- Send request with some meaningful message and GET, so server operator while reading the logs can spot/filter those requests
- it should be able to to probe server multiple times a minute
- the service has to have history of health - ideally store results in a file sqlite or rrd
- No response should also be recognized - timeout to the request is required and result stored in history

# Resolution
I'll choose Bash shell as I've got not enough time to go Python

## Requirements
* Linux machine with Bash Shell installed


## Implementation:

There are two scripts:
* collector.sh - probes service and collects the data to the file
* status_check.sh - interrogates the file to check the status

NOTE: collector.sh needs to be executed in separate shell as it is run as a service.

## Usage
1. Open first terminal and execute below.
```bash collector.sh
```
2. Open next terminal and to check results execute below.
```bash status_check.sh <file_name_of_the_log_file>
```
