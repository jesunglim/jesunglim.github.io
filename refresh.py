import os
import json
import editer


# make html
html_start = "<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset=\"utf-8\">\n        <title>임재성 기술 블로그</title>\n<link rel=\"stylesheet\" href=\"theme_index.css\">\n    </head>\n	<body>"
html_start_page = "<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset=\"utf-8\">\n        <title>임재성 기술 블로그</title>\n<link rel=\"stylesheet\" href=\"../theme_page.css\">\n    </head>\n	<body>"
html_end = "\n		</span>\n</div>\n\n    </body>\n</html>"
html_header = "\n        <div class=\"outer\">\n            <div class=\"head\">\n                <h1>임재성 기술 블로그</h1>\n                <img src=\"images/bio-photo.jpg\" alt=\"\">\n                <p>email : jesunglimkorea@gmail.com</p>\n                <A href=\"https://github.com/jesunglim\"> GitHub</A>\n                <p>호서대학교 학부생입니다.</p>\n                <hr style=\"height:3px;border:none;color:#333;background-color:#333;\">\n                <br><br><br><br>\n            </div>\n</div>\n<div class=\"inner\">\n	<span class=\"absolute\">"
html_header_post_view = "\n        <div class=\"outer\">\n            <div class=\"head\">\n                <h1>임재성 기술 블로그</h1>\n                <img src=\"../images/bio-photo.jpg\" alt=\"\">\n                <p>email : jesunglimkorea@gmail.com</p>\n                <A href=\"https://github.com/jesunglim\"> GitHub</A>\n                <p>호서대학교 학부생입니다.</p>\n                <hr style=\"height:3px;border:none;color:#333;background-color:#333;\">\n                <br><br><br><br>\n            </div>\n</div>\n<div class=\"inner\">\n	"



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
        html_list += "\n<a href= \"post_view/" + link + ".html\" style=\"text-decoration:none\">" + "<p>"+ date + " / " + category + "</p> <h1>" + title + "</h1> <p>" + text_prev + "</p> </a><br>"

        html_post = "\n<div class=\"title\">\n    <h1>" + title + "</h1> <p>" + date + " / category : " + category + "</p>" + "\n</div>\n" +"<hr><br><br> <p>" + text + "</p>" + "\n<span class=\"absolute\">" 
        html_path = "post_view/" + link + ".html"
        f = open(html_path,"wt")
        f.writelines(html_start_page + html_header_post_view + html_post + html_end)
        f.close()



f = open("index.html","wt")
f.writelines(html_start + html_header + html_list + html_end)
f.close()
