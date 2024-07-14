# This Automation Framework developed to Learn the full E2E Automation. (Python Scripts, Github, Jenkins etc).

![image](https://github.com/user-attachments/assets/a07fda81-41f4-4d60-97c0-00b9856bb767)


The idea behind this project is to Automate whole procees so that all concept gets clear...

## So, now lets start describing all detailes of the above Diagram:-

## **1. Developers:**

### Role: 
    -> Developers are responsible for writing, testing, and committing code.
    -> Interaction: They interact directly with the codebase stored in GitHub. 
    -> Developers write code for new features, bug fixes, and improvements. This involves using programming languages, frameworks, and libraries relevant to the project.

Once the Developers pushed any changes to the Github then several Action will be taken care by the GitHub special Features.
 
## **2. GitHub:**

GitHub serves as a powerful repository platform for hosting and version-controlling code, This Automated framework offers an organized and structured framework that includes essential core libraries such as - 

      -> SSH utility, 
      -> host execution utility, 
      -> config utility, 
      -> VM utility, and 
      -> various other utilities. 

These core libraries are integral to the functionality of test scripts, which leverage them to execute tasks. 

Developers write scripts for different test scenarios and push the code to GitHub, where further actions are automated by GitHub Actions. 
This automation pipeline ensures code quality and consistency by performing several checks:

      -> verifying code standards, 
      -> enforcing pylint standards, 
      -> running pre-commit checks, 
      -> obtaining reviewer approvals, and 
      -> incorporating additional features to enhance the framework. 
      
The test scripts execute on the Host, communicating with VMs via SSH and interacting with the host using Python modules, ensuring a seamless and efficient testing and deployment process.

When a pull request (PR) is raised, a webhook integrated with Jenkins gets triggered, initiating an automated sequence of actions. This webhook, configured within the version control system, sends a notification to the Jenkins server, prompting it to start a specific job or pipeline. The Jenkins job, upon receiving the trigger, begins by checking out the latest code from the repository associated with the PR. Subsequently, it executes a set of predefined scripts from the automation framework on the designated host. These scripts perform various tasks, such as running tests, building code, or deploying applications, ensuring that the changes introduced by the PR are thoroughly validated. This streamlined process not only enhances efficiency but also ensures that the codebase remains robust and free from integration issues.

## **3. Jenkins:**

When a pull request (PR) is raised:

     -> A webhook integrated with Jenkins gets triggered.
     -> The webhook, configured in the version control system, notifies the Jenkins server.

Upon receiving the trigger:

    -> Jenkins starts a specific job or pipeline.
    -> The Jenkins job checks out the latest code from the repository associated with the PR.

Execution of scripts:

    -> Predefined scripts from the automation framework are executed on the designated host.
    -> These scripts perform tasks like running tests, building code, or deploying applications.

Benefits:

    -> Ensures changes introduced by the PR are thoroughly validated.
    -> Enhances efficiency.
    -> Maintains the robustness and integration integrity of the codebase.

4. Host:

Function: The host machine acts as the central orchestrator for deploying applications.
Components Managed:
Virtual Machines (VMs):
VM 1 (Linux): A virtual environment running a Linux operating system.
VM 2 (Windows): A virtual environment running a Windows operating system.
Container: A containerized environment for application deployment, which can provide a consistent environment across different stages of development and production.
SSH Connection: Jenkins uses SSH to securely communicate and execute commands on the Host.
5. Virtual Machines and Containers:

Purpose: To provide isolated and consistent environments for deploying and running applications.
Configuration:
VM 1 (Linux): Suitable for applications or services that run on Linux.
VM 2 (Windows): Suitable for applications or services that require a Windows environment.
Container: Lightweight and portable environment ideal for microservices and cloud-native applications.
6. UI or Web Page or Orchestrator:

Function: Provides a graphical interface or web-based platform to monitor, manage, and control the entire CI/CD pipeline.
Interaction: Users can interact with the orchestrator to:
Monitor: Check the status of builds, tests, and deployments.
Control: Start, stop, or rerun processes as needed.
Manage: Configure settings, view logs, and manage resources.
