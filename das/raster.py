import os
import cv2
from shapely.geometry import Polygon
import numpy as np
import geopandas as gpd
import json

os.chdir('/Users/archisketch/Desktop/opt/') #폴더 경로
img = cv2.imread('d.png') #파일명

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #흑백사진으로 변환
ret, binary = cv2.threshold(gray, 240, 255, 0) 

contours, hierachy = cv2.findContours(binary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 3)

poly_objs = []
for i in range(len(contours)):
    if (i > 0) and (len(contours[i]))>2:
        poly_objs.append(Polygon(np.squeeze(contours[i]))) #poly_objs라는 list에 contours의 점들을 꼭지점으로 가지는 폴리곤을 만들어 넣어

polygons = poly_objs
polygons = gpd.GeoDataFrame(polygons, columns = ['geometry'])
polygons.to_file('ㅇ.json')
