from Bio.Seq import Seq
tatabox_seq=Seq("tataaaagggccAATTAGCTAGTAG")
print(tatabox_seq)
print(type(tatabox_seq))
print(dir(Seq))

from Bio.Alphabet import IUPAC
tatabox_seq=Seq("tataaaaaagggcAATAGCACTAG",IUPAC.unambiguous_dna)#ACGT만 추출하는 dna서열
print(tatabox_seq)

from Bio.Seq import Seq
exon_seq=Seq("ATGCAGTAG")
count_a=exon_seq.count("A")
print(count_a)

g_count=exon_seq.count("G")
c_count=exon_seq.count("C")
gc_contents=(g_count+c_count)/len(exon_seq)*100
print(gc_contents)

from Bio.Seq import Seq
dna=Seq("ATGCAGTAG")
mran=dna.transcribe()#1)전사 :
ptn=dna.translate()#2)번역 :
print(mran)#AUGCAGUAG
print(ptn)#MQ*

mRNA=Seq("AUGAACUSSGUUUAGAAU")#
ptn=mRNA.translate()
print(ptn)#MNXV*N 중간에 종결 코돈이 나오게 된다.
ptn=mRNA.translate(to_stop=True)
print(ptn)#MNXV

for seq in ptn.split('*'):#종결 코돈으로 서열 구분
    print(seq)  #MNXV
                #N

#상보적(complement):각각 쌍을 이루고 있는것
#역상보():상보적인 관계에서 방향을 뒤집는것[to 5->3]
seq="TATAAAAGGCAATATGCAGTAG"
comp_dic={"A":"T","C":"G","G":"C",'T':'A'}#상보적 염기를 키 값으로 하는 사전 제작
comp_seq=""
for s in seq:
    comp_seq+=comp_dic[s]
revcomp_seq=comp_seq[::-1]
print(comp_seq)
print(revcomp_seq)

seq=Seq("TATAAAAGGCAATATGCAGTAG")
comp_seq=seq.complement()
rev_comp_seq=seq.reverse_complement()
print(comp_seq)
print(rev_comp_seq)

from Bio.Data import CodonTable
codon_table=CodonTable.unambiguous_dna_by_name["Standard"]#전사 이후에mrna의 3개의 염기를 읽어 코돈 테이블에 맞춰 아미노산 제작
print(codon_table)

from Bio.Data import CodonTable
codon_table=CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]#미토콘드리아가 사용하는 코돈 테이블
print(codon_table)

#ORF(open reading frame)은 시작 코돈인 ATG부터 시작하여 종결 코돈인 TAA,TAG,TGA중 하나를 만나면 단백질을 만들 가능성 있음
from Bio.Seq import Seq
tatbox_seq=Seq("tataaaggcAATATATGCGATAG")
start_idx=tatabox_seq.find("ATG")
end_idx=tatbox_seq.find("TAG",start_idx)
orf=tatbox_seq[start_idx:end_idx+3]
print(orf)

from Bio.Seq import Seq
from Bio.SeqUtils import GC
exon_seq=Seq("ATGCAGTAG")
gc_contents=GC(exon_seq)
print(gc_contents)

#서열의 같을 지라도 DNA와 단백질 서열의 차이 떄문에 무게가 다름
from Bio.Seq import Seq
# from Bio.Alphabet import IUPAC#버전 업데이트로 제거됨
from Bio.SeqUtils import molecular_weight
seq1 = Seq("ATGCAGTAG")
#seq2 = Seq("ATGCAGTAG", IUPAC.unambiguous_dna)#버전 업데이트로 제거됨
# seq3 = Seq("ATGCAGTAG", IUPAC.protein)
print("seq1의 분자량:", molecular_weight(seq1))#seq1의 분자량: 2842.8206999999993
#print("seq2의 분자량:", molecular_weight(seq2))
# print("seq3의 분자량:", molecular_weight(seq3))

#DNA서열에서 가능한 모든 6개의 번역된 서열을 구할 수 있음
    #DNA 서열은 코돈이라는 세 개의 염기로 이루어진 부분으로 번역되며, 하나의 코돈은 아미노산으로 번역됩니다.
    #하지만 코돈은 각각의 방향으로 번역될 수 있으므로 DNA 서열은 세 개의 가능한 독립적인 방향으로 번역될 수 있습니다.
    #또한, DNA 서열은 양쪽 방향으로 독립적으로 번역될 수 있으므로 총 여섯 가지 번역이 가능합니다.
from Bio.Seq import Seq
from Bio.SeqUtils import six_frame_translations
seq1=Seq("ATGCCTTGAAATGATG")
print(six_frame_translations(seq1))
    #또는
from Bio.Seq import Seq
from Bio.SeqUtils import six_frame_translations
seq1 = Seq("ATGCCTTGAAATGATG")
translations = six_frame_translations(seq1)
for frame, protein_sequence in enumerate(translations, start=1):
    print(f"Frame {frame}: {protein_sequence}")

from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
my_seq=Seq("AGTCTCGGGACGGCGCCGAATCGCA")
print(mt.Tm_Wallace(my_seq))#84.0

#아미노산 섣열의 약자와 기호간 변환하기
from Bio.SeqUtils import seq1
essential_amino_acid_3="LeuLysMetValIleThr"
print(seq1(essential_amino_acid_3))#LKMVIT

#아미노산 약자를 서열 기호로 바꾸기
from Bio.SeqUtils import seq3
essential_amino_acid_1="LKMVITWF"
print(seq3(essential_amino_acid_1))#LeuLysMetValIleThrTrpPhe
