import hashlib
import os
from rauth import OAuth2Service

service = OAuth2Service(
    client_id='xarDLpKHjEhDk-vabP6aHKYd', # your App ID from https://wakatime.com/apps
    client_secret='sec_ChGp_dCqyb6N3TF0ylQwsko8ntnVXRro-KB_N6-P2SLTytmXFwrkCodz5sPPu4yK7Enebq3vXeydd3NJ', # your App Secret from https://wakatime.com/apps
    name='wakatime',
    authorize_url='https://wakatime.com/oauth/authorize',
    access_token_url='https://wakatime.com/oauth/token',
    base_url='https://wakatime.com/api/v1/')

redirect_uri = 'https://wakatime.com/login_ok'
state = hashlib.sha1(os.urandom(40)).hexdigest()
params = {'scope': 'email,read_logged_time',
          'response_type': 'code',
          'state': state,
          'redirect_uri': redirect_uri}

url = service.get_authorize_url(**params)
print('**** Visit {url} in your browser. ****'.format(url=url))

# the code should be returned upon the redirect from the authorize step,
# be sure to use it here (hint: it's in the URL!)
# also, make sure returned state has not changed for security reasons.
headers = {'Accept': 'application/x-www-form-urlencoded'}
session = service.get_auth_session(headers=headers,
                                   data={'code': 'foo',
                                         'grant_type': 'authorization_code',
                                         'redirect_uri': redirect_uri})

print(session.get('users/current').json()['data']['email'])