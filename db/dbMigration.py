# Drop all tables created until now

def dropAllTables(connection):
    connection.execute(
        "DROP TABLE IF EXISTS "
        "ItemListIndex,"
        "ItemList,"
        "MonsterList"
    )

# Linked to Mu/Data/Items/ItemList.xml


def createTableItemListIndex(connection):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS ItemListIndex("
        "SectionIndex SMALLINT UNSIGNED,"
        "name varchar(50),"
        "primary key (SectionIndex))"
    )

# Linked to Mu/Data/Items/ItemList.xml


def createTableItemList(connection):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS ItemList("
        "SectionIndex SMALLINT UNSIGNED,"
        "ItemIndex SMALLINT UNSIGNED,"
        "Slot TINYINT,"
        "SkillIndex SMALLINT UNSIGNED,"
        "TwoHand BOOLEAN,"
        "Width TINYINT UNSIGNED,"
        "Height TINYINT UNSIGNED,"
        "Serial BOOLEAN,"
        "Options BOOLEAN,"
        "Drops BOOLEAN,"
        "DropLevel TINYINT UNSIGNED DEFAULT NULL,"
        "DamageMin TINYINT UNSIGNED DEFAULT NULL,"
        "DamageMax TINYINT UNSIGNED DEFAULT NULL,"
        "AttackSpeed TINYINT UNSIGNED DEFAULT NULL,"
        "WalkSpeed TINYINT UNSIGNED DEFAULT NULL,"
        "Defense TINYINT UNSIGNED DEFAULT NULL,"
        "MagicDefense TINYINT UNSIGNED DEFAULT NULL,"
        "SuccessfulBlocking TINYINT UNSIGNED DEFAULT NULL,"
        "Durability TINYINT UNSIGNED DEFAULT NULL,"
        "MagicDurability TINYINT UNSIGNED DEFAULT NULL,"
        "IceRes TINYINT UNSIGNED DEFAULT NULL,"
        "PoisonRes TINYINT UNSIGNED DEFAULT NULL,"
        "LightRes TINYINT UNSIGNED DEFAULT NULL,"
        "FireRes TINYINT UNSIGNED DEFAULT NULL,"
        "EarthRes TINYINT UNSIGNED DEFAULT NULL,"
        "WindRes TINYINT UNSIGNED DEFAULT NULL,"
        "WaterRes TINYINT UNSIGNED DEFAULT NULL,"
        "MagicPower INT DEFAULT NULL,"
        "ReqLevel SMALLINT UNSIGNED DEFAULT NULL,"
        "ReqStrength SMALLINT UNSIGNED DEFAULT NULL,"
        "ReqDexterity SMALLINT UNSIGNED DEFAULT NULL,"
        "ReqEnergy SMALLINT UNSIGNED DEFAULT NULL,"
        "ReqVitality SMALLINT UNSIGNED DEFAULT NULL,"
        "ReqCommand SMALLINT UNSIGNED DEFAULT NULL,"
        "Money INT DEFAULT NULL,"
        "SetAttrib TINYINT UNSIGNED DEFAULT NULL,"
        "DarkWizard TINYINT UNSIGNED DEFAULT NULL,"
        "DarkKnight TINYINT UNSIGNED DEFAULT NULL,"
        "FairyElf TINYINT UNSIGNED DEFAULT NULL,"
        "MagicGladiator TINYINT UNSIGNED DEFAULT NULL,"
        "DarkLord TINYINT UNSIGNED DEFAULT NULL,"
        "Summoner TINYINT UNSIGNED DEFAULT NULL,"
        "RageFighter TINYINT UNSIGNED DEFAULT NULL,"
        "Dump BOOLEAN,"
        "Transaction BOOLEAN,"
        "PersonalStore BOOLEAN,"
        "StoreWarehouse BOOLEAN,"
        "SellToNPC TINYINT UNSIGNED,"
        "Repair BOOLEAN,"
        "KindA TINYINT UNSIGNED,"
        "KindB TINYINT UNSIGNED,"
        "Overlap TINYINT UNSIGNED,"
        "NAME VARCHAR(50),"
        "PRIMARY KEY (SectionIndex,ItemIndex))"
    )

# Linked to Mu/Data/Settings


def createTableMonsterList(connection):
    connection.execute(
        "CREATE TABLE IF NOT EXISTS MonsterList("
        "MonsterIndex SMALLINT UNSIGNED,"
        "ExpType BOOLEAN,"
        "Name VARCHAR(50),"
        "Level TINYINT UNSIGNED,"
        "HP INT UNSIGNED,"
        "MP TINYINT UNSIGNED,"
        "DamageMin SMALLINT UNSIGNED,"
        "DamageMax SMALLINT UNSIGNED,"
        "Defense SMALLINT UNSIGNED,"
        "MagicDefense TINYINT UNSIGNED,"
        "AttackRate SMALLINT UNSIGNED,"
        "BlockRate SMALLINT UNSIGNED,"
        "MoveRange TINYINT UNSIGNED,"
        "AttackType TINYINT UNSIGNED,"
        "AttackRange TINYINT UNSIGNED,"
        "ViewRange TINYINT UNSIGNED,"
        "MoveSpeed SMALLINT UNSIGNED,"
        "AttackSpeed SMALLINT UNSIGNED,"
        "RegenTime SMALLINT UNSIGNED,"
        "Attribute TINYINT UNSIGNED,"
        "ItemDropRate SMALLINT UNSIGNED,"
        "MoneyDropRate SMALLINT UNSIGNED,"
        "MaxItemLevel TINYINT UNSIGNED,"
        "MonsterSKill TINYINT UNSIGNED,"
        "IceRes TINYINT UNSIGNED,"
        "PoisonRes TINYINT UNSIGNED,"
        "LightRes TINYINT UNSIGNED,"
        "FireRes TINYINT UNSIGNED,"
        "PentagramMainAttrib TINYINT UNSIGNED,"
        "PentagramAttribPattern TINYINT UNSIGNED,"
        "PentagramDamageMin INT UNSIGNED,"
        "PentagramDamageMax INT UNSIGNED,"
        "PentagramAttackRate SMALLINT UNSIGNED,"
        "PentagramDefenseRate SMALLINT UNSIGNED,"
        "PentagramDefense SMALLINT UNSIGNED,"
        "PRIMARY KEY (MonsterIndex))"
    )


def createAllTable(connection):
    createTableItemListIndex(connection)
    createTableItemList(connection)
    createTableMonsterList(connection)
