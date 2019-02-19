#!/usr/bin/env python2

import argparse
import json

def create_file(json_output):
	with open(json_output, 'w') as f:
		program = {'papers': []}
		json.dump(program, f)

def process_json(json_input, json_output, input_type):
	# paper and poster program share identical file structures
	# the HTML shortcode decides which information to display

	with open(json_input) as f:
		data = json.load(f)
	
	papers = []

	for paper in data:
		paper_metadata = {}

		paper_metadata['_id'] = 'p' + str(paper['pid'])
		paper_metadata['title'] = paper['title']
		paper_metadata['abstract'] = paper['abstract']
		
		paper_metadata['authors'] = []
		
		# prettify authors
		authors_collect = []
		last_affiliation = paper['authors'][0]['affiliation']
		for author_info in paper['authors']:
			if author_info['affiliation'] == last_affiliation:
				authors_collect.append('%s %s' % (author_info['first'], author_info['last']))
			else:
				author = authors_collect[0]
				for ac in authors_collect[1:-1]:
					author += ', ' + ac
				if len(authors_collect) == 2:
					author += ' and ' + authors_collect[-1]
				elif len(authors_collect) > 2:
					author += ', and ' + authors_collect[-1]
				
				paper_metadata['authors'].append({
					'name': author,
					'affiliation': last_affiliation
				})
				
				authors_collect = ['%s %s' % (author_info['first'], author_info['last'])]
				last_affiliation = author_info['affiliation']

		author = authors_collect[0]
		for ac in authors_collect[1:-1]:
			author += ', ' + ac
		if len(authors_collect) == 2:
			author += ' and ' + authors_collect[-1]
		elif len(authors_collect) > 2:
			author += ', and ' + authors_collect[-1]
		
		paper_metadata['authors'].append({
			'name': author,
			'affiliation': last_affiliation
		})

		papers.append(paper_metadata)

	# load exisiting program and update paper info
	# program json file has to exist
	with open(json_output) as f:
		program = json.load(f)

		# loop over all papers parsed from json
		for paper in papers:
			# loop over all papers in existing program file
			for program_paper in program['papers']:
				# update paper if already in program
				if program_paper['_id'] == paper['_id']:
					program_paper.update(paper)
					break
			# paper not yet in program (for loop above)
			# so add to program
			else:
				program['papers'].append(paper)

	# write updated program to file
	with open(json_output, 'w') as f:
		json.dump(program, f, sort_keys=True,
			indent=4, separators=(',', ': '))
		f.write('\n')


def main():
	parser = argparse.ArgumentParser(description='Parse JSON exports from HotCRP')
	parser.add_argument('file', help='JSON file exported from HotCRP')
	parser.add_argument('--create', help='Create output files', action='store_true')

	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--papers', action='store_true', help='Input file contains paper info')
	group.add_argument('--posters', action='store_true', help='Input file contains poster info')

	args = parser.parse_args()

	if args.create:
		if args.papers:
			create_file('program.json')
		elif args.posters:
			create_file('posters.json')

	if args.papers:
		process_json(args.file, 'program.json', 'papers')
	elif args.posters:
		process_json(args.file, 'posters.json', 'posters')

if __name__ == '__main__':
	main()
