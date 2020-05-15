## Data Python Exercise

This exercise is designed to show us your python programming skill. Although the problem isn't very hard, we would like you to tackle the task the same way you would with a client. We expect that you provide us with a python application that follows python best practices.     

Your first tasks are to :  

* Clone this repo
* Unencrypt the project direction file  interview_problem.md.encrypted. The file has been encrypted using the AES-256-CBC algorithm with openssl.  

* Follow the directions interview_problem.md

### Here are some resources on openssl   
https://wiki.openssl.org/index.php/Enc

For Windows:   
https://wiki.openssl.org/index.php/Binaries

Hint This would be the command in linux to decrypt the file:

openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -md sha512 -d -in interview_problem.md.encrypted -pass pass:(provided password) > interview_problem.md
