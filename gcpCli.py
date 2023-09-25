import os
from google.cloud import compute_v1

project_id = 'cse5333-lab1'
zone_name = 'us-central1-a'

compute_client = compute_v1.InstancesClient()

instance_name = 'VM-instance1'
machine_type = f'zones/{zone_name}/machineTypes/e2-micro'
image_family = 'debian-12'
image_project = 'debian-cloud'

boot_disk_size = 10

network_interface = 'nic0'
network_name = f'projects/{project_id}/global/networks/default'

instance_details = {
    'name':instance_name,
    'machineType':machine_type,
    'disks':[{
        'boot':True,
        'initializeParams':{
            'sourceImage':f'projects/{image_project}/global/images/family/{image_family}'
        },
        'autoDelete':True,
        'bootSizeGb':boot_disk_size
    }],
    'networkInterfaces':[{
        'name':network_interface,
        'network':network_name
    }]
}

operation = compute_client.insert(project=project_id,
                                  zone=zone_name,
                                  body=instance_details
                                  ).execute()
operation_name =operation['name']

compute_client.wait(project=project_id, zone=zone_name, operation=operation_name)

print("instance created...")
