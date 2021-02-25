def changeAttribute(attribute):
    if (attribute == 'Index'):
        return 'Indexz'
    if (attribute == 'Drop'):
        return 'Dropz'
    if (attribute == 'Option'):
        return 'Optionz'
    else:
        return attribute


def protectName(name):
    return name.replace("'", "''")


def feedItemListDB(connector, mydoc):
    firstAttribute = True
    colname = ""
    colvalue = ""
    for sections in mydoc.getElementsByTagName('Section'):
        sqlString = "INSERT INTO ItemListIndex(SIndexz, Name) VALUES('" + \
            sections.attributes.items()[0][1] + "', '" + \
            sections.attributes.items()[1][1] + "')"
        connector.cursor().execute(sqlString)
        connector.commit()
        # Rupture section
        if (colname != ""):
            sqlString = "INSERT INTO ItemList(SIndexz," + \
                colname + ") VALUES (" + sectionId + "," + colvalue + ")"
            connector.cursor().execute(sqlString)
            connector.commit()
            colvalue = ""
            colname = ""
            sqlString = ""
            firstAttribute = True
        sectionId = sections.attributes.items()[0][1]

        for items in sections.getElementsByTagName('Item'):
            # Rupture Attribut

            if (colname != ""):
                sqlString = "INSERT INTO ItemList(SIndexz," + \
                    colname + ") VALUES (" + sectionId + "," + colvalue + ")"
                connector.cursor().execute(sqlString)
                connector.commit()
                colvalue = ""
                colname = ""
                sqlString = ""
                firstAttribute = True

            # Should be ok
            for attributes in items.attributes.items():
                if (firstAttribute):
                    colname += changeAttribute(attributes[0])
                    colvalue += "'" + protectName(attributes[1]) + "'"
                    firstAttribute = False
                else:
                    colname += ',' + changeAttribute(attributes[0])
                    colvalue += ',' + "'" + protectName(attributes[1]) + "'"

    sqlString = "INSERT INTO ItemList(SIndexz," + \
        colname + ") VALUES (" + sectionId + "," + colvalue + ")"
    connector.cursor().execute(sqlString)

    connector.commit()

    print("Done")
