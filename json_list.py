#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-05-15 00:50:25
@lastTime: 2020-05-15 01:46:53
@FilePath: \Turing\json_list.py
@Description: 
@version: 
'''


#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: LEGEND
@since: 2020-05-15 00:50:25
@lastTime: 2020-05-15 00:50:25
@FilePath: \Turing\json_list.py
@Description: 
@version: 
'''


# dd = {"c":{"a":1,"b": 2}}
# print(dd["c"]["a"])

d = {"data":
     {
         "contents":
        [
            {"cluster": {
                "id": 1,
                "name": "mike1"
            }
            },
            {"cluster": {
                "id": 2,
                "name": "mike2"
            }
            },
            {
                "context": "c"
            }
        ],
            "page": 10
        }
     }

for d in d["data"]["contents"]:
    # print("我", type(d))
    for k,v in d.items():
        if k == 'cluster':
            if v.get("name") == "mike2":
                print("OK")
            

        
