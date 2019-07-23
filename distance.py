#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:33:00 2019

@author: sonalsannigrahi
"""
import math
import numpy as np


#Haversine Distance calculator

def haversine(lat1, lon1, lat2, lon2): 
      
    # distance between lat and long converted into radians
    d_lat = (lat2 - lat1) * math.pi / 180.0
    d_lon = (lon2 - lon1) * math.pi / 180.0
  
    # degrees into radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
  
    # apply haversine formula 
    h = ((math.sin(d_Lat / 2)**2 + (math.sin(d_Lon / 2))**2 *math.cos(lat1) * math.cos(lat2)))
    R = 6371 #radius of the Earth in km
    d = 2 * R * math.asin(math.sqrt(h)) 
    return  d 

#Euclidean Distance calculator 

def euclidean(lat1, lon1, lat2, lon2):
    R = 6367 #radius of earth in km
    #Convert degrees into radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0
    lon1 = (lon1) * math.pi / 180.0
    lon2 = (lon2) * math.pi / 180.0
    #convert to 3-D point in space
    point_1 = np.array((R* math.cos(lat1)* math.cos(lon1), R*math.cos(lat1)*math.sin(lon1), R*math.sin(lat1)))
    point_2 = np.array((R* math.cos(lat2)* math.cos(lon2), R*math.cos(lat2)*math.sin(lon2), R*math.sin(lat2)))
    #find norm
    return (np.linalg.norm(point_1 - point_2))