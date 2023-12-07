# satoshi-ansible
Ansible Assessment


Scenario:
A project's app development phase has concluded, and they're ready to deploy their app image to two environments: dev and staging.

The app image comes with specific requirements and configurations for each environment. Your task is to deploy three instances of the app image on two hosts using Ansible, while adhering to production best practices.

Requirements:
Deploy three instances of the app image on each host (dev:host1, staging:host2) using Docker Compose.

dev:host1
staging:host2

Ensure that each app instance meets the following criteria:
Requires 1GB of RAM and 0.3 cores
Needs 5GB of storage to run efficiently
Exposes an API on port 8181
Utilizes a consistent storage volume (secret-keys-volume) that persists across restarts

Configure the instances according to the provided environment-specific properties and settings:

Dev Configuration:
    Tuning: true
    Debug: true
    External URL: "https://dev/approve"
    Client: "dev_client_external"
    Interaction Mode: "API"
    Device ID: 2346456


Staging Configuration:
    Tuning: true
    Debug: false
    External URL: "https://staging/approve"
    Client: "staging_client_external"
    Interaction Mode: "API"
    Device ID: 32443532

Ensure that all app instances are reachable from the local environment on their respective ports.

Write the Ansible code following best practices for both Ansible and production deployment.
 
Evaluation Criteria:

Best Practices: Demonstrated adherence to best practices in security and scalability, ensuring that the Ansible code aligns with production standards.
Deployment: Successful deployment of three instances of the application on dev:host1 and staging:host2 using Docker Compose.
Resource Fulfillment: Ensuring that each app instance satisfies the specified resource requirements and environment configurations.
Storage Management: Proper establishment of a consistent storage volume (secret-keys-volume) for the app instances, maintaining data integrity across restarts.
Accessibility: Verification that all app instances are accessible from the local environment through their designated ports.
Ansible Proficiency: Utilization of Ansible best practices, including a well-structured playbook and clearly defined tasks.
Dynamic Configuration: Skillful use of templates for dynamic configuration within the Ansible playbook.
Documentation: Provision of comprehensive documentation that offers insights into design choices, assumptions, and code organization.
Production Considerations:Thoughtful consideration of production best practices, encompassing aspects of security, scalability, and maintainability in the Ansible deployment.