from google.cloud import compute

# Create a compute client
client = compute.Client()

# Create a compute instance
instance = client.instances().create(
  project='cse5333-lab1',
  zone='us-central1-a',
  machine_type='e2-micro',
  name='my-instance',
  disks=[
    {
      'boot': True,
      'initialize_params': {
        'image': 'debian-cloud/debian-12'
      }
    }
  ]
)

# Wait for the instance to be created
instance.wait()

# Print the instance's IP address
print(instance.network_interfaces[0].access_configs[0].assigned_nat_ip)
