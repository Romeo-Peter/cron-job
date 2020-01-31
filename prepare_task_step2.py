import argparse
import configparser

def main(number, other_number):
	result = number * other_number
	print(f'The result is {result}')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Running Cron Job...')
	parser.add_argument('-n1', type=int, help='A number', default=1)
	parser.add_argument('-n2', type=int, help='Another number', default=1)

	parser.add_argument('--config', '-c', type=argparse.FileType('r'), dest='config' help='config file')

	args = parser.parse_args()

	if args.config:
		config = configparser.ConfigParser()
		config.read_file(args.config)

		# Transform values into integers
		args.n1 = int(config['DEFAULT']['n1'])
		args.n2 = int(config['DEFAULT']['n2'])
	main(args.n1, args.n2)