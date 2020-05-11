This tutorial will cover following two topics:

1. Dynamic contextualization and model serving in a scalable production environment 
3. Reliable continues integration and development process

--------------------

Important:

_It is expected that you have finished the prelab of the distributed e-infrastructures part._

0. The tasks and the configurations are designed for the Ubuntu 18.04 with medium VM flavor.  

1. We will use SNIC Science Cloud (SSC) for all the tasks. In case you want to learn more about SSC visit website  http://cloud.snic.se

2. We recommend you to create a VM in SSC and execute all the tasks on that virtual machine. You can run the tasks on your laptops but it may break you local working environment.

3. For all these tasks clone the repository:

https://github.com/SNICScienceCloud/technical-training.git

The code for all the tasks is available in the "model-serving" directory. 

```
model-serving
Single_server_without_docker
Single_server_with_docker
CI_CD
OpenStack-Client
```
------------------------

# Dynamic contextualization

Dynamic contextualization is a process of preparing a customized computing environment at runtime. The process ranging from creating/defining user roles and permissions to updating/installing different packages. 

## Task-1: Single server deployment without docker containers

In this task we will learn how the dynamic contextualization works using Cloudinit package. For this task we need to use OpenStack APIs to start a VM and contextualize it at run time. The contextualization process will setup following working environment: 


1. Flask web application as a frontend server 
2. Celery and RabbitMQ server for backend server
3. Model execution environment based on Keras and TensorFlow

In case you are not familiar with the above mentioned packages please read the following links: 

1. Flask Application -> https://flask.palletsprojects.com/en/1.1.x/
2. Celery and RabbitMQ -> https://docs.celeryproject.org/en/stable/getting-started/
3. Keras and TensorFlow -> https://www.tensorflow.org/guide/keras
4. OpenStack -> https://www.openstack.org/

A client will send a prediction request from the frontend web server, the server will pass the request to the backend Celery environment where running workers in the setup will pickup the task, run the predictions by loading the available model, send back the results and finally frontend server will display the results.

## Steps for the contextualization

1 - Goto "technical-training/model-serving/single_server_without_docker/production_server/“  directory. This directory contains the code that will run on your production server. Following is the structure of the code: 

``` 
 - Flask Application based frontend 
    -- app.py
    -- static
    -- templates
 - Celery and RabbitMQ setup
    -- run_task.py
    -- workerA.py
 - Machine learning Model and Data 
    -- model.h5
    -- model.json
    -- pima-indians-diabetes.csv
```

Open different files and try to understand the application's structure. 

2 - Goto the `technical-training/model-serving/openstack-client/single_node_without_docker_client/` directory. This is the code that we will run to contextualize our production server. The code is based on following two files:

```
cloud-cfg.txt
start_instance.py
```

Open the files and try to understand the steps. _You need to setup variable values in the start_instance.py script._ 

-------------
In order to run this code, you need to have OpenStack API environment running. Follow the instructions available on the following links: 

i. Goto https://docs.openstack.org/install-guide/environment-packages-ubuntu.html , http://docs.openstack.org/cli-reference/common/cli_install_openstack_command_line_clients.html and download the client tools and API for OpenStack.

ii. Download the Runtime Configuration (RC) file from the SSC site (Project->Compute->Access & Security->API Access->Download OpenStack RC File).

iii. Confirm that your RC file have following enviroment variables:

```
export OS_USER_DOMAIN_NAME="snic"
export OS_IDENTITY_API_VERSION="3"
export OS_PROJECT_DOMAIN_NAME="snic"
```
iv. Set the environment variables by sourcing the RC-file:
`# source <project_name>_openrc.sh`

v. The successful output of the following commands will confirm that you have the correct packages available on your VM:

```
openstack server list
openstack image list
```

vi. For the API communication we need following extra packages:

```
apt install python3-openstackclient
apt install python-novaclient
apt install python-keystoneclient
```

------------------

Once you have setup the environment, run the following command. 

` # python3 start_instance.py `

The command will start a new server and initiate the contextualization process. It will take approximately 10 to 15 minutes. The progress can be seen on the cloud dashboard. Once the process finish, attach a floating IP to your production server and access the webpage from your client machine. 

Welcome page `http://<PRODUCTION-SERVER-IP>:5100`. Predictions page `http://<PRODUCTION-SERVER-IP>:5100/predictions`

## Questions

1. Explain how the application works? Please keep your answer breif to one paragraph. 

2. Write at least four drabacks of the deployment stratagy adopted in the task-1. 

3. Currently the contextualization process takes 10 to 15 minutes. Suggest a solution to reduce the deployment time.   

