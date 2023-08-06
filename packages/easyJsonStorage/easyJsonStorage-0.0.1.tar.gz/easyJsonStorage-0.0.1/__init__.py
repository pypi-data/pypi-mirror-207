# create
def createJson(file_name,_keys):
    import io
    import json
    f = open(file_name+".json", "w")
    f.close()
    # Define data
    data={}
    for _key in _keys:
        data[_key]=[]

    # Write JSON file
    with io.open(file_name+'.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
        print(str_)
        outfile.write(str_)

#get
def getJsonKey(file_name,key):
  
    import json

    file_name = file_name+'.json'

    with open(file_name, 'r', encoding='utf-8') as f:
        my_data = json.load(f)

        return my_data[key]  #{'name': 'Alice', 'age': 30}



def addJson(filename,key,new_data_dict):
    import json
    filename=filename+'.json'
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[key].append(new_data_dict)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)




# Search
# if found return, index number
# if not found, return False
def searchValue(file_name,key,val):
    import json
    import re
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
    arr_of_dict = data[key] 
    cnt=0
    for dict_item in arr_of_dict:
        for item in dict_item:
            result = re.search(str(val).lower(), str(dict_item[item]).lower())
            if(result):
                return cnt
        cnt=cnt+1
    return 'False'

# return muliple index in array
def searchValues(file_name,key,val):
    import json
    import re
    index=[]
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
    arr_of_dict = data[key] 
    cnt=0
    for dict_item in arr_of_dict:
        for item in dict_item:
            result = re.search(str(val).lower(), str(dict_item[item]).lower())
            if(result):
                index.append(cnt)
        cnt=cnt+1
    if(len(index)):
        return index
    else:
        return 'False'
    

def getSingleDict(file_name,key,index):
    import json
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
    arr_of_dict = data[key][index]
    arr_of_dict['index']=index
    return arr_of_dict

def getMultipleDict(file_name,key,indexs):
    import json
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
    multiple_dict=[]
    for index in indexs:
        arr_of_dict = data[key][index]
        arr_of_dict['index']=index
        multiple_dict.append(arr_of_dict)
    return multiple_dict


# update a specific dictionary of json data
def updateJsonDict(file_name,key,index,new_dict_data):  
    import json
    import io
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
        #updating
        data[key][index]=new_dict_data
        print(data)
        # Saving data in file
        with io.open(file_name+'.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,indent=4,separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
        jsonFile.close()


# update a specific value of json data
def updateJsonValue(file_name,key,index,dict_key,new_value):  
    import json
    import io
    with open(file_name+".json", "r+") as jsonFile:
        data = json.load(jsonFile)
        #updating
        data[key][index][dict_key]=new_value
        # Saving data in file
        with io.open(file_name+'.json', 'w', encoding='utf8') as outfile:
            str_ = json.dumps(data,indent=4,separators=(',', ': '), ensure_ascii=False)
            outfile.write(str_)
        jsonFile.close()