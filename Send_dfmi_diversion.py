import requests
import json

HEADER = {'Authorization': 'Token <token>'}

uuids = input.get('uuids')
flow_id = '<flow_id>'
case_id = input.get('case_id')
msg_ids = input.get('message_ids')

contact_url = 'https://app.rapidpro.io/api/v2/contacts.json'
flow_url = 'https://app.rapidpro.io/api/v2/flow_starts.json'

uuids = uuids.split(',')
list_urns = []
for uuid in uuids:
    DATA =  {'uuid' : uuid}

    response = requests.get(contact_url, headers=HEADER, params=DATA, verify=True)
    list_urns.append(str(response.json()['results'][0]['urns'][0]))


extra = {"case_id":case_id, "msg_ids":msg_ids}
extra = json.dumps(extra)

DATA =  {"flow": flow_id,
		 "groups": [],
		 "contacts": [],
		 "urns": list_urns,
         "restart_participants":"True",
		 "extra": extra
		 }
response = requests.post(flow_url, headers=HEADER, verify=True, data=DATA)
