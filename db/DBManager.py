import mysql.connector
from mysql.connector import errorcode


def protectName(name):
    return name.replace("'", "''")


def changeAttribute(attribute, name="z"):
    if (attribute == 'Index'):
        return name + 'Index'
    if (attribute == 'Drop'):
        return 'Drops'
    if (attribute == 'Option'):
        return 'Options'
    else:
        return attribute


# @connector : Link with the mysql database
# @mydoc : the xml data
# @listTableName : list of table name in order
# @listSectionName : list of section name in order
def feedItemListToDB(connector, mydoc, listTableName, listSectionName):
    deepLevel = len(listTableName)
    if (isinstance(listTableName, str)):
        showChildAttribute(connector, mydoc, listTableName, listSectionName)

    elif (deepLevel == 2):
        showParentAttribute(connector, mydoc, listTableName, listSectionName)

    else:
        itemLoop(connector, mydoc, listTableName, listSectionName,
                 listNameStr, listValueStr, listParentValue, idList, deepLevel)


def showParentAttribute(connector, mydoc, tabName, sectionName):
    nameStr = ""
    valueStr = ""
    for items in mydoc.getElementsByTagName(sectionName[0]):
        parentName = sectionName[0] + items.attributes.items()[0][0] + ","
        parentValue = "'" + items.attributes.items()[0][1] + "',"
        for attributes in items.attributes.items():
            if (nameStr == ""):
                nameStr += changeAttribute(
                    attributes[0], sectionName[0])
                valueStr += "'" + protectName(attributes[1]) + "'"
            else:
                nameStr += "," + \
                    changeAttribute(attributes[0], sectionName[0])
                valueStr += ",'" + protectName(attributes[1]) + "'"
        sqlString = "INSERT INTO " + tabName[0] + \
            "(" + nameStr + ") VALUES (" + valueStr + ")"
        print(sqlString)
        connector.cursor().execute(sqlString)
        connector.commit()
        nameStr = ""
        valueStr = ""
        showChildAttribute(connector, items,
                           tabName[1], sectionName[1], parentName, parentValue)


def showChildAttribute(connector, mydoc, tabName, sectionName, parentName="", parentValue=""):
    nameStr = ""
    valueStr = ""
    for items in mydoc.getElementsByTagName(sectionName):
        for attributes in items.attributes.items():
            if (nameStr == ""):
                nameStr += changeAttribute(
                    attributes[0], sectionName)
                valueStr += "'" + protectName(attributes[1]) + "'"
            else:
                nameStr += "," + \
                    changeAttribute(attributes[0], sectionName)
                valueStr += ",'" + protectName(attributes[1]) + "'"
        sqlString = "INSERT INTO " + tabName + \
            "(" + parentName + nameStr + \
            ") VALUES (" + parentValue + valueStr + ")"
        # print(sqlString)
        connector.cursor().execute(sqlString)
        connector.commit()
        nameStr = ""
        valueStr = ""


# IS IN DEVELOPMENT
# @connector {object} : Link with the mysql database
# @mydoc {object(DOM)} : the xml data
# @listTableName {tuple of str} : list of table name in order
# @listSectionName {tuple of str} : list of section name in order
# @listNameStr {list of str} : list of the name of the xml section
# @listValueStr {list of str} : list of the value of the xml section
# @listParentValue (list of str) : list of the parents to use as primary keys
# @idList {int} : ID of the list currently in use
# @deepLevel {int} : maximum of foreach
def itemLoop(connector, mydoc, listTableName, listSectionName, listNameStr, listValueStr, listParentValue, idList, deepLevel):
    parentname = ""
    parentvalue = ""
    for items in mydoc.getElementsByTagName(listSectionName[idList]):
        if (idList != deepLevel):
            listParentValue[idList] = items.attributes.items()[0][1]
        for attributes in items.attributes.items():
            if (listNameStr[idList] == ""):
                listNameStr += changeAttribute(
                    attributes[0], listSectionName[idList])
                listValueStr += "'" + attributes[1] + "'"
            else:
                listNameStr += "," + \
                    changeAttribute(attributes[0], listSectionName[idList])
                listValueStr += ",'" + attributes[1] + "'"
        # Récupère la value du dernier item en tant que parentValue

        # Ecriture dans la BDD
        # S'il possède des parents, ajouter leur clés
        if (idList > 1):
            for i in range(deepLevel - idList):
                parentName += listSectionName[i] + 'Index'
                parentValue += listParentValue[i]

            sqlString = "INSERT INTO " + listSectionName[idList-1] + listTableName[idList] + "(" + \
                listNameStr[idList] + \
                ") VALUES (" + parentValue[idList] + listValueStr[idList] + ")"
        else:
            sqlString = "INSERT INTO " + listTableName[idList] + "(" + \
                listNameStr[idList] + \
                ") VALUES (" + listValueStr[idList] + ")"
        try:
            connector.cursor().execute(sqlString)
            connector.commit()
        except mysql.connector.Error as err:
            connector.cursor().statement
        listNameStr[idList] = ""
        listValueStr[idList] = ""
        if (idList == deepLevel - 1):
            idList = 0
        else:
            idList += 1

        itemLoop(connector, items, listTableName, listSectionName,
                 listNameStr, listValueStr, listParentValue, idList, deepLevel)
