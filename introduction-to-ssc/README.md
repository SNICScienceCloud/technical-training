# Introduction to SNIC Science Cloud 

In this lab you will learn the basics of how to work with the OpenStack based Infrastructure-as-a-Service (IaaS).  
Estimated time needed to complete the entire lab: 3-5 hours.

## Introduction

The aim of this computer assignment is to give you hands-on experience with the cloud computing infrastructure. Currently the SNIC cloud is an UPPMAX (Uppsala Multidisciplinary Center for Advanced Computational Science) resource that provide Infrastructure-as-a-Service (IaaS). It is based on the OpenStack cloud software (Kilo release) and Ceph storage and offers the following services:

1.	Compute (Nova)
2.	Storage (Ephemeral, Cinder)
3.	Identity management (KeyStone)
4.	Image (Glance)
5.	Network (Neutron)
6.	Object Store(Swift)

Together with this lab description, this lab is based on code in the following tasks: 

* Task-1: Provisioning a Virtual Machine
* Task 2: Block Storage
* Task 3: Network
* Task 4: Object Storage  
* Task 5: Cowsay as a Service

Please follow the instructions, execute the tasks and answer the related questions. 

### Important links:

1.	Information page: http://cloud.snic.se
2.	User Guide: http://www.uppmax.uu.se/smog-user-guide
3.	Dashboard: http://horizon.cloud.snic.se

Good Luck!

### Task-1: Provisioning a Virtual Machine

1.	Start an instance of Ubuntu 14.04 with 2 VCPUs.
2.	Assign a floating IPs to the instance.
3.	Access the instance using the SSH client (or if you are using Windows, using Putty) and install the program “cowsay”
4.	Open port 4567 on the instance.
5.	Create a snapshot of the instance.

````bash	
export OS_USER_DOMAIN_NAME="Default"
export OS_IDENTITY_API_VERSION="3"
export OS_PROJECT_DOMAIN_NAME="Default"
```
4.	Set the environment variables by sourcing the RC-file:
```bash
source <project_name>_openrc.sh
```

### Questions:

1.	What is the difference between the private IP and the floating IP?
2.	Can you access the Internet from the VM without assigning a floating IP to the machine?
3.	What is the difference between image, instance and snapshot?
4.	What is the name of the OpenStack service responsible for providing the :
	a.	Image Service
	b.	Compute Service


### Task-2: Block Storage

1.	Create a volume of size 1GB.
2.	Attach your newly created volume to your instance.
3.	Access the volume and copy a file to the attached volume.
4.	Modify the size of the volume created in step 1.
5.	What is the name of the OpenStack service providing volumes?

### Questions:

1.	What is the technology used to provide volumes in OpenStack? Is it RAID or LVM?
2.	What is LVM? Explain the advantage(s) of using LVM?
3.	Can one volume be attached to multiple instances or vice versa?
4.	Explain the main difference between Ephemeral Storage and Block-Storage. What are the major use-cases for the different storage types?
5.	Does your VM have ephemeral storage?

### Task-3: Network 

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

# Task-5: Cowsay as a Service

In this task you will deploy a simple service to the benefit to the world. Access
your VM and start by installing the program “cowsay” (use ‘apt-get’). Create a file cowsay-app.py and past the following code in the file.

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

If you get any messages about missing packages, just go ahead and install the using “pip” (a Python package management system).

Test that things are working by executing (from your client)

Run: 
```bash
# curl -i http://<your_public_ip>:5000/cowsay/api/v1.0/saysomething
```
If you are using Windows, use a Linux VM or install a cURL client for Windows.

