from pattern.web import *
w = Wikipedia()


file = open('figure_skating.txt','r')
all_text = file.read()



temp1 = all_text.split('Bronze')
a1 = temp1[1].split('\n\n')
a2 = temp1[3].split('\n\n')
a3 = temp1[4].split('\n\n')
a4 = temp1[5].split('\n\n')

men_singles = a1[1]
ladies_singles = a2[1]
pairs = a3[1]
ice_dancing = a4[1]


# men's single medalists

men_list = men_singles.split('\n')
del men_list[2]

men_olympic_year = []
men_gold = []
men_silver = []
men_bronze = []

for i in range(len(men_list)/2):
	year = men_list[2*i].split(' ')
	men_olympic_year.append(year[0])
	medalists = men_list[2*i+1].split('  ')
	men_gold.append(medalists[1])
	men_silver.append(medalists[2])
	men_bronze.append(medalists[3])

for j in [men_gold, men_silver, men_bronze]:
	for i in range(len(j)):
		a = len(j[i])
		j[i] = j[i][:a-6]




# ladies' single medalists

ladies_list = ladies_singles.split('\n')
del ladies_list[2]

ladies_olympic_year = []
ladies_gold = []
ladies_silver = []
ladies_bronze = []

for i in range(len(ladies_list)/2):
	year = ladies_list[2*i].split(' ')
	ladies_olympic_year.append(year[0])
	medalists = ladies_list[2*i+1].split('  ')
	ladies_gold.append(medalists[1])
	ladies_silver.append(medalists[2])
	ladies_bronze.append(medalists[3])


for j in [ladies_gold, ladies_silver, ladies_bronze]:
	for i in range(len(j)):
		a = len(ladies_gold[i])
		ladies_gold[i] = ladies_gold[i][:a-2]




# pairs medalists

pairs_list = pairs.split('\n')
del pairs_list[5]

pairs_olympic_year = []
pairs_gold = []
pairs_silver = []
pairs_bronze = []


for i in range(len(pairs_list)):
	if pairs_list[i][0] == '1' or pairs_list[i][0] == '2':
		year = pairs_list[i].split(' ')
		pairs_olympic_year.append(year[0])
	elif 'details' in pairs_list[i]:
		a = pairs_list[i].split('  ')
		pairs_gold.append(a[1])
	elif pairs_list[i][0] == '/':
		a = pairs_list[i].split('  ')
		if len(pairs_gold) > len(pairs_silver):
			b = len(pairs_gold)
			pairs_gold[b-1] = pairs_gold[b-1]+' '+a[0]
			pairs_silver.append(a[1])
		elif len(pairs_silver) > len(pairs_bronze):
			b = len(pairs_silver)
			pairs_silver[b-1] = pairs_silver[b-1]+' '+a[0]
			if len(a) == 2:
				pairs_bronze.append(a[1])
		else:
			b = len(pairs_bronze)
			pairs_bronze[b-1] = pairs_bronze[b-1]+' '+a[0]
	elif 'Debbi' in pairs_list[i]:
		a = len(pairs_silver)
		pairs_silver[a-1] = pairs_silver[a-1]+' , '+pairs_list[i]
	elif 'Jamie' in pairs_list[i]:
		pairs_bronze.append(pairs_list[i])


for_bronze = ''
for i in range(len(pairs_silver)):
	if 'Shen Xue' in pairs_silver[i]:
		for_bronze = pairs_silver[i]
		pairs_silver[i] = ''


for_gold = ''
for i in range(len(pairs_bronze)):
	if 'Jamie Sal' in pairs_bronze[i]:
		for_gold = pairs_bronze[i]
		pairs_bronze[i] = for_bronze

for i in range(len(pairs_gold)):
	if 'Elena Berezhnaya' in pairs_gold[i]:
		l = len(pairs_gold[i])
		pairs_gold[i] = pairs_gold[i][:l-16]+' , '+for_gold

for j in [pairs_gold, pairs_silver, pairs_bronze]:
	for i in range(len(j)):
		if ',' in j[i]:
			a = j[i].find('(')
			j[i] = j[i][:a-1] + j[i][a+5:]
			b = j[i].find('(')
			j[i] = j[i][:b-1]
		else:
			a = j[i].find('(')
			j[i] = j[i][:a-1]




# ice dancing medalists

ice_list = ice_dancing.split('\n')

ice_olympic_year = []
ice_gold = []
ice_silver = []
ice_bronze = []


