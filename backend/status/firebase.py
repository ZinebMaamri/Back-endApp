# -*- coding: utf-8 -*-
"""

@author: zineb
"""

import firebase
firebase = firebase.firebase.FirebaseApplication('https://text2stat-default-rdb.firebaseio.com/',None)
result=firebase.get('/text2stat-default-rdb/posts','')
print(result)