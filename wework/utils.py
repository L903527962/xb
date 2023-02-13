"""
工具类
"""
import json

from wework import app


def datajson(filejson):
    emp_list = []
    with open(file=filejson, mode='r', encoding='utf-8') as f:
        data = json.load(f)
        for i in data:
            emp_list.append(tuple(i.values()))
        return emp_list
if __name__ == '__main__':
    request_body=datajson(app.BASE_DIR +'/data/create_member.json')
    print(request_body)