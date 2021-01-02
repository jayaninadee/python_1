from flask import Flask
from flask import request
from nic_parser.parser import Parser
from string import Template
from flask import render_template

app = Flask(__name__)

name_list = ["A", "B"]


@app.route("/insert_user", methods=["get", "post"])
def insert_user_data():
    print("insert_user_data_method")
    name = ""
    print(request.method)
    if request.method == "POST":
        print("inside the post filter")
        name = request.form.get("user_name")
        name_list.append(name)

    return render_template("user_data.html", name_list=name_list)




@app.route("/_index_file_from_file_read")
def using_file_read():
    index_file = open("templates/index.html", "r")
    index_string = index_file.readlines()
    temp_string = Template(''.join(index_string))
    index_string = temp_string.substitute(name="ABCCC")
    return f"{index_string}"

#
# @app.route("/insert_user",methods=["get","post"])
# def insert_user_data():
#     name=" "
#     print("insert_user_data_method")
#     print(request.method)
#     if request.method == "POST":
#         print("inside the post filter")
#     # if "user_name" in request.args:
#     #     print(request.args["user_name"])
#         name = request.form.get("user_name")
#     return render_template("user_data.html", name=name)

@app.route("/")
def index():
    return render_template("index.html", name="Jadu")

@app.route("/")
def hello_world():
    index_file=open("templates/index.html", "r")
    index_string=index_file.readline()
    temp_string=Template(''.join(index_string))
    index_string = temp_string.substiute(name="JayaniNa")

    return f"{index_string}"



    # print(f"{request.args}")
    # name = f"{request.args['name']}"
    # nic = f"{request.args['nic']}"
    #
    # print(f"Name is {name}")
    # print(f"Nic is {nic}")
    #
    # dob = Parser(f"{nic}").birth_date
    # gender = Parser(f"{nic}").gender
    # print(dob)
    # print(gender)
    #
    # return f"Dob : {dob} , Gender : {gender.name}"
    #

if __name__ == '__main__':
    app.run(port=3232)
