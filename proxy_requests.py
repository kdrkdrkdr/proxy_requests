#-*- coding:utf-8 -*-

# Author : KDR (https://github.com/kdrkdrkdr)

import sys
import os
import requests
import subprocess
import urllib



class TorRequests(object):
    """
This class makes web requests with Tor Proxy.
    """
    
    def __init__(self):
        self._tor_is_alive()
        
        self.tor_session = requests.Session()
        self.tor_session.proxies.update(
            {
                "http"  : "socks5://127.0.0.1:9050",
                "https" : "socks5://127.0.0.1:9050",
            }
        )


    def _tor_is_alive(self):
        os.system('taskkill /f /im tor.exe')
        subprocess.Popen(['./TorService/tor.exe'])


    def get(self, *args, **kwargs):
        return self.tor_session.get(*args, **kwargs)


    def post(self, *args, **kwargs):
        return self.tor_session.post(*args, **kwargs)


    def put(self, *args, **kwargs):
        return self.tor_session.put(*args, **kwargs)


    def patch(self, *args, **kwargs):
        return self.tor_session.patch(*args, **kwargs)


    def close(self):
        self.tor_session.close()


    def delete(self, *args, **kwargs):
        return self.tor_session.delete(*args, **kwargs)



class SniRequests(object):
    """
This class makes web reqeusts by bypass the SNI block.
    """

    def __init__(self, HostURL, DNSADDR):
        self.sni_session = requests.Session()
        self._Enable_SNI_Adapter = _Enable_SNI_Adapter(HostURL, DNSADDR)
        self.sni_session.mount('https://', self._Enable_SNI_Adapter)


    def get(self, *args, **kwargs):
        return self.sni_session.get(*args, **kwargs)


    def post(self, *args, **kwargs):
        return self.sni_session.post(*args, **kwargs)


    def put(self, *args, **kwargs):
        return self.sni_session.put(*args, **kwargs)


    def patch(self, *args, **kwargs):
        return self.sni_session.patch(*args, **kwargs)


    def close(self):
        self.sni_session.close()


    def delete(self, *args, **kwargs):
        return self.sni_session.delete(*args, **kwargs)




class _Enable_SNI_Adapter(requests.adapters.HTTPAdapter):

    def __init__(self, HostURL, SNI_DNS_SERVER_ADDRESS):
        requests.adapters.HTTPAdapter.__init__(self)
        self.hostURL = HostURL
        self.SNI_DNS_SERVER_ADDRESS = SNI_DNS_SERVER_ADDRESS

    def send(self, request, **kwargs):
        try:
            connection_pool_kwargs = self.poolmanager.connection_pool_kw
            result = urllib.parse.urlparse(request.url)
            DNSADDR = self.SNI_DNS_SERVER_ADDRESS
            
            if result.scheme == 'https' and DNSADDR:
                request.url = request.url.replace(
                    'https://' + result.hostname,
                    'https://' + DNSADDR,
                )

                connection_pool_kwargs['server_hostname'] = result.hostname 
                connection_pool_kwargs['assert_hostname'] = result.hostname
                request.headers['Host'] = result.hostname

            else:
                connection_pool_kwargs.pop('server_hostname', None)
                connection_pool_kwargs.pop('assert_hostname', None)

            return super(_Enable_SNI_Adapter, self).send(request, **kwargs)


        except ( requests.exceptions.SSLError, requests.exceptions.ConnectionError ):
            sys.exit(
                "\nProxyRequests ERROR : [SSLError and ConnectionError]"
                "\n+-------------------------------------------------------+"
                "\n|1. Did you set the DNS address properly?               |"
                "\n|2. Did you enter the address of the website correctly? |"
                "\n+-------------------------------------------------------+\n"
            )

