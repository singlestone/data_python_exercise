## Tech Lead Data Python Exercise

This exercise is designed to show us your python programming skills. 
Although the problem isn't very hard, we would like you to tackle the task the same way you would with a client. 
We expect that you provide us with a python application that follows python best practices as defined by the README at the root of the repository.   

Your first tasks are to :  

* Clone this repo
* Un-encrypt the project direction file  ```interview_problem.md.encrypted```. The file has been encrypted using the AES-256-CBC algorithm with openssl.  

* Follow the directions interview_problem.md

### Here are some resources on openssl   
https://wiki.openssl.org/index.php/Enc

For Windows:   
https://wiki.openssl.org/index.php/Binaries

Hint This would be the command in linux to decrypt the file:

openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -md sha512 -d -in interview_problem.md.encrypted -pass pass:<provided password> > interview_problem.md


### Docker

A docker compose yaml file has been provided. Docker compose will run all docker containers needed for the exercise.
Here are the basic information needed for interacting with the PostgreSQL and MongoDB data stores.

Username: singlestone
Password: singlestone
database: singlestone
collection: teachers
table: students




### Grading

* follow all directions in the main repository [README](../README.md)
* Code should use type hinting, the mypy linter will identify any missed type hints.
* The code has majority of the code covered by unit tests that pass.
* the code has integration tests that pass.
* A Github workflow is created that runs pylint, mypy then runs all unit tests.

