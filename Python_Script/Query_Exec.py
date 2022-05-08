from Query_Definitions import *

input = open("Data.txt", "r")
data = []

for x in input:
    string = x.split("\n")
    string = string[0].split(" ")
    print(string)
    dict = {"Name": [], "Surname": [], "Status": [], "Category" :[], "Color": [], "Size" : [], "Date": [], "Location": [], "Desc1": [], "Desc2":[]}
    dict["Name"].append(string[0])
    dict["Surname"].append(string[1])
    dict["Status"].append(string[2])
    dict["Category"].append(string[3])
    dict["Color"].append(string[4])
    dict["Size"].append(string[5])
    dict["Date"].append(string[6])
    dict["Location"].append(string[7])
    dict["Desc1"].append(string[8])
    if len(string) > 9:
        dict["Desc2"].append(string[9])
    
    data.append(dict)

DB = select_database("itemdatabase")
cursor = DB.cursor()
initialize_null_values(DB) #Defining a "Null" Reference for foreign keys
commit_to_database(data, DB)


#get the scripts fromt he queries file and store them in a list
# sqlFile = open('../SQL_Scripts/queries.sql', 'r')
# content = sqlFile.read().split('\n')
# sqlFile.close()
# queries = []
# for i in content:
#     if i == '':
#         continue
#     if(i[0] == 's'):
#         queries.append(i)
        

#print(queries)

# cursor.execute()
# a = cursor.fetchall()
# print(a[0])