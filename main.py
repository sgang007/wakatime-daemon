# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 00:45:03 2015

@author: shubo
"""

import urllib2
import json
#import pprint
#
base_url = 'https://wakatime.com/api/v1'
res_current_user = '/users/current'
stats = '/stats/last_7_days'
res_leaders = 'leaders'
api_key = 'aa7cad32-7b96-4852-8d7d-b5a0fbb0005d'

url = base_url + res_current_user + stats+'?api_key=' + api_key

#print url
user_data = json.load(urllib2.urlopen(url))
seconds = user_data['data']['total_seconds']
print 'User seconds:', seconds

#data = json.load(response)
data = json.load(open('leaders','r'))
log_time =[]
daily_time = []

for users in data['data']:
    lang = users['running_total']['languages']  
    name = users['user']['full_name']
    time = users['running_total']['total_seconds']
    daily = users['running_total']['daily_average']
    log_time.append(time)
    daily_time.append(daily)
    #print 'Name: ',name
    #print 'Total Seconds: ', time
    #print 
    #for i in lang:
    #    print i['name']
    #print '\n'
#for story in data['data']:
#	print story
print max(log_time) 
print max(daily_time)
#pprint.pprint(data)

