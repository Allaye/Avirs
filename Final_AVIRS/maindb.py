import sys
import os
import sqlite3 as lite

con = lite.connect('Final_Avirs.db')
cur = con.cursor()


def createtb():
    queryveh = """CREATE TABLE IF NOT EXISTS VehicleTB(Scan_DI	INTEGER PRIMARY KEY NOT NULL UNIQUE,
    Vehicle_number	TEXT NOT NULL, Vehicle_type	TEXT NOT NULL, Cam_loc	TEXT NOT NULL, Date_Time	TEXT NOT NULL, 
    Vehicle_number_pic BLOB NOT NULL) """
    #  queryhit = """CREATE TABLE IF NOT EXISTS Vehicle_HitsTB" (Logid INTEGER PRIMARY KEY NOT NULL ,
    # Vehicle_number  TEXT NOT NULL, Location	TEXT NOT NULL, Date_Time TEXT NOT NULL, Vehicle_color TEXT NOT NULL)"""

    cur.execute(queryveh)
    #  cur.execute(queryhit)
    con.commit()


def vehicletbquery():
    query = "SELECT * from VehicleTB"
    vehicletb = cur.execute(query).fetchall()
    return vehicletb


def vehicle_hitstbquery():
    query = "SELECT * from  Vehicle_HitsTB"
    hitstb = cur.execute(query).fetchall()
    return hitstb


def hitquery():
    query = "SELECT Vehicle_number from Vehicle_HitsTB"
    hitstb = cur.execute(query).fetchall()
    return hitstb


def vehicledetailsquery(vn, vt, cl, dt, vnp):
    scan_id = vn + "1"
    query = " INSERT INTO 'VehicleTB' ( Vehicle_number, Vehicle_type, Cam_loc, " \
            "Date_Time, Vehicle_number_pic ) VALUES( ?, ?, ?, ?, ?)"
    cur.execute(query, (vn, vt, cl, dt, vnp))
    con.commit()
