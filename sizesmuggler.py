#!/usr/local/bin/python3

import argparse
import logging

def cl_te_size(args):

	length = 0
	linebreak = "\r\n"
	
	with open(args.f, 'r') as lines:
		text = lines.read()
		text = linebreak.join(text.splitlines())
		length += len(text)
	logging.info(f"\r\nCL TE smuggling:")
	logging.info(f"Size for Content-Length: {length}\r\n")




def te_cl_size(args):

	length = 0
	linebreak = "\r\n"
	
	with open(args.f, 'r') as lines:
		text = lines.read()
		text = linebreak.join(text.splitlines())
		length += len(text)
	te_size = format(length, 'x')
	cl_size = len(te_size)+2 # To add crlf
	logging.info(f"\r\nTE CL smuggling:")
	logging.info(f"Size for Transfer-Encoding: {te_size}")
	logging.info(f"Size for Content-Length: {cl_size}\r\n")


if __name__ == "__main__":
	logging.basicConfig(format='%(message)s',level=logging.INFO)
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", help="Txt file to import to print the length of the data for Transfer Encoding", required=True)
	parser.add_argument("-t", help="Type of smuggling. Could be CLTE or TECL.", required=True)
	args = parser.parse_args()
	if args.t != "TECL" and args.t != "CLTE":
		logging.warning("Bad Smuggling argument. CLTE or TECL.")
		exit()
	if (args.t == "CLTE"):
		cl_te_size(args)
	elif (args.t == "TECL"):
		te_cl_size(args)
	else:
		logging.error("Something went wrong")
		exit()
