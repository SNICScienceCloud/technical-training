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

Together with this lab description, this lab is based on code in thefollowing five sub-directories: 

Task 1: OpenStack-API
Task 2: CloudInit-Contextualization
Task 3: Ansible-Contextualization
Task 4: Heat-Orchestration  
Task 5: Containers 

Please follow the instructions, execute the tasks and answer the related questions. 

### Important links:

1.	Information page: http://cloud.snic.se
2.	User Guide: http://www.uppmax.uu.se/smog-user-guide
3.	Dashboard: http://horizon.cloud.snic.se

Good Luck!

## Task-0: Setting the environement for API access

Install Openstack libraries on your local machine,
 
1.	Goto http://docs.openstack.org/cli-reference/common/cli_install_openstack_command_line_clients.html
and download the client tools and API for OpenStack. 
2.	Download the Runtime Configuration (RC) file from the SSC site (Project->Compute->Access & Security->API Access->Download OpenStack RC File).
3.	Set the environment variables by sourcing the RC-file:
```bash
source <project_name>_openrc.sh
```

### Questions:

1.	What version of the API are we using? 
2.	Explain how the communication works in OpenStack?
3.	Can we use EC2 and S3 APIs to communicate with OpenStack?

Task-1: Resource provisioning using CLIs and APIs

Use the command-line interface (CLI) tools as well as the python APIs (example coode is available in OpenStack-API directory) to achieve following tasks: 

*Note: you need to edit the Python files and enter your key-name, private-network and floating IP information.*

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

## Task-2 (Single-machine contextualization)

*NOTE: The code assumes Ubuntu VMs.*

The following link provides an introduction to Cloudinit 

https://help.ubuntu.com/community/CloudInit

In this task you will prepare a single instance to install packages and start a web-service “cowsay” on the instance.  The configuration is done by CloudInit package. Run the code, It will prepare the instance at boot time. Once the instance will be running, Test that things are working by executing (from your client)

curl -i http://<your_public_ip>:5000/cowsay/api/v1.0/saysomething

If you are using Windows, use a Linux VM or install a cURL client for Windows.
 
### Questions:

1.	Explain the output?
2.	 What is contextualization? 
3.	What Language is use to prepare CloudInit configurations?  
4.	What are the variants of CloudInit package?  
5.	Can we run CloudInit scripts without booting an instance? 
6.	What limitation you can anticipate with CloudInit package?

## Task-3: Cluster contextualization

*NOTE: The code assumes Ubuntu VMs.*

In this task we will configure a Spark cluster using Ansible. Ansible is an open source  IT-automation engine that can be used to automate provisioning, configuration and deployment of cloud resurces. First, start two virtual machines based on Ubuntu:

•	ansible-node
•	sparkmaster

copy the “ansible-spark” directory to the ansible-node. Run the “install_ansible.sh” script. Then configure the Ansible setup with the following steps (all executed on the ansible-node):

1.	Generate a SSH key-pair, # ssh-keygen –t rsa
2.	Add the public key to both of the hosts “authorized_keys” file. 
3.	Make sure you can login to the machines. Also check that the user account has the “sudo” privileges.
4.	Open the ““/home/ubuntu/spark/hosts” file and fill the private IP addresses of the nodes.  
5.	Goto “/home/ubuntu/spark” directory and execute the following command:

    ansible-playbook -i hosts -s playbooks/spark-deployment.yml   

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
    # heat stack-create stack_with_init_script -f ssc-test-stack.yaml
5.	Open the SSC dashboard and click on the Orchestration and check the status of your stack.  
 
### Questions:

1.	What language is used with the Heat service to define the templates?
2.	What are the advantages of using templates rather than the APIs?
3.	Explain the different sections in the templates?

## Task-5 (Introduction to Linux Containers)

This task will introduce you to Linux containers. There are different technologies available but in this lab we will focus on LXC containers. Follow the instructions available on the following page: 

https://linuxcontainers.org/lxc/getting-started/

Start two unprivileged containers with the following parameters: 

1.	Distribution: Ubuntu, Release: trusty, Architecture: amd64
2.	Distribution: Ubuntu, Release: trusty, Architecture: i386

### Questions:

1.	In what category of virtualization does containers fall?
2.	How does LXC compate to other popular container technologies such as Docker?  

## Where to go from here? 
Why not check out how to [use Heat to deploy a Kubernetes cluster in SSC](https://github.com/SNICScienceCloud/catalystcloud-orchestration/tree/config-for-ssc/hot/ubuntu-14.04/kubernetes)? 
