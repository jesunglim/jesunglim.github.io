import os
import json
import editer

# post
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


# make html
html_start = "<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset=\"utf-8\">\n        <title>임재성 기술 블로그</title>\n    </head>\n	<body>"
html_end = "\n        </div>\n    </body>\n</html>"
html_header = "\n        <div style=\"text-align: center\">\n            <div class=\"head\">\n                <h1>임재성 기술 블로그</h1>\n                <img src=\"images/bio-photo.jpg\" alt=\"\">\n                <p>email : jesunglimkorea@gmail.com</p>\n                <A href=\"https://github.com/jesunglim\"> GitHub</A>\n                <p>호서대학교 학부생입니다.</p>\n                <hr style=\"height:3px;border:none;color:#333;background-color:#333;\">\n                <br><br><br><br>\n            </div>\n"
html_header_post_view = "\n        <div style=\"text-align: center\">\n            <div class=\"head\">\n                <h1>임재성 기술 블로그</h1>\n                <img src=\"../images/bio-photo.jpg\" alt=\"\">\n                <p>email : jesunglimkorea@gmail.com</p>\n                <A href=\"https://github.com/jesunglim\"> GitHub</A>\n                <p>호서대학교 학부생입니다.</p>\n                <hr style=\"height:3px;border:none;color:#333;background-color:#333;\">\n                <br><br><br><br>\n            </div>\n"



html_list = "           "


files = os.listdir("posts")
files.reverse()
for i in files:
    path = "posts/" + i
    with open(path) as json_file:
        json_data = json.load(json_file)
        date = json_data["date"]
        category = json_data["category"]
        title = json_data["title"]
        text = json_data["text"]
        
        text_prev = str(text.split("<img")[0])
        text_prev = text_prev[0:50]
        
        link = i.split('.')[0]
        html_list += "<a href= \"post_view/" + link + ".html\" style=\"text-decoration:none\">" + "<p>"+ date + " / " + category + "</p> <h1>" + title + "</h1> <p>" + text_prev + "</p> </a><br>"

        html_post = "           <h1>" + title + "</h1> <p>" + date + " / category : " + category + "</p><hr><br><br> <p>" + text + "</p>"  
        html_path = "post_view/" + link + ".html"
        f = open(html_path,"wt")
        f.writelines(html_start + html_header_post_view + html_post + html_end)
        f.close()



f = open("index.html","wt")
f.writelines(html_start + html_header + html_list + html_end)
f.close()
