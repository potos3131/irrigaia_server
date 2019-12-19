import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irrigaia.settings")
django.setup()


import  api.models
import json

input_file="D:\irrigaia\data\scraped_items.json"
output_file="D:\irrigaia\data\output.json"


#
#
# # you can also keep this inside a view
#
# def import2db():
#     with open(input_file, encoding='utf-8') as data_file:
#         json_data = json.loads(data_file.read())
#         for item in json_data:
#             line = api.models.Vegetable.create_from_json_structure(**item)
#         data_file.close()
# def set_family():
#     output_data = json.dumps({})
#     with open(input_file, encoding='utf-8') as data_file:
#         json_data = json.loads(data_file.read())
#         for item in json_data:
#
#             if ( item['scient_name'] ):
#                 family = (item['scient_name'][0].split(' '))[0]
#                 item['family'] =  [family]
#             else:
#                 item['family'] = [None]
#             if ( item['family'] in dict('Cucurbita')):
#                 item['Kini']=0.4
#                 item['Kmid']=1
#                 item['Kend']=0.8
#
#                 item['Kini_days']= 0
#                 item['Kdev_days']= 0
#                 item['Kmid_days']= 0
#                 item['Kend_days']= 0
#                 item['Kini']= 0
#                 item['Kmid']= 0
#                 item['Kend']= 0
#             if (item['family'] in dict('Solanum')):
#                 return ''
#
#         data_file.close()
#     with open(output_file, 'w') as outfile:
#         outfile.write(json.dumps(json_data, indent=4, sort_keys=True))
#         outfile.close()
# set_family()


####import PIXELS######
input_file="./PIXELS.json"

with open(input_file, encoding='utf-8') as data_file:
    json_data = json.loads(data_file.read())
    for item in json_data:
        line = api.models.PixelModel.create_from_json_structure(**item)
    data_file.close()