import requests
from pprint import pprint
cookie = 'PVEAuthCookie=PVE:apiuser@pam:65972FBB::RFxuxFlVm13ZWmBCqCVQNUfnDU3XtXZWt3PP7CnwRWafzhUnAXJG/3pKDcpT4U2ANzlSvhS3YgZk/tCU9/5CQMTMy8Gs1xQj98jzkFFgxTDOkEgAXyWbX0p76ZNEgmtK+cwItrQ01ccp4g4xCcrv/Ixp/9StSq1q8li57Cb8hwIl9zke4muroCIWy0MRgxI1LleHp+PRmOkdkfRHzap0mZv+tAsp58p2k2/s5wOyoBUQl2fBmEZGXEivYLVNimkZRT8qPwpKXgQWjZHFCsRPK6jSLZUdwrynMnkWH8M7t+OfpsW/GMlaOKfAfuLBKLlI/miykdazwilI8o34mCDKeg=='


payload = {}
headers = {
  'CSRFPreventionToken': '',
  'Cookie': cookie
}

url = "https://192.168.240.8:8006/api2/json/nodes/vm1/status"
response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
pprint(response)
print("--------------------------------------------------------------------")
url = "https://192.168.240.8:8006/api2/json/nodes/"
response = requests.request("GET", url, headers=headers, data=payload, verify=False).json()
pprint(response)
