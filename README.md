This is the small Django project with works with google maps and fusion table.

### Installation ###
**Requirements:** docker and docker-compose.

1) Set env variables:
* `export FUSION_TABLE_ID='your table id'` Add permission for editing table for this user in the `fusiontables.google.com`
* `export KEY_MAP_API='your map api key'`

2) Insert Service Account Credential file with name `ServiceAccountCredentialsFile.json` in the main dir.

3) Run in command line `sh redeploy.sh`

*To stop: `sh redeploy.sh stop`

#### Use case: #### 
* If you click any location on the map: 
    validate that this has a real address and it’s not some wood/mountain/ocean, etc. 
* If valid: 
save it to a simple db table with lat, lon, address (can be single string) and also to google fusion tables (decide what data). 

Have a marker appear instantly after the click on the map based on the google fusion table data. 
Update the list of addresses underneath the map with the location where you clicked. 
Duplicates on google fusion table are not allowed. 
You can reset all data on google fusion tables and the database and start fresh

