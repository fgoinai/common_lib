'''
Arthor:		FGO
Usage:		Send HTTP POST request
Param:
url: target url
param: request parameter
header: header
verify: SSL cert will be verified ot not
cookies: cookies of connection

Return:		POST connection object
Example:
post_obj = post('1.2.3.4', , , False)
'''
def post(url, param, header='', verify=True, cookies=''):
    import requests
    if header != '':
        con = requests.post(url, data=param, headers=header, verify=verify, cookies=cookies)
    else:
        con = requests.post(url, data=param, verify=verify, cookies=cookies)
    if con.status_code == 200:
        return con
    else:
        con.raise_for_status()
