from flask import jsonify


def success_api(msg: str="success"):
    return jsonify(success=True, msg=msg)


def fail_api(msg: str="fail"):
    return jsonify(success=False, msg=msg)


def table_api(msg: str="", count=0, data=None, limit=10):
    res = {
        'msg': msg,
        'code': 0,
        'data': data,
        'count': count,
        'limit': limit
    }
    return jsonify(res)


def res_api(msg, success=True, status=True, data=None):
    res = {
        'message': msg,
        'success': success,
        'status': status,
        'data': data
    }

    return jsonify(res)

