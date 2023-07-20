    #case01
from Bio import Entrez

Entrez.email='dmsdl58@naver.com'
handle=Entrez.egquery(term='bioinfomatics')#query란 데이터 베이스에 정보를 요청하는 행위를 의미한다. 인터넷 사용환경에 따라 시간걸릴지도
record=Entrez.read(handle)# read매서드로 handle을 읽어 record변수에 넣는다

#record변수에 딕셔너리와 같은 데이터가 들어가 있으며, 키 값으로 접근하여 query결과값을 알 수 있다.
#pubmed의 결과에서 논문 수를 알아 볼 것이다.
for result in record['eGQueryResult']:
    if result['DbName']=='pubmed':
        print(result['Count'])

    #case02
from Bio import Entrez
from Bio import GenBank

handle=Entrez.efetch(db='nucleotide',id='KT225476',rettype='gb',retmode='text')
    #Entrez의 efech메서드로 nucleotide데이터베이스의 KT22546 id를 가진 GenBank파일을 읽는객체를 handle에 저장한다
record =GenBank.read(handle)#handle을 읽어 record에 넣는다.
print("Accession:",record.accession)#KT225476의 GenBank정보에서 필요한 정보를 파싱하는 방법은 단순히 record객체에서 객체 변수를 호출하면 된다
print('Organism:',record.organism)#record객체에서 organism을 출력할 수 있음
print("Size:",record.size)

    #BLAST(Basic Local Aligment Search Tool) case03
        #:염기서열 또는 단백질 서열을 입력 받아 데이터 베이스를 검색하여 유사한 서열을 찾아 정보를 알려주는 생물정보학 툴
        #이의 결과는 XML형식으로 저장 가능하며, 이 결과 파일을 통해 NCBIXML모듈로 파싱할 수 있음
from Bio.Blast import NCBIWWW
    #여기서는 미지의 서열이 담긴 Fasta파일을 바이오 파이썬의 NCBIWWW모듈로 BLAST를 진행하고 NCBIXML모둘로 BLAST결과 파일을 파싱하는 예제
from Bio.Blast import NCBIWWW
from Bio import SeqIO

record=SeqIO.read("blastSample.fasta",format='fasta')#SeqIO모듈 이용하여 미지의 종의 서열이 담긴 fasta 파일을 읽어 record변수에 넣는다
result_handle=NCBIWWW.qblast('blastn','nt',record.format('fasta'))#NCBIWWW모듈dml qblast메서드를 이용하여 BLASTS를 진행한다
with open('blast_result.xml','w')as out_handle:#BLast결과를 XML파일로 쓴다.
    out_handle.write(result_handle.read())
result_handle.close()

from Bio.Blast import NCBIXML#임포트
result_handle=open('blast_result.xml')
blast_records=NCBIXML.parse(result_handle)#NCBIXML모듈의 parse매서드로 결과 파일을 연 객체를 파싱한다.

#파싱된 결과에서 필요한정보를 출력한다.
for blast_record in blast_records:
    for alignment in blast_record.aligments:
        for hsp in alignment.heps:
            print(alignment.title)
result_handle.close()#열었던 XML파일 객체를 닫는다.