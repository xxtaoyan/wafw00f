#!/usr/bin/env python

NAME = 'XLabs Security WAF'

def is_waf(self):
    if self.matchheader(('x-cdn', 'XLabs Security')):
        return True
    # Another nice fingerprint found returning server 
    # header as 'Server: XLabs WAF v3.0 http://www.xlabs.com.br/waf'
    if self.matchheader(('server', 'XLabs WAF(.*)?')):
        return True