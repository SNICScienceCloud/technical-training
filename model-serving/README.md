This tutorial will cover the following two topics:

1. Dynamic contextualization and model serving in a scalable production environment 
3. Reliable continuous integration and development process

--------------------

Important:

_It is expected that you have finished the prelab of the distributed e-infrastructures part._

_Please terminate VMs once you finish the task._ 

0. The tasks and the configurations are designed for the Ubuntu 18.04 with medium VM flavour.  

1. We will use SNIC Science Cloud (SSC) for all the tasks. In case you want to learn more about SSC visit website  http://cloud.snic.se

2. We recommend you to create a VM in SSC and execute all the tasks on that virtual machine. You can run the tasks on your laptops but it may break your local working environment.

3. For all these tasks clone the repository:

https://github.com/SNICScienceCloud/technical-training.git

The code for all the tasks is available in the "model-serving" directory. 

```
 - model-serving
   -- Single_server_without_docker
   -- Single_server_with_docker
   -- CI_CD
   -- OpenStack-Client
```
------------------------

# Dynamic contextualization

Dynamic contextualization is a process of preparing a customized computing environment at runtime. The process ranging from creating/defining user roles and permissions to updating/installing different packages. 

## Task-1: Single server deployment 

In this task, we will learn how the dynamic contextualization works using Cloudinit package. For this task, we need to use OpenStack APIs to start a VM and contextualize it at run time. The contextualization process will setup the following working environment: 


1. Flask web application as a frontend server 
2. Celery and RabbitMQ server for backend server
3. Model execution environment based on Keras and TensorFlow

In case you are not familiar with the above-mentioned packages please read the following links: 

1. Flask Application -> https://flask.palletsprojects.com/en/1.1.x/
2. Celery and RabbitMQ -> https://docs.celeryproject.org/en/stable/getting-started/
3. Keras and TensorFlow -> https://www.tensorflow.org/guide/keras
4. OpenStack -> https://www.openstack.org/

A client will send a prediction request from the front-end web server, the server will pass the request to the backend Celery environment where running workers in the setup will pick up the task, run the predictions by loading the available model, send back the results and finally frontend server will display the results.

### Steps for the contextualization

0. Start a VM from the SSC dashboard and login to the client VM.

```console 
ssh -i ubuntu@<Client-IP>
```

1. Clone the git repository.

```console
git clone https://github.com/SNICScienceCloud/technical-training.git
```

2. Goto `technical-training/model-serving/single_server_without_docker/production_server/`  directory. This directory contains the code that will run on your production server. Following is the structure of the code: 

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

3. Goto the `technical-training/model-serving/openstack-client/single_node_without_docker_client/` directory. This is the code that we will run to contextualize our production server. The code is based on the following two files:

```console
- CloudInit configuration file  
  -- cloud-cfg.txt
- OpenStack python code
  -- start_instance.py
```

Open the files and try to understand the steps. _You need to setup variable values in the start_instance.py script._ 

-------------
In order to run this code, you need to have OpenStack API environment running. 

_NOTE that Openstack APIs are only need to be installed on the client VM_. 

Follow the instructions available on the following links: 

i. Goto https://docs.openstack.org/install-guide/environment-packages-ubuntu.html , http://docs.openstack.org/cli-reference/common/cli_install_openstack_command_line_clients.html and download the client tools and API for OpenStack.

ii. Download the Runtime Configuration (RC) file from the SSC site (Project->Compute->Access & Security->API Access->Download OpenStack RC File).

iii. Confirm that your RC file have following enviroment variables:

```console
export OS_USER_DOMAIN_NAME="snic"
export OS_IDENTITY_API_VERSION="3"
export OS_PROJECT_DOMAIN_NAME="snic"
```
iv. Set the environment variables by sourcing the RC-file:

```console 
source <project_name>_openrc.sh
```

v. The successful output of the following commands will confirm that you have the correct packages available on your VM:

```console
openstack server list
openstack image list
```

vi. For the API communication we need following extra packages:

```console
apt install python3-openstackclient
apt install python-novaclient
apt install python-keystoneclient
```

------------------

4. Once you have setup the environment, run the following command. 

```console 
python3 start_instance.py
```

The command will start a new server and initiate the contextualization process. It will take approximately 10 to 15 minutes. The progress can be seen on the cloud dashboard. Once the process finish, attach a floating IP to your production server and access the webpage from your client machine. 

Welcome page `http://<PRODUCTION-SERVER-IP>:5100`. Predictions page `http://<PRODUCTION-SERVER-IP>:5100/predictions`

## Questions

1. Explain how the application works? Please keep your answer brief to one paragraph. 

