The tutorial will cover following two topics:

1 - Dynamic contextualization and model serving in a scalable production environment 
3 - Reliable continues integration and development process

Important:
———————

1 - Create a VM and execute all the tasks on that virtual machine. You can run the tasks on your laptops but it may break you local working environment.

2 - For all these tasks clone the repository:

https://github.com/SNICScienceCloud/technical-training.git

The code for all the tasks is available in the "model-serving" directory. 

model-serving
Single_server_without_docker
Single_server_with_docker
CI_CD
OpenStack-Client
————————

1- Dynamic contextualization

Dynamic contextualization is a process of preparing a customized computing environment at runtime. The process ranging from creating/defining user roles and permissions to updating/installing different packages. 

Task -1: Single server deployment without docker containers

In this task we will learn how the dynamic contextualization works using Cloudinit package. For this task we need to use OpenStack APIs to start a VM and contextualize it at run time. The contextualization process will setup following working environment: 

1 - Flask web application as a frontend server 
2 - Celery and RabbitMQ server for backend server
3 - Model execution environment based on Keras and TensorFlow

In case you are not familiar with the above mentioned packages please read the following links: 

Flask Application -> Link
Celery and RabbitMQ -> Link
Keras and TensorFlow -> Link
OpenStack ->

A client will sent a prediction request from the frontend web server, the server will pass the request to the backend Celery environment where running workers in the setup will pickup the task, run the predictions by loading the available model, send back the results and finally frontend server will display the results.

Steps for the contextualization

1 - Goto "technical-training/model-serving/single_server_without_docker/production_server/“  directory. This directory contains the code that will run on your production server. Following is the structure of the code: 

Flask Application based frontend. 
app.py
static
templates
Celery and RabbitMQ setup
run_task.py
workerA.py
Machine learning Model and Data 
model.h5
model.json
pima-indians-diabetes.csv

Open different files and try to understand the application flow. 

2 - Goto “technical-training/model-serving/openstack-client/single_node_without_docker_client/“ directory. This is the code that we will run to contextualize our production server. The code is based on following two files:

cloud-cfg.txt
start_instance.py

Open the files and try to understand the steps. You need to setup variable values in the start_instance.py script. 

In order to run this code, we need to have OpenStack API environment running. Follow the instructions available on the following links: 

i - Install OpenStack command line tools and API ->
ii - Create an API communication password on the SSC website ->
iii - Download API access RC file form the SSC cloud ->

Once you have setup the environment, run the following command. 

# python3 start_instance.py

The command will start the server and initiate the contextualization process. it will take approximately 10 to 15 minutes. One the cloud dashboard you can see the progress. Once the process finish, attach a floating IP to your production server and access the webpage from your client machine. 

