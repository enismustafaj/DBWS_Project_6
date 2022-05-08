import mysql.connector
import json
import random

#Insert Query Definitions

SQL_INSERT_PERSON = "INSERT IGNORE INTO Person (email, Username) VALUES(%s, %s);"

SQL_INSERT_ITEM = "INSERT IGNORE INTO Item (ITEM_ID, Category, Color, Size)  VALUES(%s, %s, %s, %s);"

SQL_INSERT_REPORT = "INSERT INTO Report (Status, Person_email, Person_Has_ID)  VALUES(%s, %s, %s);"

SQL_INSERT_MODERATOR = "INSERT INTO Moderator(Person_Email, Username) values(%s, %s);"

SQL_INSERT_MODERATED = "INSERT INTO Moderator_moderates_lost_and_found (Moderator_Person_email, Lost_and_Found_Specific_ITEM_ID, Reason) values(%s, %s, %s);"

SQL_INSERT_LOST = "INSERT INTO Lost (Lost_Item_ID, Lost_Date, Last_Seen) VALUES(%s, %s, %s)" 

SQL_INSERT_FOUND = "INSERT INTO Found (Found_Item_ID, Found_Date, Found_Location, Image) VALUES(%s, %s, %s, %s)" 

SQL_INSERT_CAMPUS_CARD = "INSERT INTO Campus_Card(Matr_Number, Name, CampusCard_Item_ITEM_ID) values(%s, %s, %s);"

SQL_INSERT_KEYS = "INSERT INTO `Keys` (Room_Number, College, Attached_Item_Description, Keys_Item_ITEM_ID) values(%s, %s, %s, %s);"

SQL_INSERT_EARPHONE = "INSERT INTO Earphone (Brand, Earphones_Item_ITEM_ID) values(%s, %s);"

SQL_INSERT_CLOTHES = "INSERT INTO clothes (Clothes_ITEM_ID, Color)values(%s, %s);"

SQL_INSERT_PANT = "INSERT INTO pant (Pant_Type, Clothes_Pant_ITEM_ID) values(%s, %s);"

SQL_INSERT_SHIRT = "INSERT INTO shirt (Shirt_Type, Clothes_Shirt_Item_ID) values(%s, %s);"

SQL_INSERT_CLAIM = "INSERT INTO Claim (Person_email, Claim_Item_ID, Claim_Date) VALUES(%s, %s, %s)"

#Select Qury Definitions

SQL_SELECT_A = "select * from lost_and_found  join item on lost_and_found.Specific_ITEM_ID = item.ITEM_ID and claimed = 1;"

SQL_SELECT_B = "select * from lost_and_found  join item on lost_and_found.Specific_ITEM_ID = item.ITEM_ID and claimed = 0;"

SQL_SELECT_C = "select `Given Name`, Surname, `Status`, email, `Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email;"

SQL_SELECT_D = "select * from item join (select `Given Name`, Surname, `Status`, email,\
`Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email)\
 as tab on tab.Person_Has_ID = item.ITEM_ID;"

SQL_SELECT_E = "select * from item join (select `Given Name`, Surname, `Status`, email, \
`Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email)\
 as tab on tab.Person_Has_ID = item.ITEM_ID and tab.status = 'lost';"

SQL_SELECT_F = "select * from item join (select `Given Name`, Surname, `Status`, email, \
`Person_HAS_ID` from person join Person_has_Item on Person_has_Item.Person_email = person.email)\
 as tab on tab.Person_Has_ID = item.ITEM_ID and tab.status = 'found';"

SQL_SELECT_G = "select count(*) from lost_and_found where DATE_SUB(now(), INTERVAL 60 DAY) > `Lost_Date`;"

SQL_SELECT_H = "select * from person join Moderator_Moderates_Lost_and_Found on \
 Moderator_Moderates_Lost_and_Found.Moderator_Person_email = person.email;"

