from flask import Flask
from flask import request
from nic_parser.parser import Parser


app = Flask(__name__)

@app.route("/")
def hello_world():
        name =f"{request.args['name','nic']}"
        print(f"Name is {name}")

        nic = Parser(name[1])
        print(f"{nic.birth_date}")
        print(f"{nic.gender}")
        print(f"NIC is {nic}")
        return f"Hello {name} <break> "

if __name__ == '__main__':
    app.run(port=3232)
    print("Hello World")
