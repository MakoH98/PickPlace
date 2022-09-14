import json

json1_file = open('RobotPos.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)

json1_data = json1_data['poses_robot']
data = {}
print(json1_data[int(input('0/1'))]['name'])

print()