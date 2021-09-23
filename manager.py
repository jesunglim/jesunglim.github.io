import os

html_start = "<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset=\"utf-8\">\n        <title>임재성 기술 블로그</title>\n    </head>\n	<body>"
html_end = "\n        </div>\n    </body>\n</html>"
html_header = "\n        <div style=\"text-align: center\">\n            <div class=\"head\">\n                <h1>임재성 기술 블로그</h1>\n                <img src=\"images/bio-photo.jpg\" alt=\"\">\n                <p>email : jesunglimkorea@gmail.com</p>\n                <A href=\"https://github.com/jesunglim\"> GitHub</A>\n                <p>호서대학교 학부생입니다.</p>\n                <hr style=\"height:3px;border:none;color:#333;background-color:#333;\">\n                <br><br><br><br>\n            </div>\n"


html_list = ""


files = os.listdir("posts")
for i in files:
    print(i)

f = open("../index.html","wt")
f.writelines(html_start + html_header + html_end)
f.close()


