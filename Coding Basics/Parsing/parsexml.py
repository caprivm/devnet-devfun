import xml.etree.ElementTree as ET
import re
import os

# Listar archivos en el directorio actual
files = os.listdir(os.curdir)

# Parsear el XML, cargarlo como estructura conocida para Python
xml = ET.parse("Coding Basics/Parsing/myfile.xml")
root = xml.getroot()

# Regular expression matches en el archivo
# Namespace del XML
ns = re.match(r'{.*}', root.tag).group(0)

# edit-config section of the XML
editconf = root.find(f"{ns}edit-config")
defop = editconf.find(f"{ns}default-operation")
testop = editconf.find(f"{ns}test-option")

print("The default-operation contains: %s" % defop.text)
print("The test-option contains: %s" % testop.text)

