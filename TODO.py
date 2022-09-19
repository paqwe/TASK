import argparse
import sys
def mytask(args):
	print("adding: ",args.add)
	print("listing: ",args.list)
	print("done: ",args.done)













if __name__=='__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--add',type=str,help="task name you want to add")
	parser.add_argument('--list',help="to list the current task list")
	parser.add_argument('--done',type=str,help="to mark the task as done")
	args = parser.parse_args()
	mytask(args)
	