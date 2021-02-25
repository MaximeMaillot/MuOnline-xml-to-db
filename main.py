from xml.dom import minidom
import json

import mysql.connector
from mysql.connector import errorcode

from db.dbMigration import createAllTable
from itemListManager import feedItemListDB

with open('.env.json') as dcb:
    credentials = json.load(dcb)

connector = mysql.connector.connect(
    host=credentials['host'],
    user=credentials['user'],
    password=credentials['password'],
    database=credentials['database']
)

cursor = connector.cursor()

createAllTable(cursor)

mydoc = minidom.parse('Mu/Data/Items/ItemList.xml')

feedItemListDB(connector, mydoc)

# feedItemListIndexDB(connector, mydoc)
