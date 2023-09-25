
from google.cloud import compute_v1

project_id = 'cse5333-lab1'
zone = 'us-central1-a'
instance_name = 'UbuntuVMlab1'



# details for disk image
project_name = 'debian-cloud'
image_name = 'debian-12'

boot_disk = compute_v1.AttachedDisk()
initialize_params = compute_v1.AttachedDiskInitializeParams()
initialize_params.source_image = 'projects/{project_name}/global/images/{image_name}'
initialize_params.disk_size_gb = 10
initialize_params.disk_type = 'zones/{zone}/diskTypes/pd-balanced'
boot_disk.initialize_params = initialize_params
boot_disk.auto_delete = True
boot_disk.boot = True





new_instance = compute_v1.Instance()
new_instance.network_interfaces = [{
        'name':'nic0',
        'network':f'projects/{project_id}/global/networks/default'
    }]
new_instance.name = instance_name
new_instance.disks = [boot_disk]
new_instance.machine_type = f'zones/{zone}/machineTypes/e2-micro'

request = compute_v1.InsertInstanceRequest()
request.zone = zone
request.project = project_id
request.instance_resource = new_instance

print(f"Creating the {instance_name} instance in {zone}...")

instance_client = compute_v1.InstancesClient()
operation = instance_client.insert(request=request)

#wait_for_extended_operation(operation, "instance creation")

print(f"Instance {instance_name} created.")
print(instance_client.get(project=project_id, zone=zone, instance=instance_name))
