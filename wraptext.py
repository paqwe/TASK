# import math
# s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# n=4
# loopcount=len(s)/n
# print(loopcount)
# a = (math.ceil(loopcount))
# print(a) 

# print(loopcount)
# print(s[0:4])
# print(s[4:8])
# print(s[8:12])
# print(s[12:16])
# print(s[16:20])
# print(s[20:24])
# print(s[24:28])
# for i in range(len(s)):
	# print(s,"\n")
# j=0
# for i in range(0,7):
# 	print(s[j:j+4])



s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n=4
i=0
result=''
while i<len(s):  
	result = result + (s[i:i+n]) + '\n'
	i+=n

print(result)

	
	













	
	








