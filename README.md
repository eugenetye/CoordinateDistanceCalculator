# Coordinate Distance Calculator

This is a Python program that computes the distance between two real world objects in different measure of distance. 

## Project Specification

The distance between two coordinates will be computed based on longitude and latitudes angles in three geometric and unit of distance contexts.
These three versions will be given in three different packages: Package1, Package2, and Package3.

1. In the first version, Package1, two files exist: Application.py and position.py. The Application.py file contains a method to call another method in Position oject to compute distance between coordinates in the three contexts. The position.py file gives the classes necessary to compute coordinate distance in the first context as follows:

    * Given two coordinates, given by latitude and longitude, and the radius of the Earth, determine distance between the coordinates in statute miles and planar geometry (equirectangular flat-Earth approximation). The formula to compute this distance is shown here:
    
       ![Tex2Img_1652328689](https://user-images.githubusercontent.com/105037989/167990578-1c6deb71-09d2-4933-a85d-e7e9676c142e.jpeg) where R is the radius of the Earth, x is the term given by the formula *x = (logitude2 - logitude1) * cos((latitude1 + latitude2)/2)

   
