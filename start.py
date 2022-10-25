import mcCabe
import ratioTest
import cloc
import lcsec
import os
import sys
import csv
import math


ratioTest.result(sys.argv[1])
tabTotalFile = []
tabCloc = []

def complexityMcCabe(path):
	for file in os.listdir(path):
		result = os.path.join(path, file)
		if(file.endswith('.java')):
			tabTotalFile.append([result,file.replace(".java",""),mcCabe.result(result)])
			#moyenneMcCabe += mcCabe.result(result)
			#print(mcCabe.result(file))

		elif os.path.isdir(result) :
			complexityMcCabe(result)

	#return tabTotalFile

def documentationCloc(path):
	for file in os.listdir(path):
		result = os.path.join(path, file)
		if(file.endswith('.java')):
			tabCloc.append(cloc.result(result))
			#moyenneMcCabe += mcCabe.result(result)
			#print(mcCabe.result(file))

		elif os.path.isdir(result) :
			documentationCloc(result)



def documentation(path):
	documentationCloc(path)
	moyenneCloc = 0 
	for value in tabCloc:
		moyenneCloc += value
	moyenneCloc = moyenneCloc/len(tabCloc)
	print(f"en moyenne les fichiers ont une densité de commentaire de  : {round(moyenneCloc,4)}" )

def CBOSort(tab):
	return int(tab[-1])

def complexitySort(tab): 


	return int(tab[-3])

def complexity(path):
	complexityMcCabe(path)
	#q1(tabTotalFile)





def q1 (tabTotalFile):
	tab1 = sorted(tabTotalFile,key=CBOSort, reverse=True)
	threshold10 = math.ceil(10/100 *len(tab1))
	threshold30 = math.ceil(30/100 *len(tab1))
	#tab30 = []
	threshold60 = math.ceil(60/100 *len(tab1))
	#tab60 = []
	threshold90 = math.ceil(90/100 *len(tab1))
	#tab90 = []


	for value in tab1:
		value.append(cloc.result(value[0]))


	moyenneDensite10 = 0
	moyenneDensite30 = 0
	moyenneDensite60 = 0
	moyenneDensite90 = 0
	moyenneMcCabe = 0 

	for i in range(threshold90):
		if(i < threshold10):
			moyenneDensite10 += tab1[i][-1]
		if(i < threshold30):
			moyenneDensite30 += tab1[i][-1]
		if(i < threshold60):
			moyenneDensite60 += tab1[i][-1]
		moyenneDensite90 += tab1[i][-1]

	moyenneDensite10 = moyenneDensite10/threshold10
	moyenneDensite30 = moyenneDensite30/threshold30
	moyenneDensite60 = moyenneDensite60/threshold60
	moyenneDensite90 = moyenneDensite90/threshold90

	for value in tab1:
		moyenneMcCabe += value[-2]
	moyenneMcCabe = moyenneMcCabe/len(tab1)

	with open('mcCabe.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1)

	with open('mcCabe10.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold10])

	with open('mcCabe30.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold30])

	with open('mcCabe60.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold60])

	with open('mcCabe90.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold90])

	print(f"en moyenne les fichiers ont une complexity de  : {round(moyenneMcCabe,4)}" )
	print(f"à un seuil de 10% les fichiers ont en moyenne une densité de  : {round(moyenneDensite10,4)}" )
	print(f"à un seuil de 30% les fichiers ont en moyenne une densité de  : {round(moyenneDensite30,4)}" )
	print(f"à un seuil  60% les fichiers ont en moyenne une densité de  : {round(moyenneDensite60,4)}" )
	print(f"à un seuil  90% les fichiers ont en moyenne une densité de  : {round(moyenneDensite90,4)}" )



def q2():
	tab = couple(sys.argv[1])
	threshold10 = math.ceil(10/100 *len(tab))
	threshold15 = math.ceil(15/100 *len(tab))




	tab1 = sorted(tab,key=CBOSort,reverse=True)
	print("tab1 ok")
	tab2 = sorted(tab,key=complexitySort,reverse=True)
	print("tab2 ok")

	temptab1 = []
	temptab2 = []
	moyenne10Complexity = 0 
	moyenne15Complexity = 0
	moyenne10CBO = 0 
	moyenne15CBO = 0

	with open('CBO10.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold10])

	with open('CBO15.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab1[:threshold15])

	with open('complexity10.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab2[:threshold10])

	with open('complexity15.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tab2[:threshold15])


	for i in range(threshold10):
		for j in range(threshold10):
			if(tab1[i][0] == tab2[j][0]):
				temptab1.append(tab1[i])
				moyenne10Complexity += int(float(tab1[i][-2]))
				moyenne10CBO += int(float(tab1[i][-1]))
				break
	for i in range(threshold15):
		for j in range(threshold15):
			if(tab1[i][0] == tab2[j][0]):
				temptab2.append(tab1[i])
				moyenne15Complexity += int(float(tab1[i][-2]))
				moyenne15CBO += int(float(tab1[i][-1]))
				break
	
	
		

	moyenne10Complexity = moyenne10Complexity/len(temptab1)
	moyenne15Complexity = moyenne15Complexity/len(temptab2)
	moyenne10CBO = moyenne10CBO/len(temptab1)
	moyenne15CBO = moyenne15CBO/len(temptab2)

	with open('CBO_WMC10.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(temptab1)

	with open('CBO_WMC15.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(temptab2)

	#print(f"en moyenne les fichiers ont une complexity de  : {round(moyenneMcCabe,4)}" )
	print(f"à un seuil de 10% les fichiers ont une complexite de  : {round(moyenne10Complexity,4)}" )
	print(f"à un seuil de 15% les fichiers ont une complexite de  : {round(moyenne15Complexity,4)}" )
	print(f"à un seuil  10% les fichiers ont un CBO de  : {round(moyenne10CBO,4)}" )
	print(f"à un seuil  15% les fichiers ont un CBO de  : {round(moyenne15CBO,4)}" )

	 		


def couple(path):
	result = lcsec.result(path,"mcCabe.csv")
	print("ok")
	return result


print("complexity")
complexity(sys.argv[1])


print("documentation")
documentation(sys.argv[1])


print("q1")
q1(tabTotalFile)


print("q2")
q2()
