#!/usr/bin/python

docs = [(('01JavaWhyWhat.pdf', 8), 6),
    (('02LearnJAVAwhite.pdf', 12), 1),
    (('03IO.pdf', 13), 6),
    (('04DynamicMemory.pdf', 9), 6),
    (('05ClassesObjects.pdf', 9), 6),
    (('06CreateClassObjects.pdf', 12), 6),
    (('07OODesign.pdf', 11), 6),
    (('08JDBC.pdf', 8), 6),
    (('09GraphicUserInterface.pdf', 18), 6),
    (('11GraphicObjects.pdf', 10), 6),
    (('13AppletsApplications.pdf', 13), 6),
    (('14Threads.pdf', 16), 6),
    (('15JavaSocket.pdf', 22), 6),
    (('20ME.pdf', 28), 1)]

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

for files in docs:
  if files[1] == 6:
    print6(files[0])
  elif files[1] == 1:
    print1(files[0])

print '%\end{textblock*}'
print '\end{document}'