for i in range(len(ice_list)):
	if ice_list[i][0] == '1' or ice_list[i][0] == '2':
		year = ice_list[i].split(' ')
		ice_olympic_year.append(year[0])
	elif 'details' in ice_list[i]:
		a = ice_list[i].split('  ')
		ice_gold.append(a[1])
	else:
		a = ice_list[i].split('  ')
		if len(ice_gold) > len(ice_silver):
			b = len(ice_gold)
			ice_gold[b-1] = ice_gold[b-1]+' '+a[0]
			ice_silver.append(a[1])
		elif len(ice_silver) > len(ice_bronze):
			b = len(ice_silver)
			ice_silver[b-1] = ice_silver[b-1]+' '+a[0]
			if len(a) == 2:
				ice_bronze.append(a[1])
		else:
			b = len(ice_bronze)
			ice_bronze[b-1] = ice_bronze[b-1]+' '+a[0]



for j in [ice_gold, ice_silver, ice_bronze]:
	for i in range(len(j)):
		a = j[i].find('(')
		j[i] = j[i][:a-1]



# refine pairs and ice dancing

pairs_gold_individual = []
pairs_silver_individual = []
pairs_bronze_individual = []
ice_gold_individual = []
ice_silver_individual = []
ice_bronze_individual = []

pairs_gold_individual_olympic_year = []
pairs_silver_individual_olympic_year = [] # No year which corresponds to skater ''
pairs_bronze_and_ice_individual_olympic_year = []

individual = []
pairs_ice_list = [pairs_gold, pairs_silver, pairs_bronze, ice_gold, ice_silver, ice_bronze]
pairs_ice_individual_list = [pairs_gold_individual, pairs_silver_individual, pairs_bronze_individual, ice_gold_individual, ice_silver_individual, ice_bronze_individual]

for j in pairs_ice_list:
	for i in range(len(j)):
		if ',' in j[i]:
			a = j[i].split(' , ')
			b1 = a[0].split(' / ')
			b2 = a[1].split(' / ')
			for k in [b1[0],b1[1],b2[0],b2[1]]:
				individual.append(k)
		elif '/' in j[i]:
			a = j[i].split(' / ')
			individual.append(a[0])
			individual.append(a[1])

	for k in range(6):
		if j == pairs_ice_list[k]:
			pairs_ice_individual_list[k] = individual



for i in range(len(pairs_gold)):
	if ',' in pairs_gold[i]:
		for j in range(4):
			pairs_gold_individual_olympic_year.append(pairs_olympic_year[i])
	elif '/' in pairs_gold[i]:
		for j in range(2):
			pairs_gold_individual_olympic_year.append(pairs_olympic_year[i])
	

for i in range(len(pairs_silver)):
	if '/' in pairs_gold[i]:
		for j in range(2):
			pairs_silver_individual_olympic_year.append(pairs_olympic_year[i])


for i in range(len(pairs_olympic_year)):
	pairs_bronze_and_ice_individual_olympic_year.append(pairs_olympic_year[i])
	pairs_bronze_and_ice_individual_olympic_year.append(pairs_olympic_year[i])





# Birth and Naton

men_gold_birth = []
men_silver_birth = []
men_bronze_birth = []
ladies_gold_birth = []
ladies_silver_birth = []
ladies_bronze_birth = []
pairs_gold_birth = []
pairs_silver_birth = []
pairs_bronze_birth = []
ice_gold_birth = []
ice_silver_birth = []
ice_bronze_birth = []

men_gold_country = []
men_silver_country = []
men_bronze_country = []
ladies_gold_country = []
ladies_silver_country = []
ladies_bronze_country = []
pairs_gold_country = []
pairs_silver_country = []
pairs_bronze_country = []
ice_gold_country = []
ice_silver_country = []
ice_bronze_country = []

listset = [men_gold, men_silver, men_bronze, ladies_gold, ladies_silver, ladies_bronze, pairs_gold_individual, pairs_silver_individual, pairs_bronze_individual, ice_gold_individual, ice_silver_individual, ice_bronze_individual]
birth = [men_gold_birth, men_silver_birth, men_bronze_birth, ladies_gold_birth, ladies_silver_birth, ladies_bronze_birth, pairs_gold_birth, pairs_silver_birth, pairs_bronze_birth]
country = [men_gold_country, men_silver_country, men_bronze_country, ladies_gold_country, ladies_silver_country, ladies_bronze_country, pairs_gold_country, pairs_silver_country, pairs_bronze_country, ice_gold_country, ice_silver_country, ice_bronze_country]


