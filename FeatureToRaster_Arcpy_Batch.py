# -*- coding: utf-8 -*-
"""
# —*— ProjectName：Batch FeatureToRaster
# —*— Author：李国龙
# —*— CreateTime：2022年12月13日16:37:44
# —*— Vision：1.0.0
# —*— Information:批量矢量转栅格
"""
import arcpy
from arcpy import env
import os

env.workspace = "E:/test/test/shp"   #工作空间：矢量文件路径
field = 'pm'    #字段
cellsize = "E:/test/test/ref/tem2015_2.tif" #像元大小：数值或文件路径

files = os.listdir(env.workspace)
for file in files:

    if file.find('.shp') >= 0:
        raster_name = file.replace('.shp', '.tif')
        arcpy.FeatureToRaster_conversion(file, field, raster_name, cellsize)
        print file,'\tconversion finish'

print 'All ShapeFile Convert To Raster Success！'