# ec2_operations
You can get your intance ids, start and stop your instances with this project.

For get your instance ids;

```go
Endpoint-1: "http://localhost:8081/ec2/list?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>"

```

For start your instances;

```go
Endpoint-2: "http://localhost:8081/ec2/start?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>&InstanceIds=<instance_id1>,<instance_id2>,<instance_id3>" (You can add as many instance_id as you want by separating them with commas.)


```

For stop your instances;

```go
Endpoint-3: "http://localhost:8081/ec2/stop?aws_access_key_id=<aws_access_key>&aws_secret_access_key=<aws_secret_access_key>&region_name=<region_name>&InstanceIds=<instance_id1>,<instance_id2>,<instance_id3>" (Same rules with start endpoint.)

```

# Additional Infos

Project is creating a log file when you run it. You can see your logs in there.

config.cfg file is including host and port infos. You can change them if you want.
