import json
import yaml

yaml_file = open("Coding Basics/Parsing/myfile.yaml","r")
pythondata = yaml.safe_load(yaml_file)

# Parsear el archivo
print(pythondata['expires_in'])
print("The access token from YAML is: %s" % pythondata['access_token'])

# Serializar el archivo a JSON
print("\n\n")
print(json.dumps(pythondata))