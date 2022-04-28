# tabbypdf?xml???json
import xmltodict
import json
import os


def xml_to_json(xml_path):
    # parse??xml???
    path = "./xml"
    xml_file = open(path + '/' + xml_path, 'rb')
    print(xml_file)
    xml_str = xml_file.read().decode('UTF-8')
    try:
        xml_parse = xmltodict.parse(xml_str)
    except:
        json_str = None
        return json_str
    # json?dumps()??dict???json??,loads()??json???dict???
    # dumps()???ident=1,???json
    json_str = json.dumps(xml_parse, indent=1)
    return json_str

# ????
if __name__ == "__main__":
    path = "./xml"
    fileList = os.listdir(path)
    for file in fileList:
        data = xml_to_json(file)
        if data != None:
            name = file[0:12]
            file_dir = name +".json"
            with open(file_dir, 'w', encoding='utf-8') as f:
                f.write(data)
