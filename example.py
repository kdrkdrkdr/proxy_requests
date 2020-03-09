
# 세 사이트 모두 일반적으로 접속되지 않습니다.

try:
    import requests
    req1 = requests.get('https://manamoa.net')
    print('Requests : ', req1)
except:
    print('Requests : ERROR')
    

import proxy_requests
sni = proxy_requests.SniRequests('hiyobi.me', '1.1.1.1')
req2 = sni.get('https://hiyobi.me')
print('SniRequests : ', req2)



import proxy_requests
tor = proxy_requests.TorRequests()
req3 = tor.get('https://xvideos.com')
print('TorRequests : ', req3)