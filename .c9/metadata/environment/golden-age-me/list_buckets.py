{"filter":false,"title":"list_buckets.py","tooltip":"/golden-age-me/list_buckets.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":3},"action":"remove","lines":["\"\"\"","Your module description","\"\"\""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":21,"column":25},"action":"insert","lines":["","","#%%","","# list S3 Buckets","","import boto3","","s3 = boto3.client('s3')","","#%%","","response = s3.list_buckets()","","#%%","","buckets = response[\"Buckets\"]","","#%%","","for bucket in buckets:","    print(bucket[\"Name\"])"],"id":2}]]},"ace":{"folds":[],"scrolltop":283,"scrollleft":0,"selection":{"start":{"row":21,"column":25},"end":{"row":21,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1665624263863,"hash":"a1c88520e629f46d57d539eec5356bae7a9f3843"}