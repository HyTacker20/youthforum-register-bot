import json
import os

with open('projects/forumbot/data/data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
print(data)

# {'users':
#   [
        # {'user_id': '12524241', 
        # 'user_name': 'Andrew', 
        # 'user_surname': 'Hermak'},
        
        # {'user_id': '73456456', 
        # 'user_name': 'Maks', 
        # 'user_surname': 'Andrushchak'}
#   ]
#}