my_list = [12, 45, 78, 6, 23]

# Her elemana erişmek için for döngüsü kullanma
for item in my_list:
    print(item)  # Her elemanı yazdır

# Eğer indeksleri de kullanmak isterseniz, enumerate() fonksiyonunu kullanabilirsiniz
for index, item in enumerate(my_list):
    print(f"Index: {index}, Value: {item}")
