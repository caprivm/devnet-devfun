import json
import yaml

with open("Coding Basics/Parsing/myfile.json", 'r') as json_file:
    ourjson = json.load(json_file)

json_file.close()
print(ourjson)
print(ourjson['expires_in'])
print("The access token from JSON is: %s" % ourjson['access_token'])

# Para convertir el archivo JSON en un YAML
print("\n\n---")
print(yaml.dump(ourjson))