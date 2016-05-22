#! /usr/bin/python
import cgi
import os
import shutil
from stegano import lsb
from stegano import exifHeader

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type: text/html'

HEAD = '''
<!DOCTYPE html>
<html lang='en'>
    <head>
          <meta charset="UTF-8">
          <title>Success</title>
    </head>
    <body>
'''

END = '''
    </body>
</html>    
'''

def main():
	print HTML_HEADER
	print HEAD
	data = cgi.FieldStorage()
	fileds = data['file']
	if fileds.filename.endswith('.jpg') or fileds.filename.endswith('.png') or fileds.filename.endswith('.jpeg') or fileds.filename.endswith('.tiff') and fileds.filename.count('/') == -1:
	    os.chdir('files')
	    with open(fileds.filename, 'wb') as fout:
	        shutil.copyfileobj(fileds.file, fout, 100000)
        os.chdir('../')
        # do NOT touch above code
        
        if fileds.filename.endswith('.png'):
            sec = lsb.hide('files/'+fileds.filename, data['message'].value)
            sec.save('files/'+fileds.filename)
        if fileds.filename.endswith('.jpg') or fileds.filename.endswith('.jpeg'):
            secret = exifHeader.hide('files/'+fileds.filename, 'files/'+fileds.filename, secret_message=data['message'].value)
        print "Successfully generated."
        print '<a href="http://jonathanwong.koding.io/bstego/files/'+fileds.filename+'">Link here</a>'
	print END

main()    
