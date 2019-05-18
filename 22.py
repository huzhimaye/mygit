import requests
import time
with open('E:/yangzengyan/Desktop/11.txt','w')as w:
    headers={
    'Host':'variation.ic4r.org',
    'Referer':'http://variation.ic4r.org/search?chrom=-',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }
    for start in range(18161):
        url = "http://variation.ic4r.org/search?chrom=-&draw=1&columns%5B0%5D%5Bdata%5D=accession&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=pos&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=alleles&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=maf&columns%5B3%5D%5Bname%5D=&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=cons&columns%5B4%5D%5Bname%5D=&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=asc&start={}&length=1000&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1557976474146".format(start*1000)
        print(time.strftime("%H:%M:%S", time.localtime())+' the %sk snp poision download' % (start+1))
        try:
            response=requests.post(url,headers=headers,timeout = None)
            response.raise_for_status()
        except requests.ConnectionError as e:
            w.write('Error:',e.args)
        linelist = response.json()['data']
        for slist in linelist:
            w.write(slist['accession']+'\t'+slist['pos']+'\t'+slist['alleles']+'\t'+slist['maf']+'\t'+slist['cons'][0]+'\n')