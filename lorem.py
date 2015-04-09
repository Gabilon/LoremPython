import random

#Finds words1.txt and reads ('r')
#Splits words into items in a list ('words' becomes a list)
words = open('words1.txt','r')
words = words.read().split()

#Ask user how many parragraphs
ask_par = raw_input("Enter how many paragraphs: ")

#parses the string value into a int
#if not possible it will show an error
try:
	value  = int(ask_par)
except:
	print("\nError! Must enter a integer\n")

#Variables
max_sentences = 20
min_sentences = 8
output_str = ""

#Asking if filler will be added
ask_Coqui = raw_input("Coqui ipsum dolor amet? [y = yes,n = no]: ")
ask_filler = raw_input("Add filler? [y = yes, n = no]: ")
print "\n"
if ask_Coqui == "y" or ask_Coqui == "Y":
	output_str += "Coqui ipsum dolor amet"
if ask_filler == "y" or ask_filler == "Y":
	filler = open('mono.txt','r')
	filler = filler.read().split()
	for x in filler:
		words.append(x)


def ipsum(ask_Coqui,value,output_str):
	#Array and Counter 
	array_paragraphs = []
	n = 0
	while n < value:
		for x in range(0,random.randint(4,14)): #Sentences
			if x == 0:
				output_str = output_str.rstrip(" ")
			if output_str == "Coqui ipsum dolor amet":
				output_str += " "
			for y in range(0, random.randint(min_sentences,max_sentences)): #Words
				if output_str == "Coqui ipsum dolor amet ":
					output_str = add_Coqui(output_str)
				if y == 0:
					output_str += random.choice(words).title()
				output_str += " " + random.choice(words).lower()
				if y == 10:
					output_str += ","
			output_str = output_str.rstrip(",")
			output_str += "." + " "
		array_paragraphs.append(output_str)
		output_str = ""
		n += 1

	return array_paragraphs

def add_Coqui(output_str):
	for y in range(0, random.randint(min_sentences, max_sentences)):
		if y == 0:
			output_str = output_str.rstrip(" ")
		output_str += " " + random.choice(words).lower()
		if y == 10:
			output_str += ","
	output_str = output_str.rstrip(",")
	output_str += ". "
	return output_str

complete = ipsum(ask_Coqui,value,output_str) #returns array/list

#prints out the list.  
for x in complete:
	print x
	print ""

