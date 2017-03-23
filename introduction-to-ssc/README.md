# Introduction to SNIC Science Cloud 

In this lab you will learn the basics of how to work with the OpenStack based Infrastructure-as-a-Service (IaaS).  
Estimated time needed to complete the entire lab: 3-5 hours.

## Introduction

The aim of this computer assignment is to give you hands-on experience with the cloud computing infrastructure. The SNIC Science Cloud (SSC) is an SNIC (Swedish National Infrastructure for Computing) national resource that provide Infrastructure-as-a-Service (IaaS). It is based on the OpenStack cloud software (Newton release) and Ceph storage and offers the following services:

1.	Compute (Nova)
2.	Storage (Ephemeral, Cinder)
3.	Identity management (KeyStone)
4.	Image (Glance)
5.	Network (Neutron)
6. 	Orchestration (Heat)
7.	Object Store(Swift)

In this lab you will perform the following five tasks: 

* Task 1: Provisioning a Virtual Machine
* Task 2: Block Storage
* Task 3: Network
* Task 4: Object Storage  
* Task 5: Deploy a simple REST-endopoint enable service: "Cowsay as a Service" 

Please follow the instructions, execute the tasks and answer the related questions. 

### Important links:

1.	Information page: https://cloud.snic.se

The SSC information page contains links to the dashboard, to the OpenStack end-user guide (which you need to consult to complete the tasks below), as well as answers to many of the questions. 

Good Luck!

## Task 0: Create a new SSH-keypair
The only method allowed to access the cloud instances are via ssh-keypairs. Username/Password are disabled by default on all cloud instances (according to best practice) and should never be enabled for security reasons. If you are not familiar with the use of ssh-keys, here is a simple explaination of how it works: http://blakesmith.me/2010/02/08/understanding-public-key-private-key-concepts.html. 

The OpenStack software helps you create/import keys, and will make sure that your public keys are injected in the instaces you create. The private key should be private and is for you to safekeep on your clients. 

1. Create a new SSH-keypair from the Horizon portal (Compute -> Access and Security -> KeyPairs)

## Task 1: Provisioning a Virtual Machine

1.	Start an instance by booting an image of Ubuntu 16.04 with 2 VCPUs (remember to inject the keypair you created in Task 0). Choose the default option "Create New Volume" and choose no for "Delete Volume on Instance Delete" (default). 
2.	Assign a floating IPs to the instance.
3.	Access the instance using a SSH client (or if you are using Windows, using Putty) and install the program “cowsay”.
4.	Open port 4567 on the instance.
5.	Take a volume snapshot of your running instance. 
5.	Terminate the instance. 
6. 	Boot a new instance by booting it from from the recently created volume snapshot. 
7. 	Delete the volume snapshot. 

### Questions:

1.	What is the difference between the private IP and the floating IP that is attached to the instance?
2.	Can you access the Internet from the VM without assigning a floating IP to the machine?
3.	What is the difference between image, instance and snapshot?
4.	What is the name of the OpenStack service responsible for providing the :
	a.	Image Service
	b.	Compute Service
5. 	What is the difference between booting from an image (snapshot) and booting from a volume (snapshot) snapshot? 

## Task 2: Block Storage

1.	Create a volume of size 1GB.
2.	Attach your newly created volume to your instance.
3.	Access the volume and copy a file to the attached volume (hint, you will need to format and mount the volume).
4.	Modify the size of the volume created in step 1.

### Questions:

1.	What is the name of the OpenStack service providing volumes?
2.	What is the technology used to provide volumes in OpenStack? Is it RAID or LVM?
3.	What is LVM? Explain the advantage(s) of using LVM?
4.	Can one volume be attached to multiple instances or vice versa?
5.	Explain the main difference between Ephemeral Storage and Block-Storage. What are the major use-cases for the different storage types?
6.	Does your VM have ephemeral storage?

## Task 3: Network 

### Questions:

1.	Explain the picture in the tab “Network Topology”
2.	What is the subnet used by the Tenant?
3.	What is the role of the router?
4.	Explain the path of the traffic of the VM to the Internet?
5.	Find out the unique ID of the external network.
6.	What is the name of the OpenStack service handling Networks?
 
## Task-4: Object Storage 

1.	Find out the public url of the Container "SNIC-Workshop".
2.	Download the object NIST.pdf from the Horizon dashboard.
3.	From your VM, download NIST.pdf using "curl"
4.	Try to create a container named "testcontainer", did it work? If not, can you see the problem?
 
### Questions:

1.	Explain the difference between a folder on your UNIX filesystem and a pseudo-folder inside a container?
2.	The corresponding system in Amazon Web Services is called "S3". Is there a principal difference between an "S3 bucket" and a container in OpenStack's object store?
3.	What is the name of the OpenStack service providing the Object Store?

## Task-5: Cowsay as a Service

In this task you will deploy a simple service to the benefit to the world. Access
your VM and start by installing the program “cowsay” (use ‘apt-get’). Create a file cowsay-app.py and paste the following code in the file.

```bash
from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)


@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    data=subprocess.check_output(["cowsay","Hello student"])
    return data

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

```
Run:

```bash
# python app.py
```
It will start a webserver on you VM.

If you get any messages about missing packages, just go ahead and install them using “pip” (a Python package management system).

Test that things are working by executing (from your client)

Run: 
```bash
# curl -i http://<your_public_ip>:5000/cowsay/api/v1.0/saysomething
```
If you are using Windows, use a Linux VM or install a cURL client for Windows.

