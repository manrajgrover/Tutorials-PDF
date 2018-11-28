import urllib.request, sys

def report(blocknr, blocksize, size):
    current = blocknr*blocksize
    sys.stdout.write("\r{0:.2f}%".format(100.0*current/size))

def downloadFile(url):
    print ("\n",url)
    fname = url.split('/')[-1]
    print (fname)
    urllib.request.HTTPSHandler(url, fname, report)
#    urllib.request.urlretrieve(url, fname, report)


tld = "http://www.tutorialspoint.com/"
#enter any tutorials url name from the website
#in the future we could scrape and show a menu
print ("Name of Tutorial? ")
query = input()

url =  tld+query+'/'+query+'_tutorial.pdf'

downloadFile(url)

print ("\nTutorial for " + query + " has been downloaded\n")
~                                                                    
