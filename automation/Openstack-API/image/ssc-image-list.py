
from os import environ as env
import glanceclient.v2.client as glclient
import keystoneclient.v3.client as ksclient

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
                           username=env['OS_USERNAME'],
                           password=env['OS_PASSWORD'],
                           project_name=env['OS_PROJECT_NAME'],
                           project_domain_name=env['OS_USER_DOMAIN_NAME'],
                           project_id=env['OS_PROJECT_ID'],
                           version=env['OS_IDENTITY_API_VERSION'],
                           user_domain_name=env['OS_USER_DOMAIN_NAME'],
                           region_name=env['OS_REGION_NAME'])

glance_endpoint = keystone.service_catalog.url_for(service_type='image')

glance = glclient.Client(glance_endpoint, token=keystone.auth_token)

images = glance.images.list()

for image in images:
    print image.get('name', 'not available'),