2. What are the drawbacks of the current deployment strategy adopted in the task-1? Write at least four drawbacks.

3. Currently, the contextualization process takes 10 to 15 minutes. How can we reduce the deployment time?   

-----------------------------

TERMINATE THE SERVER VM STARTED FOR THE TASK-1!

-----------------------------

## Task-2: Single server deployment with Docker Containers

In this task, we will repeat the same deployment but with Docker containers. It will create a flexible containerized deployment environment where each container has a defined role. 

1. Now goto `technical-training/model-serving/single_server_with_docker/production_server/` directory on the client VM. The directory contains the code that will run on your production server. Following is the structure of the code: 

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
 - Docker files
    -- Dockerfile
    -- docker-compose.yml
```

Open different files and try to understand the application's structure. 

2 - Goto the `technical-training/model-serving/openstack-client/single_node_with_docker_client/` directory. This is the code that we will run to contextualize the production server. The code is based on the following two files:

```console
- CloudInit configuration file  
  -- cloud-cfg.txt
- OpenStack python code
  -- start_instance.py
```

Open the files and try to understand the steps. _You need to setup variable values in the start_instance.py script._ 

3. Run the following command. 

```console 
python3 start_instance.py
```

The command will start a new server and initiate the contextualization process. It will take approximately 10 to 15 minutes. The progress can be seen on the cloud dashboard. Once the process finish, attach a floating IP to your production server and access the webpage from your client machine. 

Welcome page `http://<PRODUCTION-SERVER-IP>:5100`. Predictions page `http://<PRODUCTION-SERVER-IP>:5100/predictions`

4. The next step is to test the horizontal scalability of the setup. 

4a. Login to the production server. 

```console 
ssh -i ubuntu@<PRODUCTION-SERVER-IP>
```

4b. Switch to the superuser mode.
   
```console
sudo bash
```

4c. Check the cluster status:

```console 
cd /technical-training/model-serving/single_server_with_docker/production_server
docker-compose ps
```

The output will be as following:

```console
   Name                          Command               State                                             Ports                                           
------------------------------------------------------------------------------------------------------------------------------------------------------------------
production_server_rabbit_1     docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:15672->15672/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp
production_server_web_1        python ./app.py --host=0.0.0.0   Up      0.0.0.0:5100->5100/tcp
production_server_worker_1_1   celery -A workerA worker - ...   Up  
```

Following three containers are running on the production server: 

```
production_server_rabbit_1  -> RabbitMQ server
production_server_web_1 -> Flask based web application
production_server_worker_1_1 -> Celery worker 
```

Now we will add multiple workers in the cluster using docker commands. 

4d. Currently, there is one worker available. We will add two more workers. 

```console 
docker-compose up --scale worker_1=3 -d
```

4e. Check the cluster status.

```console
docker-compose ps
```

Output will be:

```console
            Name                          Command               State                                             Ports                                           
------------------------------------------------------------------------------------------------------------------------------------------------------------------
production_server_rabbit_1     docker-entrypoint.sh rabbi ...   Up      15671/tcp, 0.0.0.0:15672->15672/tcp, 25672/tcp, 4369/tcp, 5671/tcp, 0.0.0.0:5672->5672/tcp
production_server_web_1        python ./app.py --host=0.0.0.0   Up      0.0.0.0:5100->5100/tcp
production_server_worker_1_1   celery -A workerA worker - ...   Up
production_server_worker_1_2   celery -A workerA worker - ...   Up                                                             
production_server_worker_1_3   celery -A workerA worker - ...   Up
```

Now we have 3 workers running in the system. 

4f. Now scale down the cluster.

```console 
docker-compose up --scale worker_1=1 -d
```

## Questions

1. What problems Task-2 deployment strategy solves compared to the strategy adopted in Task-1? 

2. What are the outstanding issues that the deployment strategy of Task-2 cannot not address? What are the possible solutions to address those outstanding issues? 

3. What is the difference between horizontal and vertical scalability? The strategy discussed in Task-2, is it horizontal or vertical scalability? 

-----------------------------

TERMINATE THE SERVER VM STARTED FOR THE TASK-2!

-----------------------------

# Continuous Integration and Continuous Delivery (CI/CD)

I 

## Task-3: Deployment of multiple servers using Ansible

For this task we need three VMs

1. Client VM: This machine will serve as an Ansible host name and initiate the configuration process. 

2. Production Server: The machine will host the dockerised version of the application discussed in previous tasks (1 and 2).

3. Development Server: The machine will host the development environment and push the new changes to the production server. 

### Steps to setup Ansible host and orchestration environment

1. Login to the Client machine

```console 
ssh -i ubuntu@<PRODUCTION-SERVER-IP>
```

