## Data Tech Lead Python Exercise  

For this exercise, please write a Python application that processes 
two data files:

1. A PostgreSQL table containing student data
2. A MongoDB collection containing teacher data

From these data stores, generate an output file in JSON listing:

1. Each student
2. The teacher the student has
3. The class ID the student is scheduled for

Upload the JSON file to an AWS S3 bucket.

Assumptions:
* An analyst with no Python coding ability should be able to setup and run the 
app using the directions provided.
* The software will run on a machine with limited resources, and it may not be 
possible to read all the data into memory at one time.

Additional requirements for Tech Lead:

* Follow all guidelines in the main repository [README](../README.md)
* Use type hinting. Use a mypy linter to identify any missed type hints.
* 50% or more of code coverage with unit tests.
* One or more integration tests.

### Database Servers

Docker compose will run all needed development databases locally. 
A `docker-compose.yml` file has been provided. To startup the local development environment, run:

```
cd path/to/data_tech_lead
docker-compose up
```

### Connection Information

Here is connection information for the PostgreSQL and MongoDB data stores:

```
username: singlestone    
password: singlestone    
database: singlestone 
``` 

MongoDB collection: `teachers`    
PostgreSQL table: `students`    

MongoDB GUI: http://localhost:8081   
PostgreSQL GUI: http://localhost:8080  (make sure you put `postgres` as the server)

**Note:** The GUIs use the HOSTNAME in `docker-compose-yml` to connect to each data store. When writing code to connect to a data store, you should instead use `localhost` as the hostname.

