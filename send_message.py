import json
import requests
import sys

WEBHOOK_URI = '<YOUR_CHIME_WEBHOOK_URL_HERE>'

def post_message(msg):
    response = None
    try:
        response = requests.post(
            url=WEBHOOK_URI,
            json={"Content": msg})
        return json.loads(response.text)
    except:
        return response.text

## Check for a message as runtime parameter
if len(sys.argv) != 2:
    print('\n\tIncorrect usage!')
    print('\n\tExample Usage:')
    print('\tpython3 ' + sys.argv[0] + ' \"Hello world\"\n')
    exit()

## Get the message to send as a parameter
message = sys.argv[1]

## Post the message
req_res = post_message(message)
print(json.dumps(req_res, indent=2))