2. Goto `technical-training/model-serving/ci_cd` directory. This directory contains the following two sub-directories 

```
/production server 
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
/development server
 - Machine learning Model and Data 
    -- model.h5
    -- model.json
    -- pima-indians-diabetes.csv
    -- neural_net.py
  
```

Open different files and try to understand the application's structure. 

3. Goto the `technical-training/model-serving/openstack-client/single_node_with_docker_ansible_client` directory. This is the code that we will run to contextualize our production server. The code is based on the following files:

```console
- CloudInit files 
  -- prod-cloud-cfg.txt
  -- dev-cloud-cfg.txt
- OpenStack code  
  -- start_instance.py
- Ansible files
  -- setup_var.yml
  -- configuration.yml  
```

The client code will start two VMs and uisng Ansible orchestration environment it will contextualize both of the VMs simultanously. 

4. Installation and configuration of Ansible on the client machine.

4a. First will generate a cluster SSH key.

First check the username you are login as 

```console
whoami
ubuntu
```

you need to be as _ubuntu_ user. If you are _root_ user switch back to _ubuntu_ user. 

Create a directory 

```console
mkdir -p /home/ubuntu/cluster-keys

```


```console
ssh-keygen -t rsa
```

Output

```console
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ubuntu/.ssh/id_rsa): /home/ubuntu/cluster-keys/cluster-key
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/ubuntu/cluster-keys/cluster-key.
Your public key has been saved in /home/ubuntu/cluster-keys/cluster-key.pub.
The key fingerprint is:
4a:dd:0a:c6:35:4e:3f:ed:27:38:8c:74:44:4d:93:67 demo@a
The key's randomart image is:
+--[ RSA 2048]----+
|          .oo.   |
|         .  o.E  |
|        + .  o   |
|     . = = .     |
|      = S = .    |
|     o + = +     |
|      . o + o .  |
|           . o   |
|                 |
+-----------------+
```

Now we have cluster ssh keys at the following location:

1. Private key: `/home/ubuntu/cluster-keys/cluster-key`

2. Public key: `/home/ubuntu/cluster-keys/cluster-key.pub`

4c. Now we start Production and Development servers. But first open `prod-cloud-cfg.txt` delete the old key from the section `ssh_authorized_keys:` and copy the complete contents of `/home/ubuntu/cluster-keys/cluster-key.pub` in the section `ssh_authorized_keys:` 

Repeat same step with the `dev-cloud-cfg.txt`. Delete the old key from the section `ssh_authorized_keys:` and copy the complete contents of `/home/ubuntu/cluster-keys/cluster-key.pub` in the section `ssh_authorized_keys:`

Now run the `start_instance.py` code.

```console
python3 start_instance.py
```
The output will give you the internal IPs of the VMs. 

```console
user authorization completed.
Creating instances ... 
waiting for 10 seconds.. 
Instance: prod_server_with_docker_6225 is in BUILD state, sleeping for 5 seconds more...
Instance: dev_server_6225 is in BUILD state, sleeping for 5 seconds more...
Instance: prod_server_with_docker_6225 is in ACTIVE state, sleeping for 5 seconds more...
Instance: dev_server_6225 is in BUILD state, sleeping for 5 seconds more...
Instance: prod_server_with_docker_6225 is in ACTIVE state ip address: 192.168.1.19
Instance: dev_server_6225 is in ACTIVE state ip address: 192.168.1.17
```
Now we have two VM running with the internal IP addresses.

4b. Install Ansible packages on the client machine. 

```console
sudo bash
apt-add-repository ppa:ansible/ansible
apt update
apt install ansible
```
Now we have ansible packages install. 

i. prod_server_with_docker_6225  -> 192.168.1.19

ii. dev_server_6225 -> 192.168.1.17

4d. Open the Ansible inventory file and add the IP address in that file. For this step you need to swtich to _root_ user.

```console
sudo bash
```

```console
nano  /etc/ansible/hosts
```

file contents

```console
[servers]
prod_server ansible_host=<production server IP address>
dev_server ansible_host=<development server IP address>

[all:vars]
ansible_python_interpreter=/usr/bin/python3

[prod_server]
prod_server ansible_connection=ssh ansible_user=appuser

[dev_server]
dev_server ansible_connection=ssh ansible_user=appuser
```

If you need to learn more about Ansible, here are some useful links: 

Ansible official site 
https://www.ansible.com/

Easy installation instructions
https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-18-04

4e. Just to confirm the access premission are correctly set, access production and development server from the client VM. 

First switch back to user _ubuntu_

```console
ssh -i /home/ubuntu/cluster-keys/cluster-key appuser@<PRODUCTION-SERVER-IP>
```
If the login is successfull, exit from the production server and repeat the step with development server 

