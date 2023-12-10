# Ansible Docker Compose deployment

This Ansible code deploys a dockerized application to 2 environments (dev and staging) following production best practices.

## Solution Structure

The application has the following requirements:
- Requires 1GB of RAM and 0.3 cores
- Needs 5GB of storage to run efficiently
- Exposes an API on port 8181
- Utilizes a consistent storage volume (secret-keys-volume) that persists across restarts

Dev Configuration:
- Tuning: true
- Debug: true
- External URL: "https://dev/approve"
- Client: "dev_client_external"
- Interaction Mode: "API"
- Device ID: 2346456


Staging Configuration:
- Tuning: true
- Debug: false
- External URL: "https://staging/approve"
- Client: "staging_client_external"
- Interaction Mode: "API"
- Device ID: 32443532

I've created a **control-node** instance (where **Ansible** is installed) and 2 instances (**dev** and **staging**).
The solution deploys the applications to both environments with different configurations.

Folder structure:
```
/app
    app.py
    Dockerfile
    my-site.conf
    my-site.crt
    my-site.key
    nginx.conf
    requirements.txt
    
/files
    docker-compose.yaml.j2

/group_vars
    servers.yaml

/host_vars
    dev.yaml
    staging.yaml

/roles
    /docker

inventory.ini
playbook.yaml
```

I've installed the docker role from Ansible Galaxy, it installs Docker and Docker Compose in the target servers.
In **./roles/docker/defaults/main.yaml** we can configure the ubuntu user to be included in the docker group to be able to run docker.

```console
ansible-galaxy role install geerlingguy.docker --roles-path ./roles 
```

- **./app** Includes the Python app, Dockerfile, SSL certificates and requirements to be installed by pip.

- **playbook.yaml** has the tasks that we apply to the hosts in **inventory.ini**.

- **./group_vars** includes the common variables for both environments.

- **./host_vars** includes variables specific for each environment.

- **./host_vars/docker-compose.yaml.j2** is the template used to build the docker-compose specific for each environment

## Application

The application is a simple flask Python app that listens on port 8181. To deploy the app I use a docker-compose file with Jinja templates with variables per environment.
The docker compose uses an image previously built with Dockerfile and pushed to Docker Hub, another option would be to build the app locally.

```
docker buildx build --platform linux/amd64 -t adriannavarro/app:latest . 
```
```
docker push adriannavarro/app:latest
```

The docker compose has also a nginx image with a self-signed certificate to be able to listen in port 443. It acts as a proxy to be able to scale the app.

```console
{"message":"Hello from https://${ENV}/approve!"}
``````

<img src="dev.png" width="600">

<img src="staging.png" width="600">

## How to run it

Execute playbook:

````
ansible-playbook -i inventory.ini playbook.yaml
``````
## Improvements

- The app only uses one environment variable (EXTERNAL_URL), it should obviously use all the rest in a real scenario.
- ngnix uses a self-signed certificate, we could use Let's Encrypt for example to avoid certificate issues.
- The way I scale the service is arguably not the best, I should use **community.docker.docker_compose native** task to do it. Using imperative bash commands is not recommended in Ansible, but I ran into issues and couldn't make it work with the native solution.


## Conclusion

This Ansible solution follows industry best practices for deploying applications to different environments. It uses variables to apply different configurations per environment, uses roles from Ansible Galaxy to organize the code better and uses secure ports to access the application.

