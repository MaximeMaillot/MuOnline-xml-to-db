from xml.dom import minidom
import json

import mysql.connector
from mysql.connector import errorcode

from db.dbMigration import dropAllTables, createAllTable
from db.DBManager import feedItemListToDB

with open('.env.json') as dcb:
    credentials = json.load(dcb)

connector = mysql.connector.connect(
    host=credentials['host'],
    user=credentials['user'],
    password=credentials['password'],
    database=credentials['database']
)

cursor = connector.cursor()

dropAllTables(cursor)

createAllTable(cursor)

mydoc = minidom.parse('MuTest/Data/Monster/Settings/MonsterList.xml')
feedItemListToDB(connector, mydoc, ("MonsterList"), ("Monster"))

mydoc = minidom.parse('MuTest/Data/Items/ItemList.xml')
feedItemListToDB(connector, mydoc, ("ItemIndexList",
                                    "ItemList"), ("Section", "Item"))
