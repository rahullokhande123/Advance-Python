
#========================= dumps() Python to json ==========================
import json
python_data={
    'name':'Rahul',
    'city':'Bhopal',
    'age':24
}
json_data=json.dumps(python_data)
print(json_data)

print(type(json_data))
# # ====================================
python_data=json.loads(json_data)
print(python_data)
print(type(python_data))

#======================== loads() Json to python ===========================

json_data='''{
    "name":"Rahul",
    "city":"Bhopal",
    "age":24
}'''

print(type(json_data))
python_data=json.loads(json_data)
print(python_data)