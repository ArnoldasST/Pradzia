
list = []
x = 1
for i in range(5):
    word = input("Iveskite Zodi: ")
    list.append(word)
    list.append(x)
    x += 1
    list.append(len(word))
print(list)
print()
'''
'''
list2 = []
number_of_words_selected_by_user = int(input("Kiek zodziu norite ivesti?: "))
i = 0
x = 1
while i < number_of_words_selected_by_user:
    word = input("Iveskite Zodi: ")
    list2.append(word)
    list2.append(x)
    x += 1
    list2.append(len(word))
    i += 1
print(list2)