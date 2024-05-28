import re
import requests

def remove_brackets(text):
  return re.sub(r"<.*?>", "", text)

for i in range(90000,90101):
  url = "https://diemthi.vnexpress.net/diem-thi-lop-10/detail/id/1_"
  url+=str(i)
  result = requests.get(url).text

  source = remove_brackets(result)

  start = source.find("Môn thi")
  end = source.find("Facebook")

  source = source[start:end]

  check = False
  main = ""
  dem = 0
  source.replace('\n','')
  source.replace(' ','')
  for j in range(0,len(source)):
    if( source[j].isdigit() or source[j] == '.' ):
      main+=source[j]
      check = True
    elif (check == True):
      main+=','
      check = False
      dem+=1
  main = main[:-1]
  if dem == 4:
    vt = main.rfind(",")
    smain = main[:vt]
    emain = main[vt:]
    main = smain + ",0" + emain
  main = str(i) + ',' + main + '\n'
  with open("sbd.csv","a") as file:
    file.write(main)
  file.close()



