# Basic contextualization and orchestration 

In this lab you will learn the basics of how to automatically configure instances and how to automate and orchestrate deployment of single resources as well as more complex stacks.  

Estimated time needed to complete the entire lab: 3-5 hours.

## Introduction

The aim of this tutorial is to give you hands-on experience with the service contextualization and orchestration. The lab will provide a brief introduction to different tools that can be used for efficient resource-provisioning. This forms a foundation for automated, robust and reprodicible resource management in the SNIC Science Cloud. SSC is based on the Liberty release of OpenStack and offers the follwing core services: 

1.	Compute (Nova)
2.	Storage (Ephemeral, Cinder)
3.	Identity management (KeyStone)
4.	Image (Glance)
5.	Network (Neutron)
6.	Orchestration (Heat) 
7.	Object Storage (Swift)

Together with this lab description, this lab is based on code in the following tasks: 

* Task 1: OpenStack-API
* Task 2: CloudInit-Contextualization
* Task 3: Ansible-Contextualization
* Task 4: Heat-Orchestration  
* Task 5: Containers 

Please follow the instructions, execute the tasks and answer the related questions. 

### Important links:

1.	Information page: http://cloud.snic.se
2.	User Guide: https://docs.openstack.org/horizon/pike/user/ , https://docs.openstack.org/python-novaclient/pike/
3.	SNIC Science Cloud (SSC): https://cloud.snic.se

Good Luck!

## Task-0: Setting the environment for API access

Install Openstack libraries on your test virtual machine,
 
1.	Goto https://docs.openstack.org/install-guide/environment-packages-ubuntu.html , http://docs.openstack.org/cli-reference/common/cli_install_openstack_command_line_clients.html
and download the client tools and API for OpenStack. 
2.	Download the Runtime Configuration (RC) file from the SSC site (Project->Compute->Access & Security->API Access->Download OpenStack RC File).
3. Confirm that your RC file have following enviroment variables:

```bash	

export OS_USER_DOMAIN_NAME="snic"
export OS_IDENTITY_API_VERSION="3"
export OS_PROJECT_DOMAIN_NAME="snic"
```

4.	Set the environment variables by sourcing the RC-file:

```bash 

source <project_name>_openrc.sh
```
5. Run the following commands and explain the output:

```bash

openstack server list
openstack image list
```

### Questions:

1.	What version of the API are we using? 
2.	Explain how the communication works in OpenStack?
3.	Can we use EC2 and S3 APIs to communicate with OpenStack?

## Task-1: Resource provisioning using CLIs and APIs

Use the command-line interface (CLI) tools as well as the python APIs (example coode is available in OpenStack-API directory) to achieve following tasks: 

*Note: you need to edit the Python files (in the OpenStack-API folder) and enter your key-name, private-network and floating IP information.*

4.	List available images
5.	List running instances
6.	Boot a new instance
7.	Modify the code to boot multiple instances 
8.	Attach a floating IP and connect via SSH
9.	Write python code to terminate the instance  
10.	 Contextualize the instance at boot time. Code is available in “nova/add-userdata” directory

### Questions:

1.	What is the difference between the private IP and the floating IP?
2.	Can you access the Internet from the VM without assigning a floating IP to the machine?
3.	Explain the arguements to the function used in Python to boot a single instance?

## Task-2: Single-machine contextualization

*NOTE: The code assumes Ubuntu VMs.*
The code for this task is in  the folder "contextualization".

The following link provides an introduction to Cloudinit 

https://help.ubuntu.com/community/CloudInit

In this task you will prepare a single instance to install packages and start a web-service “cowsay” on the instance.  The configuration is done by CloudInit package. Run the code, It will prepare the instance at boot time. Once the instance will be running, Test that things are working by executing (from your client)

In this task, you will prepare a script that automatically installs packages and starts the web-service “cowsay” on a single instance.
The configuration is done by the CloudInit package, read and try to understand *cloud-cfg.txt* that you can find in the “contextualization” folder.

The file *ssc-instance-user-data.py* , in the same folder is used to start the instance. Open the file, try to understand it.

The python file is not complete, make the necessary changes, run the file and see if your instance is created. Test that the server is working by executing following curl command:

```bash

curl -i http://<your_public_ip>:5000/cowsay/api/v1.0/saysomething

```

If you are using Windows, use a Linux VM or install a cURL client for Windows.
 
### Questions:

1.	Explain the output?
2.	What is contextualization? 
3.	What language is use to prepare CloudInit configurations?  
4.	What are the variants of CloudInit package?  
5.	Can we run CloudInit scripts without booting an instance? 
6.	What limitation you can anticipate with the CloudInit package?

