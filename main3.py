from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
seq=Seq("AGCT")#먼저 sequence객체를 만들고
seqRecord=SeqRecord(seq)#seqrecord객체를 만듦
print(seqRecord)

    #압축 풀기1
import gzip
# with gzip.open('S_20210809_027_P_R1.fastq.gz','wb') as f:
#     f.write(string.encode('utf-8')) #압축
import gzip
import pandas as pd
# Open the gzip-compressed FASTQ file in binary ('rb') mode
with gzip.open('E:\\USE\\CODE\\pycharm\\biotest\\S_20210809_027_P_R1.fastq.gz', 'rb') as f:
    original_string = f.read().decode('utf-8')
# Split the original string into lines to create a list of rows for the DataFrame
lines = original_string.strip().split('\n')
# Create a DataFrame with a single column 'Data' containing the lines from the FASTQ file
df = pd.DataFrame({'Data': lines})
# Save the DataFrame as a CSV file
df.to_csv('S_20210809_027_P_R1.csv', index=False)
with open('S_20210809_027_P_R1.txt', 'w', encoding='utf-8') as txt_file:
    for line in df['Data']:
        txt_file.write(line + '\n')
import gzip
from Bio import SeqIO
handle=gzip.open('S_20210809_027_P_R1.fastq.gz','rt')
seq=SeqIO.parse(handle,'fastq')
for s in seq:
    print(s.seq)
    #압축 풀기2

    #Sequence읽기

from Bio import SeqIO
