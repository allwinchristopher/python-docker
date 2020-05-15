# POC for simple Python web application using Containarisation with Docker and deployment using Ansible.

1. Install the required pre-requisites:

    -> python3
    -> wget
    -> elinks
      
2. Install docker-ce 18 or 19 and enable the docker services at system startup:

   -> yum install -y yum-utils device-mapper-persistent-data lvm2
   -> yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
   -> yum install -y docker
   -> systemctl start docker
   -> systemctl enable docker
   
3. Verify the docker version:
   
   -> dokcer version
   
4. 

