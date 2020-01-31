# proxy_requests


# 모듈 설명
프록시를 이용해 요청합니다.



### SniRequests 예제

요청하고자 하는 웹사이트에서 사용하고 있는 서비스의 DNS주소를 이용해야합니다.  
예) CloudflareDNS, OpenDNS, GoogleDNS  
-> 웹 사이트에서 Cloudflare 서비스를 사용하고 있다면 CloudflareDNS로 SNI_DNS_SERVER_ADDRESS 를 지정해주세요. 

```python
import proxy_requests
proxy_requests.SNI_DNS_SERVER_ADDRESS = '1.1.1.1'
sni = proxy_requests.SniRequests()
html = sni.get('https://manamoa.net').text # 마나모아 사이트는 Cloudflare 서비스를 사용함
```


### TorRequests Example

토르 프록시를 이용해서 웹에 요청합니다.

```python
import proxy_requests
tor = proxy_requests.TorRequests()
html = tor.get('https://check.torproject.org/').text
```


## 사용법 영상
https://blog.naver.com/powerapollon/221791573044


## 스타좀 눌러줍쇼..

