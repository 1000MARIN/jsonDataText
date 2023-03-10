import json
import os

dir = './json'
jsonFileList = os.listdir(dir)
print(jsonFileList)

for filePath in jsonFileList:
    print(filePath)
    
    with open(dir +"\\" +filePath, 'r', encoding='utf8') as f:
        contents = f.read() 
        json_data = json.loads(contents)

    f = open(filePath+'.txt','w')
    for i in json_data["annotations"]:
        id = i["id"]
        textId = str(id)
        print("id = " + textId)
        print("\n")
        f.write("id = " + textId + "\n")
        f.write("\n")
        data = str(i["segmentation"])
        newData = data.replace('[[', '').replace(']]', '').replace(',', '')
        listData = list(newData.split())
        jData = listData[0::2]
        hData = listData[1::2]
        
        for j, h in zip(jData,hData):
            print(j + ", " + h)
            f.write(j + ", " + h + "\n")
        print("==========================")
        f.write("\n")
        f.write("==========================" + "\n")
        f.write("\n")

    f.close()