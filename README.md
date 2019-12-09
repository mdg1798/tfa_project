# Squirrel Tracker

![Adorable Squirel ](https://user-images.githubusercontent.com/56944956/70470451-e1d19900-1a7f-11ea-8af1-b39bddc81373.jpg)


## One Stop Solution to Track Squirrels
Our Project is a web application to keep track of all the known squirrels within Central Park in New york. The application is based on 2018 Central Park Squirrel Census data and the user == YOU! can add, update, and view squirrel data. 

## Data Source

Users can import the 2018 Central Park Squirrel Census data by using the command:

`python manage.py import_squirrel_data /path/to/file.csv`

Also, users can export the data in csv format with this command:

`python manage.py export_squirrel_data /path/to/file.csv`


## Functions

Map
url: /map
The map displays the location of squirrel sightings. You can see locations of 100 squirrels on the map.

Sightings
url: /sightings
List all squirrel sightings with links to edit each as well as a single link at the top to add a new sighting.

Updation
url: sightings/<unique_squirrel_id>
View, edit and update a particular sighting.

Adding new Squirrel
url: sightings/add
Create a new squirrel sighting.

Stats
url: sightings/stats
Show general stats(e.g. Location, Age, Latitude, Longitude and Primary Fur Color) about the sightings.


### Group Information
Project Group 16, Section 2

Uni = [mdg2197, nm3147]

### Link To App
https://dynamic-nomad-255500.appspot.com/



