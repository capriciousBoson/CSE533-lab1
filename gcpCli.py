
from google.cloud import compute_v1

project_id = 'cse5333-lab1'
zone_name = 'us-central1-a'
instance_name = 'Ubuntu-VM-lab1'

new_instance = compute_v1.Instance()
new_instance.network_interfaces = [{
        'name':'nic0',
        'network':f'projects/{project_id}/global/networks/default'
    }]
new_instance.name = instance_name
new_instance.disks = [{
        'boot':True,
        'initializeParams':{
            'sourceImage':f'projects/debian-cloud/global/images/family/debian-12'
        },
        'autoDelete':True,
        'bootSizeGb':10
    }]
new_instance.machine_type = f'zones/{zone_name}/machineTypes/e2-micro'

request = compute_v1.InsertInstanceRequest()
request.zone = zone_name
request.project = project_id
request.instance_resource = new_instance

print(f"Creating the {instance_name} instance in {zone_name}...")

instance_client = compute_v1.InstancesClient()
operation = instance_client.insert(request=request)

#wait_for_extended_operation(operation, "instance creation")

print(f"Instance {instance_name} created.")
print(instance_client.get(project=project_id, zone=zone_name, instance=instance_name))
