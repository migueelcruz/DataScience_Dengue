#importação da biblioteca necessária 
from dbfread import DBF

#definindo variável com o nome do arquivo
db = r'DENGUE_2019.dbf'

#definindo variável com o caminho do arquivo
path = r'/home/miguel/Área de Trabalho/tcc/'

#variável dbf recebe um objeto DBF passando parametro o arquivo da base de dados
dbf = DBF(db, encoding='latin1')

#definindo os campos do DBF a serem exportados
headers = ['NU_NOTIFIC','TP_NOT','ID_AGRAVO','DT_NOTIFIC','SEM_NOT','NU_ANO','SG_UF_NOT','ID_MUNICIP','ID_REGIONA',
'ID_UNIDADE','DT_SIN_PRI','SEM_PRI','DT_NASC','NU_IDADE_N','CS_SEXO','CS_GESTANT','CS_RACA','CS_ESCOL_N','SG_UF',
'ID_MN_RESI','ID_RG_RESI','ID_DISTRIT','ID_BAIRRO','NM_BAIRRO','CS_ZONA','ID_PAIS','DT_INVEST','ID_OCUPA_N','TP_SISTEMA',
'NDUPLIC_N','DT_DIGITA','DT_TRANSUS','DT_TRANSDM','DT_TRANSSM','DT_TRANSRM','DT_TRANSRS','DT_TRANSSE','NU_LOTE_V','NU_LOTE_H',
'CS_FLXRET','FLXRECEBI','IDENT_MICR','MIGRADO_W','febre','mialgia','cefaleia','exantema','vomito','nausea','dor_costas',
'conjuntvit','artrite','artralgia','petequia_n','leucopenia','laco','dor_retro','diabetes','hematolog','hepatopat',
'renal','hipertensa','acido_pept','auto_imune','evolucao','dt_obito']

#Escrevendo o arquivo csv com as informações lidas da base de dados, usando o delimitador ";"
with open(path + 'Dengue.csv','w',encoding='utf-8') as f:
    for i in headers:
        f.write(i+';')
    f.write('\n')
    for record in dbf:
        for header in headers:
            f.write(str(record[header.upper()])+';')
        f.write('\n')
