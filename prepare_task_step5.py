import argparse
import sys
import yaml

def main(number, other_number, outut):
	result = number * other_number
	print(f'The result is {result}', file=outut)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Running Cron Job...')
	parser.add_argument('-n1', type=int, help='A number', default=1)
	parser.add_argument('-n2', type=int, help='Another number', default=1)

	parser.add_argument('--config', '-c', type=argparse.FileType('r'), help='config file in YAML')
	parser.add_argument('-o', dest='output', type=argparse.FileType('w'), default=sys.stdout, help='Ouput file')

	args = parser.parse_args()

	if args.config:
		config = yaml.load(args.config, Loader=args.config)

		# Transform values into integers
		args.n1 = config['ARGUMENTS']['n1']
		args.n2 = config['ARGUMENTS']['n2']

	main(args.n1, args.n2, args.output)