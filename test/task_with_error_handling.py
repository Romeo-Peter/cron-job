import argparse
import sys
import logging

# Log fomat
LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG

def main(number, other_number, output):
	result = number / other_number
	print(f'The result is {result}', file=output)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Running Cron Job...')
	parser.add_argument('-n1', type=int, help='A number', default=1)
	parser.add_argument('-n2', type=int, help='Another number', default=1)
	parser.add_argument('--config', '-c', type=argparse.FileType('r'), dest='config', help='config file')
	parser.add_argument('-o', dest='output', type=argparse.FileType('w'), help='Output file', default=sys.stdout)
	parser.add_argument('-l', type=str, dest='log', help='Log file', default=None)

	args = parser.parse_args()

	if args.log:
		logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, filename=args.log)
	else:
		logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

	try:
		main(args.n1, args.n2, args.output)
	except Exception as e:
		logging.exception('Error running task')
		print('Error. Please check log file for more.', file=args.output)
		exit(1)
	