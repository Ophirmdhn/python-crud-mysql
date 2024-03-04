import mysql.connector as mysql

host = "localhost"
user = "root"
password = ""
database = "db_crud"

# Koneksi database
db = mysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = db.cursor()  # Untuk mengeksekusi sql

# cursor.execute("CREATE DATABASE db_crud")  # Membuat database baru

# cursor.execute("DROP DATABASE db_crud")  # Menghapus database

# cursor.execute("SHOW DATABASES")  # Menampilkan semua database yang ada

# db.database = "db_crud"

# Membuat table
# cursor.execute("""
#     CREATE TABLE tb_mahasiswa(
#     id INT(3) NOT NULL AUTO_INCREMENT,
#     nama VARCHAR(50) NOT NULL,
#     nim VARCHAR(10) NOT NULL,
#     PRIMARY KEY (id)
#     );
# """)

# cursor.execute("DROP TABLE tb_mahasiswa")  # Menghapus table

# db.commit()  # Menjalankan query/mengupdate data

# cursor.execute("DESC tb_mahasiswa")  # Menampilkan deskripsi tabel
# print(cursor.fetchall())

cursor.execute("SHOW TABLES")  # Menampilkan table yang ada pada database
print(cursor.fetchall())  # Menampilkan data di terminal

# Menambahkan data ke dalam tabel
# cursor.execute("""
#     INSERT INTO tb_mahasiswa (nama,nim)
#     VALUES ('Sumbul', 11223344)
# """)
# db.commit()

# Mengupdate data pada tabel
# cursor.execute("""
#     UPDATE tb_mahasiswa
#     SET nama = 'Ahmad', nim = '12341234'
#     WHERE id = 4
# """)
# db.commit()

# Menghapus data pada tabel
# cursor.execute("""
#     DELETE FROM tb_mahasiswa
#     WHERE id = 2
# """)
# db.commit()


cursor.execute("SELECT * FROM tb_mahasiswa")  # Menampilkan semua data yang ada pada tb_mahasiswa
data = cursor.fetchall()
for i in data:
    print(i)
