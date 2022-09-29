import argparse
import sys
import json

task_file='todolist.json'
def printwithformat(x,y):
	print(x,"\t",y)

def mytask(args):

	import hashlib
	if args.add:
		with open(task_file) as abc:
			finaldata = json.load(abc)
		# finaldata["tasklist"].append(args.add)
		d = hashlib.sha256(str.encode(args.add))
		# print(d)
		k = d.hexdigest()
		# print(k)
		# print(k[0:6])
		identifier=k[0:6]
		finaldata["tasklist"][identifier]= args.add
		json_object=json.dumps(finaldata, indent=4)
		with open(task_file, "w") as outfile:
			outfile.write(json_object)
		

    
	elif args.done:
		with open(task_file) as f:
			data = json.load(f)
		# data["tasklist"].remove(args.done)
		data["tasklist"].pop(key)
		json_object=json.dumps(data, indent=4)
		with open(task_file, "w") as m:
			m.write(json_object)
			




	elif args.list:
		with open(task_file) as f:
			data = json.load(f)
			printwithformat("TASK_ID","TASK_NAME")
			for key,value in data['tasklist'].items():
				printwithformat(key,value)
				# data['tasklist'][identifier] = args.add
				# printwithformat(identifier,args.add)




					
			
if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--add',type=str,help="task name you want to add")
	parser.add_argument('--list',action='store_true',help="to list the current task list")
	parser.add_argument('--done',type=str,help="to mark the task as done")
	args = parser.parse_args()
	mytask(args)
	


