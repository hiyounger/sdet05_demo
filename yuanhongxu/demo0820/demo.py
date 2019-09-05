from flask import Flask, jsonify,request

app = Flask(__name__)

resp_today = {"code": 200, "data": {"customerNum": 1234567, "contactsNum": 342, "businessNum": 457, "contractNum": 546,"recordNum": 234, "receivablesNum": 55, "businessStatusNum": 88}, "error": ""}
resp_yesterday = {"code": 200, "data": {"customerNum": 12567, "contactsNum": 32, "businessNum": 457, "contractNum": 546,"recordNum": 234, "receivablesNum": 55, "businessStatusNum": 88}, "error": ""}
resp_month = {"code": 200, "data": {"customerNum": 123567, "contactsNum": 42, "businessNum": 457, "contractNum": 546,"recordNum": 234, "receivablesNum": 55, "businessStatusNum": 88}, "error": ""}
resp_week = {"code": 200, "data": {"customerNum": 823567, "contactsNum": 382, "businessNum": 457, "contractNum": 546,"recordNum": 234, "receivablesNum": 55, "businessStatusNum": 88}, "error": ""}


@app.route('/', methods=["GET", "POST"])
def index():
    req=request.data
    time=req.split('"')[3]
    # print time
    if time=="today":
        return jsonify(resp_today)
    elif time=="yesterday":
        return jsonify(resp_yesterday)
    elif time=="month":
        return jsonify(resp_month)
    elif time=="week":
        return jsonify(resp_week)


if __name__ == '__main__':
    app.run()
