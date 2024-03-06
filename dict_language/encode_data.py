with open("words.txt", "r") as f:
	dict_str = f.read()

my_dict={}
value = 0;

for item in dict_str.split("\n"):
	my_dict[item] = value
	value += 1


#print(my_dict['mom'])
i = input("Please enter the sentence: ")
i = i.lower()
i = i.split(" ")

sentence=""
for item in i:
	sentence = sentence + "-" + str(my_dict[item])


print(sentence)

