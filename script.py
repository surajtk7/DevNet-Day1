import json
import yaml
import xmltodict

with open("sample.json",'r') as file1:
    pydata=json.load(file1)

with open("sample.yaml",'w') as file2:
    ydata=yaml.dump(pydata,file2)

with open("sample.xml",'w') as file3:
    file3.write(xmltodict.unparse(pydata))


    

     

