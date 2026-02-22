from Bio import SeqIO

goodreads_count = 0
read_count = 0

# Read input FASTQ, filters by average phred, and adds those filtered reads to a new FASTQ file
with open('sample1_rawReads.fastq', 'r') as infile, open('sample1_cleanReads.fastq', 'w') as outfile:
    for record in SeqIO.parse(infile, 'fastq-sanger'):
        read_count += 1
        
        # Calculate average phred quality
        avg_phred = sum(record.letter_annotations['phred_quality']) / len(record.letter_annotations['phred_quality'])

        if avg_phred >= 30:
            goodreads_count += 1
            SeqIO.write(record, outfile, "fastq")


# Print outputs
print(f"Total reads in original file: {read_count}")
print(f"Reads passing filter: {goodreads_count}")
