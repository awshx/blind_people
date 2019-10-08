#!/usr/bin/python

# importation des librairies
import pandas as pd
import xlsxwriter as xls

def creationDataframe():
	convertion = pd.read_excel('logo_informations.xlsx', sheetname='Sheet1')	

	return convertion

def convertion_csv(convertion):
	print(convertion)
	convertion.to_csv("./logo_informations.csv", sep='\t', encoding='utf-8', index=False)

def main():

	convertion = creationDataframe()
	convertion_csv(convertion)

if __name__ == "__main__":
	main()
