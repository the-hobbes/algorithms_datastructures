"""External sort.
		What happens when you need to sort (or process) a very large file, too large
		to read into memory? You can break it into pieces small enough to fit into
		memory (chunks), and sort the data in each of these chunks. Sorted chunks
		are written back into memory. Finally, once all the chunks are sorted, they
		can be merged together (perhaps two at a time). At the end, we'll have a
		fully sorted file.
"""
import sys 


def readEachLine():
	"""Process a file line by line. 
			This is ok if the lines are reasonably sized, but if they are large (or
			there are no newlines) then you may run into trouble reading large amounts
			of data into memory.
	"""
	linecount = 0
	with open('loglines.txt') as logfile:
		for line in logfile:
			linecount += 1
	return linecount

def readEachChunk():
	"""Process a file in fixed-size chunks.
			Print out the size of each chunk.
	"""
	totalsize = 0
	with open('chunkfile.txt') as chunkfile:
		while True:
			chunk = chunkfile.read(1024)
			if not chunk:
				break
			totalsize += sys.getsizeof(chunk)
	return totalsize


def main():
	# Generate large files with:
	# https://www.skorks.com/2010/03/how-to-quickly-generate-a-large-file-on-the-command-line-with-linux/
	# Generated: for i in {1..20}; do cat loglines.txt loglines.txt > loglines2.txt && mv loglines2.txt loglines.txt; done
	assert readEachLine() == 2097152
	# Generated: dd if=/dev/zero of=chunkfile.txt count=3024 bs=2024
	assert readEachChunk() == 6341762


if __name__ == '__main__':
	main()