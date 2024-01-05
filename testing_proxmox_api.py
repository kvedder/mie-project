import requests, time
from pprint import pprint
cookie = 'PVEAuthCookie=PVE:apiuser@pam:65976B9A::mbdWg9JG75rPoo08+si8x3BxrqAAPfm8EwD3p+gGZzDypFaR+FRstoJcPI/7HwwezPWpCabO5mnmOqFexS3KttaqzC83LML235sTolIep9bdc79lsheMvScQexlJUCCMaYIeInK7kEMXRLiyJfitfMpdJ/OF4U7g7kJx1p/Vi4lxi8QF/3EEHWJ6p9IK94zSqgbgThR76cOuaVc5KP1hsoNrwFmKs+iVfnQY8ltuG9NcTYb/VNZJWBOpxRgCrlfhhQXfhZ7VeYEOWH3aNaeOkWoSEZYP0Wo6G+NEuqp9+rqAapbQ3COpZHWfuFmC2dGxyoXyQj8aGcMvnxgvnnJ/lg=='
import json

payload = {}
headers = {
  'CSRFPreventionToken': '65976B9A:fBxw8K8O78aYXet/QFgiCbY+O+daS8jNi3uUeQ7PJa8',
  'Content-Type': 'application/json',
  'Cookie': cookie
}

# create the VM from the template
url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/106/clone"
payload = json.dumps({
  "newid": 120,
  "description": "testing VM for MIE",
  "name": "mie-test-dhcp",
})
response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
#
print(response)

time.sleep(15)

# start the VM
url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/120/status/start"
payload = json.dumps({})
response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

print(response)
time.sleep(15)


# get ip of new VM created
url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/120/agent/network-get-interfaces"
response = requests.request("GET", url, headers=headers, verify=False).json()
pprint(response['data']['result'][1]['ip-addresses'])

# write the provision script to the server
filename = "install_dhcp.sh"
with open(filename) as script:
    contents = script.read()

url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/120/agent/file-write"
payload = json.dumps({
  "content": contents,
  "file": "/tmp/install_dhcp.sh"
})

response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()

print(response)

print("--------------------------------------------------------------------")

url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/120/agent/exec"
payload = json.dumps({
  "command": ["chmod", "+x", "/tmp/install_dhcp.sh"]
})

response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
print(response)

print("--------------------------------------------------------------------")

url = "https://192.168.240.8:8006/api2/json/nodes/vm1/qemu/120/agent/exec"
payload = json.dumps({
  "command": ["bash", "-c", "/tmp/install_dhcp.sh"]
})

response = requests.request("POST", url, headers=headers, data=payload, verify=False).json()
print(response)
