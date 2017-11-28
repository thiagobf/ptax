#Author: Thiago Fernandes
#Date: 27/11/2017
#Description: Retrieve the exchange rates with Brazillian Real and other currencies parity, PTAX. csv format file
#parameters: DATAINI = Start Date, Format DD/MM/YYYY
#            DATAFIM = End Date, Format DD/MM/YYYY
import urllib2
import sys

url = "https://ptax.bcb.gov.br/ptax_internet/consultaBoletim.do?method=gerarCSVFechamentoMoedaNoPeriodo&ChkMoeda=61&DATAINI=:DI&DATAFIM=:DF"

DATAINI=sys.argv[1]
DATAFIM=sys.argv[2]
url.replace(":DI", DATAINI);
url.replace(":DF", DATAFIM);
print "Currencies parity for Brazillian Real" 
print "Downloading from " + url

file_name = "ptax_"+DATAINI+"_"+DATAFIM+".csv"
filename = file_name.replace("/","_");
u = urllib2.urlopen(url)
f = open(filename, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading PTAX: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()
