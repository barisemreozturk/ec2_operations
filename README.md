# ec2_operations
You can get your intance ids, start and stop your instances with this project.

For get your instance ids;
Endpoint-1: http://localhost:8081/ec2/list?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>

For start your instances;
Endpoint-2: http://localhost:8081/ec2/start?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>&InstanceIds=<instance_id1>,<instance_id2>,<instance_id3> (You can add as many instance_id as you want by separating them with commas.)

For stop your instances;
Endpoint-3: http://localhost:8081/ec2/stop?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>&InstanceIds=<instance_id1>,<instance_id2>,<instance_id3> (Has same rules with start endpoint.)
