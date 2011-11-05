#!/usr/bin/python

# Format (('<filename>', <number of pages in pdf>), <number of slides per page>)
# Currently only support 1 or 6 slides per page
docs = []

def print1page( fileName, page ):
  print '\includegraphics[width=20cm,height=15cm,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'

def print6page( fileName, page ):
  print '\includegraphics[width=20cm,height=15cm,trim=73px 534px 320px 95px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'
  print '\includegraphics[width=20cm,height=15cm,trim=332px 534px 61px 95px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'
  print '\includegraphics[width=20cm,height=15cm,trim=73px 314px 320px 314px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'
  print '\includegraphics[width=20cm,height=15cm,trim=332px 314px 61px 314px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'
  print '\includegraphics[width=20cm,height=15cm,trim=73px 95px 320px 534px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'
  print '\includegraphics[width=20cm,height=15cm,trim=332px 95px 61px 534px,page=' + str(page) + ']{' + fileName + '}'
  print '\\newpage'

def print1( fileInfo ):
  print '\section{\'' + fileInfo[0] + '\'}'
  print '\\newpage'
  for pgNum in range( fileInfo[1] ):
    print1page( fileInfo[0], pgNum + 1)

def print6( fileInfo ):
  print '\section{\'' + fileInfo[0] + '\'}'
  print '\\newpage'
  for pgNum in range( fileInfo[1] ):
    print6page( fileInfo[0], pgNum + 1)

print '\documentclass[10pt]{article}'
print '\usepackage[papersize={20cm,15cm},margin=0px]{geometry}'
print '\usepackage[utf8]{inputenc}'
print '\usepackage{color}'
print '\usepackage{xcolor}'
print '\usepackage{graphicx}'
print '\usepackage[bookmarks]{hyperref}'
print '%\usepackage[absolute]{textpos}'
print '\\thispagestyle{empty}'
print ''
print '\\begin{document}'
print '\\tableofcontents'
print '\\newpage'

for files in docs:
  if files[1] == 6:
    print6(files[0])
  elif files[1] == 1:
    print1(files[0])

print '%\end{textblock*}'
print '\end{document}'

