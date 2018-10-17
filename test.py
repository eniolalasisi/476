import urllib
urllib.urlopen("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")




#LOCAL_FILE = 'http_access_log.bak'

#print("\n\nDownloading log file... ")
#response = urllib.urlopen("https://s3.amazonaws.com/tcmg412-fall2016/http_access_log", "http_access_log")
#with open(LOCAL_FILE, "wb") as local:
#	local.write(response.read())
#print("File retrieved and saved to disk)


import urllib2

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
html = response.read()
line = len(html.splitlines())
print('Total requests: ',line)


from datetime import datetime

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
byWeekday = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

count = 0
for line in response:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: date = splitLine[3][1:12]

	except: pass

	
	try: formatted_date = datetime.strptime(date, "%d/%b/%Y")
	except: pass

	byWeekday[formatted_date.weekday()] += 1


weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for i in range(7):
	print(weekDays[i]+ ' requests '+  ': '+ str(byWeekday[i]))




from datetime import datetime

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
byMonth1994 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
byMonth1995 = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

count = 0
for line in response:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: date = splitLine[3][1:12]

	except: pass

	
	try: formatted_date = datetime.strptime(date, "%d/%b/%Y")
	except: pass

	for key in byMonth1994:
		if formatted_date.isocalendar()[0] == 1994:
			if formatted_date.month == key:
				byMonth1995[formatted_date.month] += 1
		else: 
			if formatted_date.month == key:
                                byMonth1995[formatted_date.month] += 1
	




months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']


for i in range(12):
	print('1994 requests for '+ months[i]+ ': '+ str(byMonth1994[i+1]))

for i in range(12):
        print('1995 requests for '+ months[i]+ ': '+ str(byMonth1995[i+1]))



from datetime import datetime

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
byWeek1994 = {}
byWeek1995 = {}
count = 0
for line in response:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: date = splitLine[3][1:12]

	except: pass

	try: formatted_date = datetime.strptime(date, "%d/%b/%Y")
	except: pass

	iso_tuple = formatted_date.isocalendar()
	for key in range(53):
		if 1994 == iso_tuple[0]:
			if key not in byWeek1994.keys():
				byWeek1994[key] = 0
			else:
				if key == iso_tuple[1]:
					byWeek1994[key] += 1
		if 1995 == iso_tuple[0]:
                        if key not in byWeek1995.keys():
                                byWeek1995[key] = 0
                        else:
                                if key == iso_tuple[1]:
                                        byWeek1995[key] += 1



week = []
string='week'
for i in range(53):
	weekNum = string + ' ' + str(i)
	week.append(weekNum)

for key in range(53):
		print('1994 requests for '+ week[key]+ ': '+ str(byWeek1994[key]))
for key in range(53):
		print('1995 requests for  '+ week[key]+ ': '+ str(byWeek1995[key]))


import re

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
statusList = []

count = 0
for line in response:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: status = splitLine[8]
	except: pass

	try: statusInt = int(status)
	except: pass

	statusList.append(statusInt)

numUnsuccessful=0
for i in statusList:
	if 400 <= i <= 499:
		numUnsuccessful += 1

print('Percentage of unsuccessful requests: ' + str(100*(numUnsuccessful/726736.0)))


import re

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
statusList = []

count = 0
for line in response:
	count += 1
	lineList.append(line)

for i in range(len(lineList)):
	splitLine = lineList[int(i)].split()

	try: status = splitLine[8]
	except: pass

	try: statusInt = int(status)
	except: pass

	statusList.append(statusInt)

numSuccessful=0
for i in statusList:
	if 300 <= i <= 399:
		numSuccessful += 1



print('Percentage of redirected requests: ' + str(100*(numSuccessful/726736.0)))


import operator

response = urllib2.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')

lineList = []
reqCount = {}
reqFileList = []

count = 0
for line in response:
	count+=1
	lineList.append(line)

for i in range(len(lineList)):
	listSplit = lineList[int(i)].split()
	try: reqFile = listSplit[6]
	except: pass
	reqFileList.append(reqFile)

for key in reqFileList:
	if key not in reqCount:
		reqCount[key] = 1
	else:
		if key in reqCount:
			reqCount[key] += 1


mostRequested = max(reqCount.items(), key=operator.itemgetter(1))[0]
leastRequested = min(reqCount.items(), key=operator.itemgetter(1))[0]

print(str(mostRequested) + ' was requested the most, ' + str(reqCount['index.html']) + ' times')
print(str(leastRequested) + ' was requested the least, ' + str(reqCount['7512.map?159,276']) + ' times')



