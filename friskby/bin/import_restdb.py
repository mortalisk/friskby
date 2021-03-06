#!/usr/bin/env python
import os
import requests
import django
import sys

restdb_url = "https://friskbybergen-1d96.restdb.io/rest/posts"
restdb_key = os.getenv("RESTDB_IMPORT_KEY")
post_key   = os.getenv("RPI_IMPORT_KEY")



def update_env(*args):
    for arg in args:
        var,value = arg.split("=")
        os.environ[var] = value
    
    if not os.environ.has_key("DJANGO_SETTINGS_MODULE"):
        os.environ["DJANGO_SETTINGS_MODULE"] = "friskby.settings"

    new_path = os.path.realpath( os.path.join( os.path.dirname(__file__) , "../../") )
    sys.path.insert( 0 , new_path )


def assert_env():
    assert os.environ.has_key("DATABASE_URL")
    assert os.environ.has_key("DJANGO_SETTINGS_MODULE")

#################################################################
update_env()
assert_env()
django.setup()

from sensor.models import *


response = requests.get( restdb_url , 
                         params = {"max" : 10000000}, 
                         headers = {"x-apikey" : restdb_key , "Content-Type" : "application/json"})

print response

import_set = set(["FriskPI01" , "FriskPI02" , "FriskPI04"])
data = {}
if response.status_code == 200:
    for line in response.json( ):
        device_id = line["deviceid"]
        if device_id in import_set:
            ts = line["timestamp"]
            pm10 = line["data"]["PM10"]
            pm25 = line["data"]["PM25"]
            
            sensor_id_pm10 = "%s_PM10" % device_id
            sensor_id_pm25 = "%s_PM25" % device_id
            if not sensor_id_pm10 in data:
                data[sensor_id_pm10] = []

            if not sensor_id_pm25 in data:
                data[sensor_id_pm25] = []
            
            data[sensor_id_pm10].append( (ts , pm10 ))
            data[sensor_id_pm25].append( (ts , pm25 ))


for sensor_id in data.keys():
    print "Deleting old %s entries" % sensor_id
    RawData.objects.filter( sensor_id = sensor_id ).delete()
    print "Inserting new %s entries" % sensor_id
    cnt = 0
    for (ts,pm) in data[sensor_id]:
        post = {"key" : post_key,
                "sensorid" : sensor_id,
                "value" : pm,
                "timestamp" : ts }
        
        rd = RawData.create( post )
        if rd.status != RawData.VALID:
            raise ValueError("Invalid RawData:%s " % rd)
            
        cnt += 1 
        if cnt % 100 == 0:
            print "%s : %d/%d" % (sensor_id , cnt, len(data[sensor_id]))
