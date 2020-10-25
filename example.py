
# 세 사이트 모두 일반적으로 접속되지 않습니다.


import proxy_requests
tor = proxy_requests.TorRequests()
req3 = tor.get('https://httpbin.org/ip').json()
print('TorRequests : ', req3)