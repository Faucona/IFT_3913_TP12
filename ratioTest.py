import csv
import math
import os
import sys
import lcsec
def ratioTest(path):
	for file in os.listdir(path):

		result = os.path.join(path, file)
		if(file.endswith('.java')):
			tabTotal.append(file)

			if ("Test" in file):
				for i in range(len(tabValue)):
					if(file.replace("Test","") in tabValue[i][0]):
						tabValue[i].append(round(os.path.getsize(os.path.join(path, file))/int(tabValue[i][1]),4))
						tabTestValue.append(tabValue.pop(i))
						break

			else :
				#print(file)
				#varf = file.replace('.java','')
				#print(varf)
				strResult = f"{result}, {os.path.getsize(os.path.join(path, file))}"
				tabResult = strResult.split(',')
				tabResult.append(file.replace('.java','')) 
				tabValue.append(tabResult)
				

		elif os.path.isdir(result) :
			ratioTest(result)

	return tabTestValue

def start(string):
	if (not isinstance(string, str)):
		return f"{string}"
	else:
		return string

tabValue = []
tabTestValue = []
tabTotal = []
def result(string):

	tab = ratioTest(start(string))

	moyenne = 0
	ecartType = 0
	for value in tabTestValue : 
		#print(value)
		moyenne += value[-1]

	moyenne = round(moyenne/len(tabTestValue),4)

	for value in tabTestValue : 
		ecartType += (moyenne - value[-1])**2

	ecartType = math.sqrt(ecartType/len(tabTestValue))


	with open('classeTester.csv', 'w', newline='') as myfile:
	    wr = csv.writer(myfile, delimiter=',')
	    wr.writerows(tab)

	with open('classeNonTester.csv', 'w', newline='') as myfile:
	    wr = csv.writer(myfile, delimiter=',')
	    wr.writerows(tabValue)

	#for value in tabValue :
	
	tab3 = lcsec.result(string,'classeNonTester.csv')

	moyenne2 = 0
	#ecartType = 0
	for value in tab3 : 
		moyenne2 += value[-1]

	moyenne2 = round(moyenne2/len(tab3),4)
	
	with open('classeNonTesterCBO.csv', 'w', newline='') as myfile:
	    wr = csv.writer(myfile, delimiter=',')
	    wr.writerows(tab3)


	print(f"nombre de classe total : {len(tabTotal)}")
	print(f"nombre de classe tester : {len(tabTestValue)}")
	print(f"nombre de classe non tester : {len(tabValue)}")
	print(f"nombre de classeTest non associé à une classe repertorié : {len(tabTotal) - len(tabValue) - len(tabTestValue)*2}")
	print(f"pourcentage de classe non tester : {round(len(tabValue)/len(tabTotal),4)*100}%" )
	print(f"en moyenne les fichier non tester on un CBO de : {round(moyenne2,4)}" )
	print(f"en moyenne la taille fichier d'un fichier test est : {moyenne*100}% de son fichier tester" )
	print(f"ecart type de la taille d'un fichier test est : {round(ecartType,4)}" )

if __name__ == "__main__":
	result(sys.argv[1]) 
	