```console
ssh -i /home/ubuntu/cluster-keys/cluster-key appuser@<DEVELOPMENT-SERVER-IP>
```
If the login successfull, exit from the development server. 

4f. For this step you need to be login as _ubuntu_ user on the client VM. 

Now we will run the Ansible script available in the `technical-training/model-serving/openstack-client/single_node_with_docker_ansible_client` directory. 

```console
ansible-playbook configuration.yml --private-key=/home/ubuntu/cluster-keys/cluster-key
```
The process will take 10 to 15 minutes to complete. Once the process successfully completed you have both production and development servers ready. 

Attach floating IP address to the production server and access the same web page as we have in previous tasks.  

---------------------------------

## Task-4: CI/CD using Git HOOKS 


0 - SSH key based communication between Production and Development Servers 

  - Login to Development Server 
    
    ```console
    ssh -i cluster-key appuser@<DEVELOPMENT-SERVER-IP>
    ```console
    
  - Generate SSH key 
    
    ```console
    ssh-keygen
    ```console

  NOTE: This step will create two files, private key `/home/appuser/.ssh/id_rsa` and public key `/home/appuser/.ssh/id_rsa.pub`.

  - copy contents of the public key file `/home/appuser/.ssh/id_rsa.pub` from the development server.

  - Login to Production Server
    
    ```console
    ssh -i cluster-key appuser@<PRODUCTION-SERVER-IP>
    ```console

  - Open file `/home/appuser/.ssh/authorized_keys` and past the contents of the public key files. 

     ```console
     nano /home/appuser/.ssh/authorized_keys
     ``` 

1 - Login to the Production Server 

   ```console
   ssh -i cluster-key appuser@<PRODUCTION-SERVER-IP> 
   ```
   
 - Create a directory (it will be jump directory)
   
   ```console
   pwd 
   /home/appuser/
   ```
   
   ```console
   mkdir my_project

   cd my_project
   ``` 
 - Here is the path to your jump directory. Double check that user `appuser` is the owner of `my_project` directory. 
   
   ```console
   pwd
    /home/appuser/my_project       
   ```
   
 - Create git empty directory 
   
   ```console
   git init --bare
   ```
   
   Initialized empty Git repository in `/home/appuser/my_project/`

 - Create a git hook `post-receive`
 
  ```console
  nano hooks/post-receive
  ```
File contents  

```console
#!/bin/bash
while read oldrev newrev ref
do
    if [[ $ref =~ .*/master$ ]];
    then
        echo "Master ref received.  Deploying master branch to production..."
        git --work-tree=/technical-training/model-serving/ci_cd/production_server --git-dir=/home/appuser/my_project checkout -f
    else
        echo "Ref $ref successfully received.  Doing nothing: only the master branch may be deployed on this server."
    fi
done
```


 - Change permissions
 
  ```console
  chmod +x hooks/post-receive
  ```
  
 - Exit Production Server



2 - login to the Development Server

   ```console
   ssh -i cluster-key appuser@<DEVELOPMENT-SERVER-IP>
   ```
   
 - Create a directory

   ```console
   pwd
     /home/appuser/

   mkdir my_project

   cd my_project
   ```

 - This is your development directory. Double check that user `appuser` is the owner of `my_project` directory.

   ```console
   pwd
     /home/appuser/my_project 
   ```
   
 - Create git empty directory

   ```console
   git init
   ```
   
   Initialized empty Git repository in `/home/appuser/project/.git/`

 - Add files model.h5 and  model.json in `/home/appuser/project/` directory. The files are available in `/technical-training/model-serving/ci_cd/development_server/` directory. 

 - Goto `/home/appuser/project` directory
    
 - Add files for the commit 
   
   ```console
   git add .
   ```
   
 - Commit files
 
   ```console
   git commit -m "new model" 
   ```
   
 - connect development server's git to production server's git. 

   ```console
   git remote add production appuser@<PRODUCTIONS-SERVER-IP>:/home/appuser/my_project
   ```
   
 - Push your commits to the production server
   
   ```console
   git push production master
   
   Delta compression using up to 2 threads.
   Compressing objects: 100% (4/4), done.
   Writing objects: 100% (4/4), 2.36 KiB | 2.36 MiB/s, done.
   Total 4 (delta 0), reused 0 (delta 0)
   remote: Master ref received.  Deploying master branch to production...
   To 192.168.1.21:/home/appuser/my_project
   * [new branch]      master -> master 
   ```

For further details visit following link: 
https://www.digitalocean.com/community/tutorials/how-to-use-git-hooks-to-automate-development-and-deployment-tasks
