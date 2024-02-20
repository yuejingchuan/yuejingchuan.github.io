import json

from mysql_db import con, cursor
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/users", methods=['post'])
def login_data():
    username = request.json['username']
    password = request.json['password']
    login_select_str = f"select * from t_users where username = '{username}' and password = '{password}'"
    cursor.execute(login_select_str)
    result = cursor.fetchall()
    return json.dumps(result)


@app.route("/update", methods=['post'])
def dispatch_update():
    dispatch_num = request.json['dispatchNum']
    print(type(dispatch_num))
    username = request.json['username']
    dispatch_num += 1
    dispatch_update_str = f"update t_users set dispatchNum = {dispatch_num} where username = '{username}'"

    cursor.execute(dispatch_update_str)
    con.commit()
    return json.dumps({"dispatchNum": dispatch_num})


@app.route("/centerInfoSelect", methods=['post'])
def select_center_info():
    select_all_str = f"select * from centerinfo"
    cursor.execute(select_all_str)
    results = cursor.fetchall()
    return json.dumps(results)







app.run(debug=True, port=8888)
