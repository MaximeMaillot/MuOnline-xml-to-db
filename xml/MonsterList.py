try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")
import json

import mysql.connector
from mysql.connector import errorcode

with open('.env.json') as dcb:
    credentials = json.load(dcb)

connector = mysql.connector.connect(
    host=credentials['host'],
    user=credentials['user'],
    password=credentials['password'],
    database=credentials['database']
)


def dbToXMLOneNode(connector, tableName, sectionName, fileName):
    sqlString = "select * from " + tableName
    cursor = connector.cursor()
    cursor.execute(sqlString)

    data = cursor.fetchall()

    num_fields = len(cursor.description)
    field_names = [i[0] for i in cursor.description]

    root = etree.Element(tableName)

    test = {}

    for item in data:
        for i in range(num_fields):
            test[field_names[i]] = str(item[i])
        etree.SubElement(root, sectionName, test)

    tree = etree.ElementTree(root)
    tree.write(fileName + ".xml")


dbToXMLOneNode(connector, "ItemList", "Item", "ItemList")
