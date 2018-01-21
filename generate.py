#! /usr/bin/python
import json

f = open('./data/colors.json','r')
json = json.loads(f.read())
result_list = list()
result_list.append("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
result_list.append("<resources>")
for color in json:
    result_list.append("    <color name=\"copic_%s\">%s</color>" % (color["code"], color["bg"]))
result_list.append("</resources>")

out = open("./copiccolors/src/main/res/values/copic.xml", "w")
out.write("\n".join(result_list))
out.close()

