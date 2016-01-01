from lxml import html
import requests
import csv,os,time
joiner=' , '
def modifyEntry(entry):
    if len(entry)==0:
        entry.append('')
def createTree(link):
    page = requests.get(link)
    tree = html.fromstring(page.text)
    return tree

def extractLinkWithTree(tree,xpath):
    temp = tree.xpath(xpath)
    #print temp
    return temp

def extractLink(link,xpath):
    return extractLinkWithTree(createTree(link),xpath)

def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output

def justdial(keyword,state):
  mainPageLink="http://www.justdial.com/"+state+"/"+keyword
  dir_path=keyword
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)
  print "Extracting data:\nPlease wait...\n"
  pageLink=[mainPageLink]
  pageLink+=extractLink(mainPageLink,'//*[@class="jpag"]/a/@href')

  for x in pageLink:
    pageLink+=extractLink(x,'//*[@class="jpag"]/a/@href')
    print pageLink
    pageLink=uniq(pageLink)
    #break


  print "\n\n\nPage List Prepared. Writing to file page_list.csv\n"
  print "Writing to file page_list.csv completed.\n"
  print "Analysing  pages..\n"
  print "Extracting entries"


  global i
  global path
  i = 0



        
  for page in pageLink:
    print page
    a = page.split("page-")
  
    try:
      print i
      if int(i) < int(a[1]):
            i = int(a[1])
            path = a[0]
            print i
      else:
            print "else"
    except:
      print "no pages"
  new_link = []
  a = 1
  print i
  with open(dir_path+'/final_list.csv', 'wb') as csvfile:
      spamwriter1 = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      for a in range(1,i+1):
            if int(a)<=int(i):
              new_link = path+"page-"+str(a)
              spamwriter1.writerow([new_link]) 
   
   
  for x in pageLink:
    new_link=pageLink+extractLink(x,'//*[@class="jpag"]/a/@href')
    new_link = uniq(new_link) 
   
   
   
   
   
  

   
   
  with open(dir_path+'/'+state+'.csv', 'wb') as csvfile:
      spamwriter = csv.writer(csvfile, delimiter=',',
                  quotechar='"', quoting=csv.QUOTE_MINIMAL)   
   
   
   
   
   
      for page in new_link:

          for LinkInPage in extractLink(page,'//p[@class="jcnwrp"]/span/a/@href'):
              while (1):
                  tree=createTree(LinkInPage)
                  name=extractLinkWithTree(tree,"//*[@class='fn']/text()")
                  address=extractLinkWithTree(tree,"//*[@class='jaddt']/span/text()")
                  tag=extractLinkWithTree(tree,"//*[@id='alsp']/section[@class='jpbg']/section[@id='alsol']/table[@class='tblrw']/tr/td/a/text()")
                  tag=uniq(tag)
                  tel=extractLinkWithTree(tree,"//*[@class='tel']//text()")
                  tel=uniq(tel)
                  website=extractLinkWithTree(tree,"//*[@class='wsurl']/a/@href")
                  rating=extractLinkWithTree(tree,"//*[@class='value-title']/@title")
                  rating=uniq(rating)
                  website=uniq(website)
                  establish=extractLinkWithTree(tree,"//*[@class='fcont'][last()]/text()[2]")
                  print rating
                  modifyEntry(website)
                  modifyEntry(address)
                  modifyEntry(tel)
                  modifyEntry(establish)
                  modifyEntry(rating)
                  modifyEntry(name)
                  row= [(name[0].strip()).encode('ascii','ignore')]+[address[0].strip().encode('ascii','ignore')]+[((joiner.join(tel)).strip()).encode('ascii', 'ignore')]+[website[0].strip().encode('ascii','ignore')]+[establish[0].strip().encode('ascii','ignore')]+[rating[0].strip().encode('ascii','ignore')]+[((joiner.join(tag)).strip()).encode('ascii', 'ignore')]
                  #row=row1.encode('ascii','ignore') 
                  if (row!=['','','','']):
                     #print (row!=['','','',''])
                      break
                
              time.sleep(1)
              spamwriter.writerow(row)        
              print row
      #break
  os.remove(dir_path+'/final_list.csv')
  print "Fetching entries finished"