SQL_SELECT_I = "select * from lost_and_found join (select * from person \
join Moderator_Moderates_Lost_and_Found on Moderator_Moderates_Lost_and_Found.Moderator_Person_email = person.email) \
as tab on tab.Lost_and_Found_Specific_ITEM_ID = lost_and_found.Specific_ITEM_ID;"

SQL_UPDATE = "update lost_and_found set claimed = 1 where Specific_ITEM_ID = 1;"




def select_database(data = None):
    if data != None:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database = str(data)
            )
        return mydb
    else:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root"
            )
        return mydb

#Defining 'Null' value references for the base tables for later use
def initialize_null_values(Database):
    cursor = Database.cursor()
    cursor.execute("INSERT IGNORE INTO person VALUES(%s, %s, %s);", ('none', 'none', 'none'))
    cursor.execute("INSERT IGNORE INTO item VALUES(%s, %s, %s, %s);", ('0', 'none', 'none', 'none'))
    cursor.execute("INSERT IGNORE INTO person_has_item VALUES(%s, %s, %s);", ('none', 'none', '0'))
    Database.commit()


def commit_to_database(data, Database):
    for x in data:
        cursor = Database.cursor()
        #Extracting from dictionary
        Username = "".join(x["Username"])
        Status = "".join(x["Status"])
        Category = "".join(x["Category"])
        Color = "".join(x["Color"])
        Size = "".join(x["Size"])
        Date = "".join(x["Date"])
        Location = "".join(x["Location"])
        Desc1 = "".join(x["Desc1"])
        Desc2 = "".join(x["Desc2"])

        #Data Generation From Extraction
        Email = "".join(x["Username"]) + "@jacobs-university.de"
        print(Email)
        ITEM_ID = str(random.randint(0, 99999) % 500)
        Person = (Email, Username)
        Item = (ITEM_ID, Category, Color, Size)
        Has_Item = (Status, Email, ITEM_ID,)

        if Category.lower() == "campus_card":
            #Insersion with predefined query
            cursor.execute(SQL_INSERT_PERSON, Person )
            cursor.execute(SQL_INSERT_ITEM, Item)
            cursor.execute(SQL_INSERT_HAS_ITEM, Has_Item)
            #Case specific insersion
            Campus_Card = (Desc1, Desc2, ITEM_ID)
            cursor.execute(SQL_INSERT_CAMPUS_CARD, Campus_Card)
            #Case Loast and found
            if Status.lower() == "lost":
                Lost_And_Found = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
            elif Status.lower() == "found":
                Lost_And_Found = (ITEM_ID, 'null', 'null','0', Date, Location, 'null', 'none', Email)
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
        
        elif Category.lower() == "keys":
            #Insersion with predefined query
            cursor.execute(SQL_INSERT_PERSON, Person )
            cursor.execute(SQL_INSERT_ITEM, Item)
            cursor.execute(SQL_INSERT_HAS_ITEM, Has_Item)
            #Case specific insersion
            Keys = (Desc1, Desc2, 'null', ITEM_ID)
            cursor.execute(SQL_INSERT_KEYS, Keys)
            #Case Loast and found
            if Status.lower() == "lost":
                Lost_And_Found = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
            elif Status.lower() == "found":
                Lost_And_Found = (ITEM_ID, '0000-00-00', 'null','0', Date, Location, 'null', 'none', Email)
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)

        elif Category.lower() == "earphones":
            #Insersion with predefined query
            cursor.execute(SQL_INSERT_PERSON, Person )
            cursor.execute(SQL_INSERT_ITEM, Item)
            cursor.execute(SQL_INSERT_HAS_ITEM, Has_Item)
            #Case specific insersion
            Earphone = (Desc1, ITEM_ID)
            cursor.execute(SQL_INSERT_EARPHONE, Earphone)
            #Case Loast and found
            if Status.lower() == "lost":
                Lost_And_Found = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
            elif Status.lower() == "found":
                Lost_And_Found = (ITEM_ID, '0000-00-00', 'null','0', Date, Location, 'null', 'none', Email)
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)

        elif Category.lower() == "shirt":
            #Insersion with predefined query
            cursor.execute(SQL_INSERT_PERSON, Person )
            cursor.execute(SQL_INSERT_ITEM, Item)
            cursor.execute(SQL_INSERT_HAS_ITEM, Has_Item)
            #Case specific insersion
            Cloth = (ITEM_ID, Color)
            Shirt = (Desc1, ITEM_ID)
            cursor.execute(SQL_INSERT_CLOTHES, Cloth)
            cursor.execute(SQL_INSERT_SHIRT, Shirt)
            #Case Loast and found
            if Status.lower() == "lost":
                Lost_And_Found = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
            elif Status.lower() == "found":
                Lost_And_Found = (ITEM_ID, '0000-00-00', 'null','0', Date, Location, 'null', 'none', Email)
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)

        elif Category.lower() == "pant":
            #Insersion with predefined query
            cursor.execute(SQL_INSERT_PERSON, Person )
            cursor.execute(SQL_INSERT_ITEM, Item)
            cursor.execute(SQL_INSERT_HAS_ITEM, Has_Item)
            #Case specific insersion
            Cloth = (ITEM_ID, Color)
            Pant = (Desc1, ITEM_ID)
            cursor.execute(SQL_INSERT_CLOTHES, Cloth)
            cursor.execute(SQL_INSERT_PANT, Pant)
            #Case Loast and found
            if Status.lower() == "lost":
                Lost_And_Found = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)
            elif Status.lower() == "found":
                Lost_And_Found = (ITEM_ID, '0000-00-00', 'null','0', Date, Location, 'null', 'none', Email)
                cursor.execute(SQL_INSERT_LOST_AND_FOUND, Lost_And_Found)

    Database.commit()


