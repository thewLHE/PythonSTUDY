#변수 선언
Gv=[]#annotation읽어온거 넣는것
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

GN=open("C:/Users/dmsdl/Desktop/JupyterJ/HG/GCF_000001405.40_GRCh38.p14_genomic.gff")
GNV=GN.readlines()
print("test start\n")
for line in GNV:
    if(line.startswith("#")):
        continue
    #print(line)#type : string
    line.rstrip()
    Gv.append(line.split("\t"))
#print(Gv)#2차 list
GN.close()
#print(len(Gv))#총 리스트 갯수

Nav=open("C:/Users/dmsdl/Desktop/JupyterJ/HG/GCF_000001405.40_GRCh38.p14_genomic.fna")
NavV=Nav.read()
NavV=''.join(NavV.split('\n')[1:])
Nav.close()
#print(NavV)#string type
print("END")

F_D=input("원하는 정보를 대소 구분하여 입력해주세요 : ")
#F_D="EcoRI"#change input
y=0;M=dict()
F_i=[]
for x in Gv:
    Data=str(x[8]).strip()
    Data=list(Data.split(";"))
    for D in Data:
        if F_D in D:
            F_i=D
            #print("Find!",Data)
            if(Name.find("ID=")==0):
                M[(Name,x[6])]=[x[3],x[4],Data]#value determine
                #print(x[3])#seq first
            else:
                break
        else: 
            continue#only keyword data Insert
    Name=Data[0]
"""
for k, v in M.items():
    print("{} : {}".format(k, v))
"""
#print(M)#키와 값  전부 출력
#print(Data)
"""
['ID=NC_000001.11:1..248956422', 'Dbxref=taxon:9606', 'Name=1', 'chromosome=1', 'gbkey=Src', 'genome=chromosome', 'mol_type=genomic DNA']
['ID=gene-DDX11L1', 'Dbxref=GeneID:100287102,HGNC:HGNC:37102', 'Name=DDX11L1', 'description=DEAD/H-box helicase 11 like 1 (pseudogene)', 'gbkey=Gene', 'gene=DDX11L1', 'gene_biotype=transcribed_pseudogene', 'pseudo=true']
"""
print("END2")

seq="";t_seq=""
for k, v in M.items():
    print(">",k[0],"\tSeq",k[1])
    F_n=int(v[0])-1
    L_n=int(v[1])-1
#t_seq=NavV[F_n:L_n]
    rS=""
    x=0
    if(k[1]=="-"):
        seq=NavV[F_n:L_n]
        while len(seq)>=x:
            rS+=seq[len(seq)-x-1]
            x+=1
        print("RSEQ:",seq)
        print("{}".format(v))
    else:
         seq=NavV[F_n:L_n]       #임시적으로 +로 간주
         print("FSEQ:",seq)
         print("{}".format(v))
    print("\n")
print("END3")