import inspect
from os import environ as env
from  novaclient import client
import keystoneclient.v3.client as ksclient
from keystoneauth1 import loading
from keystoneauth1 import session

loader = loading.get_plugin_loader('password')
from os import environ as env
import keystoneclient.v3.client as ksclient

auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
                                username=env['OS_USERNAME'],
                                password=env['OS_PASSWORD'],
                                project_name=env['OS_PROJECT_NAME'],
                                project_domain_name=env['OS_USER_DOMAIN_NAME'],
                                project_id=env['OS_PROJECT_ID'],
                                user_domain_name=env['OS_USER_DOMAIN_NAME'])            
sess = session.Session(auth=auth)
nova = client.Client('2.1', session=sess)

print '\n Server List:\n'

for server in nova.servers.list():
    print server.id, server.name

