import mysql.connector as mysql

host = "localhost"
user = "root"
password = ""
database = "db_crud"

db = mysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


def show_menu():
    print("\n===== APLIKASI DATA MAHASISWA =====")
    print("1. Tambahkan Data")
    print("2. Tampilkan Data")
    print("3. Edit Data")
    print("4. Hapus Data")
    print("0. Keluar")
    print("===================================")

    menu = int(input("Pilih Menu : "))

    if menu == 1:
        insert_data()
    elif menu == 2:
        show_data()
    elif menu == 3:
        update_data()
    elif menu == 4:
        delete_data()
    elif menu == 0:
        exit()
    else:
        print("\nMenu tidak tersedia!")


def insert_data():
    name = input("Masukan nama : ")
    nim = input("Masukan NIM : ")

    cursor = db.cursor()
    query = "INSERT INTO tb_mahasiswa (nama, nim) VALUES (%s, %s)"
    value = (name, nim)
    cursor.execute(query, value)
    db.commit()
    print(f"\n{cursor.rowcount} Data berhasil disimpan")


def show_data():
    cursor = db.cursor()
    query = "SELECT * FROM tb_mahasiswa"
    cursor.execute(query)
    result = cursor.fetchall()

    if cursor.rowcount < 0:
        print("\nTidak ada data!")
    else:
        print("\n======== DATA MAHASISWA ========")
        for data in result:
            print(data)


def update_data():
    cursor = db.cursor()
    show_data()
    student_id = int(input("\nPilih id mahasiswa yang ingin diubah : "))
    name = input("Masukan nama baru : ")
    nim = input("Masukan NIM baru : ")

    query = "UPDATE tb_mahasiswa SET nama = %s, nim = %s WHERE id = %s"
    value = (name, nim, student_id)
    cursor.execute(query, value)
    db.commit()
    print(f"\nMahasiswa dengan id {student_id} berhasil diubah")


def delete_data():
    cursor = db.cursor()
    show_data()
    student_id = int(input("\nPilih id mahasiswa yang ingin dihapus : "))

    query = "DELETE FROM tb_mahasiswa WHERE id = %s"
    value = (student_id,)
    cursor.execute(query, value)
    db.commit()
    print(f"\nMahasiswa dengan id {student_id} berhasil dihapus")


if __name__ == "__main__":
    while True:
        show_menu()
