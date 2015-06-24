from linkedin import linkedin # pip install python-linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = '772jk5p0ft1g55' #初始信息源
CONSUMER_SECRET = 'FXw9hRWAf6bDoA7Y'
USER_TOKEN = '3aea0b44-88f8-41fe-893b-5723934d69eb'
USER_SECRET = '164c8431-2488-42a3-a7b1-f0808b5d73b3'

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

app.get_profile()

import json
import os


connections = app.get_connections()

connections_data = os.path.join("C:/", "Users", "lizhaoning", "Desktop", "coco.csv")

f = open(connections_data, 'w')
f.write(json.dumps(connections, indent=1))
f.close()

from prettytable import PrettyTable # pip install prettytable

pt = PrettyTable(field_names=['Name', 'Location'])
pt.align = 'l'

[ pt.add_row((c['firstName'] + ' ' + c['lastName'], c['location']['name'])) 
  for c in connections['values']
      if c.has_key('location')]

print pt

import json

# See http://developer.linkedin.com/documents/profile-fields#fullprofile
# for details on additional field selectors that can be passed in for
# retrieving additional profile information.

# Display your own positions...

my_positions = app.get_profile(selectors=['positions'])
print json.dumps(my_positions, indent=1)

# Display positions for someone in your network...

# Get an id for a connection. We'll just pick the first one.
connection_id = connections['values'][1]['id']
connection_positions = app.get_profile(member_id=connection_id, 
                                       selectors=['positions'])
print json.dumps(connection_positions, indent=1)