for l in listset:
	templist1 = []
	templist2 = []
	for i in range(len(l)):
		men_gold_url = URL('https://en.wikipedia.org/wiki/'+l[i]).download()
		men_gold_text = plaintext(men_gold_url)

		if men_gold_text.find('Born')==-1:
			men_gold_url = URL('https://en.wikipedia.org/wiki/'+l[i]+'_(figure_skater)').download()
			men_gold_text = plaintext(men_gold_url)
		
		men_gold_text_list = men_gold_text.split('\n')

		for j in range(len(men_gold_text_list)):
			if men_gold_text_list[j]=='Born':
				templist1.append(men_gold_text_list[j+1])

			if men_gold_text_list[j]=='Country represented':
				templist2.append(men_gold_text_list[j+1])

		for k in range(12):
			if l == listset[k]:
				birth[k] = templist1
				country[k] = templist2




			

# calculations - Age to get medal / Average age / Age graph / Nation graph / oldest,youngest / most nation

men_gold_age =[]
men_silver_age =[]
men_bronze_age =[]
ladies_gold_age =[]
ladies_silver_age =[]
ladies_bronze_age =[]
pairs_gold_age =[]
pairs_silver_age =[]
pairs_bronze_age =[]
ice_gold_age =[]
ice_silver_age =[]
ice_bronze_age =[]


olympic_year = [men_olympic_year, men_olympic_year, men_olympic_year, ladies_olympic_year, ladies_olympic_year, ladies_olympic_year, pairs_gold_individual_olympic_year, pairs_silver_individual_olympic_year, pairs_bronze_and_ice_individual_olympic_year, pairs_bronze_and_ice_individual_olympic_year, pairs_bronze_and_ice_individual_olympic_year, pairs_bronze_and_ice_individual_olympic_year]
birth = [men_gold_birth, men_silver_birth, men_bronze_birth, ladies_gold_birth, ladies_silver_birth, ladies_bronze_birth, pairs_gold_birth, pairs_silver_birth, pairs_bronze_birth]
age = [men_gold_age, men_silver_age, men_bronze_age, ladies_gold_age, ladies_silver_age, ladies_bronze_age, pairs_gold_age, pairs_silver_age, pairs_bronze_age, ice_gold_age, ice_silver_age, ice_bronze_age]


for j in birth:
	for i in range(len(j)):
		for k in range(len(birth)):
			if j==birth[k]:
				medal_age = str(olympic_year[k][i]) - str(j[i][1:5])
				age[k].append(medal_age)
print olympic_year
print age

"""
average_gold_age = sum(age_got_gold_medal)/len(age_got_gold_medal)

youngest_gold_age = min(age_got_gold_medal)
for i in range(len(men_gold)):
	if age_got_gold_medal[i] == min(age_got_gold_medal):
		youngest_gold_name = men_gold[i]
		
oldest_gold_age = max(age_got_gold_medal)
for i in range(len(men_gold)):
	if age_got_gold_medal[i] == max(age_got_gold_medal):
		oldest_gold_name = men_gold[i]

def men_gold_age_graph():
	for i in range(len(age_got_gold_medal)):
		print olympic_year[i] + ' ' + '*'*int(age_got_gold_medal[i])
	print '    5    10   15   20   25   30'


number = [1,2,3,4,5]


while True:
	answer = raw_input('What do you want to know in figure skating? (put the number)\n1) men single / 2) ladies single / 3) pairs / 4) ice dancing / 5) end\n')
	if answer == 1:
		answer = raw_input('What do you want to know in men single medalists?\n1) gold / 2) silver / 3) bronze')
		if answer == 1:
			answer = raw_input('What do you want to know in men single gold medalists?\n1) average age / 2) youngest medalist / 3) oldest medalist / 4) most numbers of country gold medalists in / 5) age graph / 6) country graph')
			if answer == 1:
				
		if answer == 2:
		if answer == 3:
	elif answer == 2:
		print youngest_gold_name + ', ' + str(youngest_gold_age)
	elif answer == 3:
		print oldest_gold_name + ', ' + str(oldest_gold_age)
	elif answer == 4:
		men_gold_age_graph()
	elif answer == 5:
		print 'Thank you'
		break

"""