## Task-3: Cluster contextualization

*NOTE: The code assumes Ubuntu VMs.*

In this task we will configure a Spark cluster using Ansible. Ansible is an open source  IT-automation engine that can be used to automate provisioning, configuration and deployment of cloud resurces. First, start two virtual machines based on Ubuntu:

* ansible-node
* sparkmaster

copy the “ansible-spark” directory to the ansible-node. Run the “install_ansible.sh” script. Then configure the Ansible setup with the following steps (all executed on the ansible-node):

1.	Generate a SSH key-pair, # ssh-keygen –t rsa
2.	Add the public key to both of the hosts “authorized_keys” file. 
3.	Make sure you can login to the machines. Also check that the user account has the “sudo” privileges.
4.	Open the ““/home/ubuntu/spark/hosts” file and fill the private IP addresses of the nodes.  
5.	Goto “/home/ubuntu/spark” directory and execute the following command:

```bash

ansible-playbook -i hosts -s playbooks/spark-deployment.yml   

```

The complete deployment will take approximately 20 to 30 minutes. Once the installation is finished you can check the cluster status using the following URL: 

http://<floating-IP-sparkmaster>:8080
 
### Questions:

1.	What language is used by Ansible to define the configurations? 
2.	Can Ansible be used with different Linux distributions? 
3.	What is Ansible inventory file?
4.	What is the major difference between CloudInit vs Ansible-based resource contextualization?
5.	Explain how Ansible works and suggest, within the scope of this task, what is still left to automate?  

## Task-4: Orchestration using Heat

In this task you will create a cluster of two machines using the Heat engine. Heat is OpenStack's native orcherstation engine and will  let you automate the deployment of complex resources/stacks. The cluster will be completely customized by having its own network, security group, router settings and resources. Complete the following steps to provide the required information in the template file :

1.	Enter your personal key name by replacing the “key” section’s default value.
2.	Generate a SSH key-pair, # ssh-keygen –t rsa
3.	Replace “<ADD-CLUSTER’s-PUBLIC-KEY>” with the public part of the generated key pair. Replace it for both of the instances.
4.	Run the command

```bash

openstack stack create stack_with_init_script -f ‘yaml’ -t ssc-test-stack.yml 
```

5.	Open the SSC dashboard and click on the Orchestration and check the status of your stack.  
 
### Questions:

1.	What language is used with the Heat service to define the templates?
2.	What are the advantages of using templates rather than the APIs?
3.	Explain the different sections in the templates?

## Task-5: Introduction to Linux Containers

This task will introduce you to Linux containers. There are different technologies available but in this Lab, we will focus on Docker containers. Your task is to build and run CSaaS service using Docker containers.

#### Step-1: Install Docker on your VM.

0 - Switch to the root user:
```bash
> sudo bash
```

1 - First, add the GPG key for the official Docker repository to the system:
```bash
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

2 - Add the Docker repository to APT sources:
```bash
# add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

3 - Update the package database with the Docker packages from the newly added repo:
```bash
# apt-get update
```
4 - Install Docker:
```bash
# apt-get install -y docker-ce
```

5 - (Optional) Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:
```bash
# systemctl status docker
```

For more information visit: 

http://docker.com 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
 
#### Step - 2: Use the Dockerfile available in the repository (container directory) and build your own container. 

1 - Go to the container directory 
```bash
# cd container
```
2 - Execute the docker build and run commands 
```bash
# docker build -t cowsay:latest .
```
```bash
# docker run -it cowsay
```
Or
```bash
# docker run -d -p 5000:5000  cowsay
```

#### Step - 3: Test that service is available by executing (from your client)
```bash
$ curl -i http://<your_public_ip>:5000/cowsay/api/v1.0/saysomething  
```

### Questions:

1. In what category of virtualization do containers fall?
2. What are the other frameworks that provide container technology. Write at least two name. 
3. Explain the provided Dockerfile. What does it do? How does it work? Write a brief (one line) description about each line in the Dockerfile.    
4. Write a brief (one line) description about each command used in Step-2-2.
5. What is dockerhub? Write a brief description of how can we use dockerhub for our newly build CSaaS container?   
6. Write a CloudInit script that contextualize a VM based on the steps (Step-1 and 2) mentioned in this task. Submit the script with your assignment report.

## Where to go from here? 
Why not check out how to [create Kubernetes cluster using KubeNow](https://github.com/kubenow/KubeNow)? 
