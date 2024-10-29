string = "hello word"
print (string)
# Mendefinisikan string
greeting = "Hello, World!"

# Mengakses karakter dalam string
first_character = greeting[0]
print("Karakter pertama:", first_character)

# Menghitung panjang string
length = len(greeting)
print("Panjang string:", length)

# Mengubah huruf menjadi huruf kecil dan besar
lowercase = greeting.lower()
uppercase = greeting.upper()
print("Huruf kecil:", lowercase)
print("Huruf besar:", uppercase)

# Mengganti substring
new_greeting = greeting.replace("World", "Python")
print("Greeting baru:", new_greeting)

# Memecah string menjadi list
words = greeting.split(", ")
print("Kata-kata dalam list:", words)

# Menggabungkan list menjadi string
joined_string = " - ".join(words)
print("String yang digabungkan:", joined_string)
