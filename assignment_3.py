from pprint import pprint

comp_map = {"T": "A", "A": "T", "G": "C", "C": "G"}
sample = "AAAACCCGGT"
answer = "ACCGGGTTTT"

def get_short_string_position(short_string, long_string):
	pos = long_string.find(short_string)
	if pos == -1:
		return None
	else:
		return pos

def fasta_file_to_dict(in_file):
	fasta = {}
	with open(in_file) as file_one:
	    for line in file_one:
		line = line.strip()
		if not line:
		    continue
		if line.startswith(">"):
		    active_sequence_name = line[1:]
		    if active_sequence_name not in fasta:
			fasta[active_sequence_name] = []
		    continue
		sequence = line
		fasta[active_sequence_name].append(sequence)

	return fasta

def sequence_complement(sequence):
	out_sequence = ""
	for base in sequence:
		out_sequence += complement(base)
	return out_sequence
def reverse_complement(sequence):
	return sequence_complement(sequence)[::-1]

def complement(base):
	return comp_map[base]

if __name__ == "__main__":
	print "test..."
	print sample
	print reverse_complement(sample)
	fasta = fasta_file_to_dict("my_genome.fa")
	#pprint(fasta)
	print get_short_string_position("brown", "the quick brown fox")
 
