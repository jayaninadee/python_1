from flask import Flask
from flask import request
from nic_parser.parser import Parser
from string import Template
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def hello_world():
    index_file=open("templates/index.html","r")
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
