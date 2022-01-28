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
	te_size = format(length, 'x')
	cl_size = len(te_size)+2 # To add crlf
	logging.info(f"Size for Transfer-Encoding:\r\n{te_size}")
	logging.info(f"Size for Content-Length:\r\n{cl_size}")


if __name__ == "__main__":
	logging.basicConfig(format='%(message)s',level=logging.INFO)
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", help="txt file to import to print the length of the data for Transfer Encoding", required=True)
	args = parser.parse_args()
	cl_te_size(args)
