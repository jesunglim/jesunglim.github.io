import os
import json
import editer


data = {
    "date" :  str(editer.date),
    "category" : str(editer.category),
    "title" : str(editer.title),
    "text" : str(editer.text),
}

file_num = len(os.listdir("posts"))
file_num = str(file_num + 1)
path = "posts/" + file_num + ".json"
with open(path, "w") as json_file:
    json.dump(data, json_file, ensure_ascii=False)

