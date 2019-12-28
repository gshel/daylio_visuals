#Project Title
For Daylio users who want to explore and interact with their data without spreadsheets.
##Tech
This project makes use of the following:

* Git
    * https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* Docker-compose
    * https://docs.docker.com/compose/install/
* Python 3.6
    * https://realpython.com/installing-python/
* Elasticsearch
    * Installed and configured by Docker-compose. It is also ephemeral, meaning that once the docker-compose command is stopped, Elasticsearch will no longer be accessible on your machine and changes you've made will be lost..
* Kibana
    * Installed and configured by Docker-compose. It is also ephemeral, meaning that once the docker-compose command is stopped, Kibana will no longer be accessible on your machine and changes you've made will be lost.

##Getting Started

###Export Daylio Data
In your Daylio mobile app, follow these steps:
1. Tap 'More'
2. Tap 'Export Entries'
3. Select 'CSV (table)'
4. Send the .csv to yourself so that it is accessible from your computer
5. Download the .csv to your computer

###OS-specific Instructions
####Linux
1. Clone this repository 
    
    ```$ git clone https://github.com/gshel/daylio_visuals.git```
    
2. Change to local project repo's root directory 
    
    ```$ cd daylio_visuals```
    
3. Move exported data into your local project repo 
    
    ```$ mv <RELATIVE_PATH_TO_CSV>/daylio_export.csv .```
    
4. Run the following command to start Elasticsearch and Kibana locally 
    
    ```$ docker-compose up```
    
    :warning: As long as this terminal is up, you will be able to access Elasticsearch and Kibana. If the terminal is closed, you'll need to repeat this process from this step onwards. 
    
5. Open a new terminal
6. Run the following command 
    
    ```$ python3 csv_to_es.py```
7. [Go to the `Kibana Configuration` section to continue](README.md#kibana-configuration)

####Mac
TODO

####Windows 10
TODO

###Kibana Configuration
1. Open your browser and navigate to Kibana at `localhost:5601`
2. On the left-side of Kibana find and click on `Management`
3. Under Kibana, click `Index Patterns`
4. Click `Create index pattern`
5. For Step 1, enter `daylio*` into the `Index pattern` field
6. For Step 2, select `datetime` from the `Time Filter field name` drop-down
7. Click `Create index pattern`

Congrats, setup complete! On the left-side of Kibana, find and click on `Visualizations` to start exploring.