def random_item_id():
    return str(random.randint(0, 99999) % 500)

def website_input_user(cursor, x):
    Username = "".join(x["Username"])
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    data = (Email, Username)

    cursor.execute(SQL_INSERT_PERSON, data)

def website_input_item(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Category = "".join(x["Category"])
    Color = "".join(x["Color"])
    Size = "".join(x["Size"])
    data = (ITEM_ID, Category, Color, Size)
    cursor.execute(SQL_INSERT_ITEM, data)

def website_input_person_has_item(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Status = "".join(x["Status"])
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    data = (Status, Email, ITEM_ID)
    cursor.execute(SQL_INSERT_REPORT, data)

def website_input_lost_item(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Date = "".join(x["Date"])
    Location = "".join(x["Location"])
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    data = (ITEM_ID, Date, Location, '1', '0000-00-00', 'null', 'null', Email, 'none')
    cursor.execute(SQL_INSERT_LOST_AND_FOUND, data)

def website_input_lost(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Date = "".join(x["Date"])
    Location = "".join(x["Location"])
    data = (ITEM_ID, Date, Location,)
    cursor.execute(SQL_INSERT_LOST, data)

def website_input_found(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Date = "".join(x["Date"])
    Location = "".join(x["Location"])
    Image = "".join(x["Image"])
    data = (ITEM_ID, Date, Location,Image)
    cursor.execute(SQL_INSERT_FOUND, data)


def website_input_found_item(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Date = "".join(x["Date"])
    Location = "".join(x["Location"])
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    data = (ITEM_ID, '0000-00-00', 'null','0', Date, Location, 'null', 'none', Email)
    cursor.execute(SQL_INSERT_LOST_AND_FOUND, data)

def website_input_moderator(cursor, x):
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    Username = "".join(x["Username"])
    data = (Email, Username)
    cursor.execute(SQL_INSERT_MODERATOR, data)

def website_input_moderates(cursor, x):
    ITEM_ID = "".join(x["ITEM_ID"])
    Email = "".join(x["Username"]) + "@jacobs-university.de"
    Reason = "".join(x["Reason"])
    data = (Email, ITEM_ID, Reason)
    cursor.execute(SQL_INSERT_MODERATED, data)
