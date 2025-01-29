# Distributed Key-Value Store with Consistent Hashing

Saving and retrieving data to/from a distributed key-value store is tricky.
We need to distribute the data across multiple servers and ensure that the data is evenly distributed.
If the data is not evenly distributed, some servers will have more data than others, which can lead to performance issues.
To distribute the data evenly, we can use a technique called consistent hashing.

Consistent hashing is a technique used in distributed systems to distribute data across multiple servers.
It is used in systems where data is distributed across multiple servers and the servers can be added or removed dynamically.
Consistent hashing is used in systems like load balancers, distributed caches, and distributed databases.

In this sample project, we use consistent hashing to distribute data across multiple Redis instances.

## Instructions

```bash
docker-compose up -d

python zoo_setup.py

./start.sh 192.168.0.100:7001
```
