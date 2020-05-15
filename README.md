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



   
4. Create a simple python script to read and write the file contents:

   Filename - docker_rw.py

   ==> This script executes by taking an input from one file location and writes it to another file on another location.




5. Python script created using Flask web framework to demonstrate a simple web-app with different context paths:

   Filename - python-flask.py


   Pre-requisites of this script:

   5.1 Install and configure pip3 -> pip3 install flask

   5.2 Import the flask module into the script to use the web framework





6. Flask webapp to render HTML contents:

   Filename - python-webapp.py


   Pre-requisites of this script:
   
   6.1 Create a folder named "template" under the source directory structure and place the html contents.

   6.2 Flask looks for the html contents to serve under templa tes directory, when a web request is being hit at the root(home) directory.





7. Flask webapp to integrate with redis in-memory datasore:

   Filename - local-compose-webapp.py


   Pre-requisites of this script:
   
   7.1  Install Redis datastore using the pip3 module and import it in the source.

   7.2  Configure the redis host and port and assign it to a variable.

   7.3  If a web request is being made to the Flask webapp, it increments and stores the value in a particular key at redis.

   7.4  The stored value from a key in redis can be also retrieved and displayed at the web-browser, if a request is made to the particular context path.





8. Implementing the application at dokcer containers using bind/named-volumes volumes mounting:

   Filename - docker-compose-webapp.py
   Filename - dockerfile/Dockerfile & dockerfile/docker-compose.yml-network


   Pre-requisites of this script:
   
   8.1 Deploy multiple docker containers of customised python and redis images and map them with the respective volumes, where the python app has to fetch input/output parameters.

   8.2 Flask application integrates with the redis application usinf redis container name.

   8.3 Redis container must be made dependent of flask application to ensure redis container is up and running before flask app.

   8.4 The corresponding docker files can be found under "dockerfile" folder.This script uses bridge network.





9. Implementing the overlay network on Docker Swarm:

   Filename - docker-compose-webapp.py
   Filename - docker-stack/Dockerfile  &  docker-stack/docker-compose.yml


   Pre-requisites of this script:

   9.1 Setup a docker swarm cluster and add a worker node to it.

   9.2 Create an overlay network to integrate multiple container in multiple hosts and scale applications between them.

   ==>  Create a service by deploying the application using docker stack. The stack when deployed creates an instance of python & redis container with two replica sets on the cluster.






10. Ansible roles created to deploy the applications created in the swarm cluster:

    Folder - ansible_role
    Main playbook -  swarm-init.yml
    Ansible log  -  ansible_swarmcluster.log

    Roles:

    10.1  Creating an ansible role to create the docker swarm cluster

    10.2  Adding a target node to the cluster

    10.3  Creating a service and deploying it in the cluster with docker stack.
