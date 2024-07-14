# This Automation Framework developed to Learn the full E2E Automation. (Python Scripts, Github, Jenkins etc).

![image](https://github.com/user-attachments/assets/a07fda81-41f4-4d60-97c0-00b9856bb767) Fig. 1

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

## **3. Jenkins:**

When a pull request (PR) is raised, a webhook integrated with Jenkins gets triggered, initiating an automated sequence of actions. This webhook, configured within the version control system, sends a notification to the Jenkins server, prompting it to start a specific job or pipeline. The Jenkins job, upon receiving the trigger, begins by checking out the latest code from the repository associated with the PR. Subsequently, it executes a set of predefined scripts from the automation framework on the designated host. These scripts perform various tasks, such as running tests, building code, or deploying applications, ensuring that the changes introduced by the PR are thoroughly validated. This streamlined process not only enhances efficiency but also ensures that the codebase remains robust and free from integration issues.

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

## **4. Host:**

In our architecture, the host functions as a vital mediator, orchestrating communication between scripts, virtual machines (VMs), and containers through SSH and designated ports. This setup is particularly valuable as we utilize the host to address SSH communication-related APIs, facilitating a deeper understanding of these processes during our learning phase. The host environment may include a diverse array of components, such as:

    -> Linux VMs: Providing robust environments for running applications and services.
    -> Windows VMs: Enabling the execution of Windows-based applications and tools.
    -> Containers: Offering lightweight, portable environments for application deployment and scaling.
    -> Additional Tools: Supporting various utilities that enhance functionality and ease of management.

We can execute scripts directly on the host to carry out a variety of tasks, including fetching data, running system commands, or automating workflows. The OS module plays a crucial role here, allowing for efficient interaction with the underlying operating system, thus streamlining operations and improving overall productivity.

## **5. UI or Web Page or Orchestrator:**

The UI, also referred to as the Web Page or Orchestrator, offers a user-friendly graphical interface that enables efficient monitoring, management, and control of execution processes. Users can interact with the orchestrator to perform a variety of essential tasks, including:

    -> Checking the Status of Builds: Easily monitor the progress and health of builds.
    -> Running Scripts: Execute scripts directly from the interface for seamless integration.
    -> Scheduling Tests: Organize and schedule tests in sequences to optimize workflow.
    -> Storing Logs: Keep records of execution logs for future reference and analysis.
    -> Controlling Execution: Simplify the execution process with straightforward controls.
    -> Managing Resources: Allocate and manage resources effectively to enhance performance.
    -> Viewing Logs: Access detailed logs to troubleshoot and understand system behavior.

This orchestration layer significantly enhances user interaction, providing a comprehensive platform for operational efficiency.


-------------------------------------------------------------------------------------------------------------------------------------
The project is structured into five key phases as highlighted in the above Fig 1:

    1. Host Environment Setup: Begin by establishing the host environment. This involves writing the necessary libraries and scripts to facilitate communication between the host, virtual machines, and containers.

    2. GitHub and Jenkins Configuration: Next, configure GitHub to integrate with Jenkins, enabling seamless interaction between the two platforms.

    3. Host Integration as a Jenkins Node: Integrate the host as a node within Jenkins, setting up triggers that activate automation whenever an action occurs in GitHub.

    4. User Interface Development: Create a user-friendly web interface that allows users to interact with the automation framework effortlessly, providing a graphical means to initiate processes.

    5. UI and Host Integration: Finally, link the user interface with the host, allowing users to trigger the automation framework directly from the web page.
-------------------------------------------------------------------------------------------------------------------------------------
