import mcCabe
import ratioTest
import cloc
import lcsec
import os
import sys
import csv


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

def complexity(path):
	complexityMcCabe(path)
	moyenneMcCabe = 0 
	for value in tabTotalFile:
		moyenneMcCabe += value[-1]
	moyenneMcCabe = moyenneMcCabe/len(tabTotalFile)

	with open('mcCabe.csv', 'w', newline='') as myfile:
	     wr = csv.writer(myfile, delimiter=',')
	     wr.writerows(tabTotalFile)
	print(f"en moyenne les fichiers ont une complexity de  : {round(moyenneMcCabe,4)}" )
	


def couple(path):
	lcsec.result(path,"mcCabe.csv")
complexity(sys.argv[1])
documentation(sys.argv[1])
couple(sys.argv[1])
