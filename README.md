![](https://github.com/gshel/daylio_visuals/workflows/static/badge.svg)

# Daylio Visuals
For Daylio users who want to explore and interact with their data without spreadsheets.

## Getting Started
_Table of Contents_
* [Daylio](README.md#daylio)
* [Setup](README.md#setup)
    * [Linux](README.md#linux)
    * [Mac](README.md#mac)
    * [Windows 10](README.md#windows-10)
* [Kibana](README.md#kibana)
    * [Configure](README.md#configure)
    * [Visualize](README.md#visualize)
* [Contribute](README.md#contribute)
### Daylio
In your Daylio mobile app, follow these steps:
1. Tap 'More'
2. Tap 'Export Entries'
3. Select 'CSV (table)'
4. Send the .csv to yourself so that it is accessible from your computer
5. Download the .csv to your computer

### Setup
#### Linux
1. Install the following to continue
    * [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/#_installing_on_linux)
    * [Python3](https://realpython.com/installing-python/#linux)
    * [Docker](https://docs.docker.com/install/)
    * [Docker-compose](https://docs.docker.com/compose/install/)
    
2. Clone this repository from Github
    
    ```$ git clone https://github.com/gshel/daylio_visuals.git```
    
3. Change to local project repository's root directory 
    
    ```$ cd <PATH_CLONED_REPO>/daylio_visuals```
    
4. Move exported data into your local project repo 
    
    ```$ mv <PATH_TO_CSV>/daylio_export.csv .```
    
5. Run the following command, starting Elasticsearch + Kibana locally 
    
    ```$ docker-compose up```
    
    :warning: As long as this terminal is up, you will be able to access Elasticsearch and Kibana. If the terminal is closed, you'll need to repeat the process from this step onwards. 

6. Verify that Elasticsearch + Kibana have successfully started -> http://localhost:5601

7. Open a new terminal

8. Run the following commands 
    
    ```
    $ pip3 install -r requirements.txt 
    $ python3 csv_to_es.py
   ```
    
9. [Configure Kibana](README.md#kibana)

#### Mac
1. Install the following to continue
    * [Git](https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop)
    * [Python3](https://realpython.com/installing-python/#macos-mac-os-x)
    * [Docker Desktop](https://docs.docker.com/docker-for-mac/install/)

2. Verify Docker Desktop installation

    ```$ docker --version```

3. [Clone this repository](https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop)

4. Open up a terminal window

5. Change to local project repository's root directory
    
    ```$ cd ~/Documents/Github/daylio_visuals```
    
6. Move exported data into your local project repo 
    
    ```$ mv <PATH_TO_CSV>/daylio_export.csv .```
    
7. Run the following command, starting Elasticsearch + Kibana locally 
    
    ```> docker-compose up```
    
    :warning: As long as this terminal is up, you will be able to access Elasticsearch and Kibana. If the terminal is closed, you'll need to repeat the process from this step onwards. 

8. Verify that Elasticsearch + Kibana have successfully started -> http://localhost:5601

9. Open a new terminal

10. Run the following commands 
    
    ```
    $ pip3 install -r requirements.txt 
    $ python3 csv_to_es.py
    ```
    
11. [Configure Kibana](README.md#kibana)

#### Windows 10
1. Install the following to continue
    * [Github Desktop](https://help.github.com/en/desktop/getting-started-with-github-desktop/installing-github-desktop)
    * [Python3](https://www.microsoft.com/en-us/p/python-37/9nj46sx7x90p)
    * [Docker Desktop](https://docs.docker.com/docker-for-windows/install/)
    
    :warning: For Docker to run properly on Windows, [Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v) and [Virtualization](https://docs.docker.com/docker-for-windows/troubleshoot/#virtualization-must-be-enabled) **must** be enabled.
2. Verify that Docker is properly installed

    ```> docker version```
    
    :warning:  don't copy/paste the "> ", otherwise the command won't work! This is just to show that you're entering the command into Microsoft Powershell.

3. [Clone this repository](https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop)
    
4. Open up Microsoft Powershell as an administrator 
 
5. Change to local project repository's root directory
    
    ```> cd C:\Users\%UserProfile%\Documents\Github\daylio_visuals```

6. Move your Daylio export into the repository's root directory

7. Run the following command, starting Elasticsearch + Kibana locally 
    
    ```> docker-compose up```
    
    :warning: As long as this terminal is up, you will be able to access Elasticsearch and Kibana. If the terminal is closed, you'll need to repeat the process from this step onwards. 
 
8. Verify that Elasticsearch + Kibana have successfully started -> http://localhost:5601

9. Open a new window of Powershell as an administrator

10. Run the following commands 
    
    ```
    > pip install -r requirements.txt 
    > python csv_to_es.py
    ```
    
12. [Configure Kibana](README.md#kibana)
### Kibana
#### Configure
1. Open your browser and navigate to Kibana at http://localhost:5601
2. On the left-side of Kibana find and click on `Management`
3. Under Kibana, click `Index Patterns`
4. Click `Create index pattern`
5. For Step 1, enter `daylio*` into the `Index pattern` field
6. For Step 2, select `datetime` from the `Time Filter field name` drop-down
7. Click `Create index pattern`

Congrats, setup complete! 
#### Visualize
On the left-side of Kibana, find and click on `Visualizations` to start exploring.

### Contribute
Have any suggestions on how to improve this project? 

Even if it's just a suggestion on rephrasing, your input is appreciated! Feel free to reach out by starting an issue in the GitHub repository. If you're new to programming, I'd be happy to show you how to submit a Pull Request! 
#### Special Thanks to...
Thank you to those of you who acted as a guinea pig so that others could have an easier time setting this up!
* stebo02

#### Join the community
Join the community at [r/Daylio](https://www.reddit.com/r/daylio) on Reddit!
