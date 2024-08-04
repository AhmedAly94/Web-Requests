import requests

#GET request
#payload = {'page':2,'count':25}
#r = requests.get('https://httpbin.org/get',params=payload)
#print(r.text)
#print(r)
#print(r.headers)

#POST request
#payload = {'username':'ahmed','password':'ok'}
#r = requests.post('https://httpbin.org/post',data=payload)

#Authentication request
r = requests.get('https://httpbin.org/basic-auth/ahmed/ok',auth =('ahmed','ok'))
#r_dict = r.json()
#print(r_dict)
#print(r_dict['form'])
#print(r.url)
#print(r.status_code) #if 200 means successfull request

#print(dir(r)) #built-in Python function that is used to list the attributes and methods of an object
#print(help(r))

#downloadImage
with open('comic.png','wb')as f:
    f.write(r.content)  




