# Coordinate Distance Calculator

This is a Python program that computes the distance between two real world objects in different measure of distance. 

## Project Specification

The distance between two coordinates will be computed based on longitude and latitudes angles in three geometric and unit of distance contexts.
These three versions will be given in three different packages: Package1, Package2, and Package3.

1. In the first version, Package1, two files exist: Application.py and position.py. The Application.py file contains a method to call another method in Position object to compute distance between coordinates in the three contexts. The position.py file gives the classes necessary to compute coordinate distance in the first context as follows:

    * Given two coordinates, given by latitude and longitude, and the radius of the Earth, determine distance between the coordinates in statute miles and planar geometry (equirectangular flat-Earth approximation). The formula to compute this distance is shown here:
    
       ![Tex2Img_1652328689](https://user-images.githubusercontent.com/105037989/167990578-1c6deb71-09d2-4933-a85d-e7e9676c142e.jpeg) where R is the radius of the Earth, x is the term given by the formula ***x = (longitude2 - longitude1) * cos((latitude1 + latitude2)/2)*** and y is given by the formula ***y = (latitude2 - latitude1).***
     
     * It should be noted that latitude and longitude for position 1 and 2, ***(latitude1,longitude1)*** and ***(latitude2,longitude2)*** respectively, must be converted into radians in the computations of ***d***.
     * The Position Class has the latitude and longitude attributes that converted from an input ***(latitude, N/S, longitude, W/E)*** such as ***(42.917, N, 85.5872, E)*** to ***(42.917, S, 85.5872 W)***.
     * Namely, the valid value for latitude is [-90, 90] where the negative represents a position south of the equator and the positive a position north of the equator.
     * The range for longitude is [-180, 180] where the negative represents a position west of the meridian line while the positive a position east of the meridian line.
     * Lastly, the Unit Class has the radius attribute for the Earth in miles, whose value is 3950 miles.

2. Next, the Position Class is changed with the new one from position.py file in Package2 to test the information hiding of the calculation. 
     * Here, the distance computed between two coordinates is in statute miles and through spherical coordinates. The haversine calculation is based on the theta and phi, which are: ***d = R * c***, where R is Earth's radius, c is given by the formula ![render](https://user-images.githubusercontent.com/105037989/167992414-f6420c7c-9734-478d-bd82-fdafd96d7f34.png), and a is given by the formula ![render (1)](https://user-images.githubusercontent.com/105037989/167992897-75796e5b-2be4-4b57-be93-a408f9ffeeba.png). 
     * The latitudes and longitudes must be converted to radians as well. In fact, latitude converted to radians is the angle phi and longitude converted to radians is the angle theta.

3. Lastly, Package3 has a kilometer.py file which expands into the third context by computing the distance between two coordinates in kilometers and in spherical geometry. This should be done without modifying the current implementation, which increases the reusability. Here, the Earth's radius is considered to be 6359 kilometers. 

   
