name = input(" имя: ");
print();

surename = input(" фамилия: ");
print();

adress = input(" адрес: ");
print();

whereDoYouStudyOrWork = input(" место работы или учёбы: ");
print();

phoneNumber = input(" номер телефона: ");
print("\n");


information = "имя: "+str(name)		+"\n\nфамилия: "+str(surename)		+"\n\nадрес: "+str(adress)		+"\n\nместо работы или учёбы: "+str(whereDoYouStudyOrWork)		+"\n\nномер телефона: "+str(phoneNumber);

print();
print();

print("		нажмите Enter чтобы сохранить в документе.");
input();
my_filename=str(name + " " + surename);
data=information;
fext2='txt'
print(my_filename)
with open(my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:
     print(data, file=fp, sep="\n")
     fp.close()# закрытие файла

