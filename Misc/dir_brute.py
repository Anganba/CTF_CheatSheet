import requests

i=0
while(i<100):
	a = requests.get("http://MACHINE_IP/dir/?parameter="+str(i))
	b= a.text
	if("wrong" not in b):
		print(b)
	i=i+1