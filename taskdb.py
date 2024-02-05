	import sqlite3
 
# Veritabanı bağlantısı
connection = sqlite3.connect("TESTDB.db")
cursor = connection.cursor()
 
class Database:
    @staticmethod
    def getColumnNames():
        cursor.execute("PRAGMA table_info(STUDENTS)")
        columns = cursor.fetchall()
        return columns
 
    @staticmethod
    def updateStudent(columnName, newValue, where):
        cursor.execute("UPDATE STUDENTS SET "+columnName+" = ? WHERE studentId = ?;", (newValue, where,))
        connection.commit()
        print("Veri güncellendi.")
        print(Database.getAllStudents())
 
    @staticmethod
    def insertStudent(name, surname):
        cursor.execute("INSERT INTO STUDENTS (studentName, studentSurname) VALUES (?, ?);", (name, surname,))
        connection.commit()
        print("Öğrenci eklendi.")
        print(Database.getAllStudents())
 
    @staticmethod
    def deleteStudent(studentId):
        cursor.execute("DELETE FROM STUDENTS WHERE studentId = ?;", (studentId,))
        connection.commit()
        print("Öğrenci silindi.")
        print(Database.getAllStudents())
 
    @staticmethod
    def searchStudent(value):
        value = '%' + value + '%'
        cursor.execute("SELECT * FROM STUDENTS WHERE studentName LIKE ? OR studentSurname LIKE ?;", (value, value,))
        students = cursor.fetchall()
        return students
 
    @staticmethod
    def getAllStudents():
        cursor.execute("SELECT * FROM STUDENTS ORDER BY studentName ASC;")
        students = cursor.fetchall()
        return students
 
# Sonsuz döngü ile kullanıcı arayüzü oluşturma
while True:
    print("\nMerhaba, öğrenci veri tabanında ne işlem yapmak istersiniz?")
    print("[1] Öğrenci Ara")
    print("[2] Öğrenci Güncelleştir")
    print("[3] Öğrenci Ekle")
    print("[4] Öğrenci Sil")
 
    choice = input("Seçiminiz: ")
 
    if choice == "1":
        value = input("Aramak istediğiniz öğrencinin adını veya soyadını girin: ")
        print(Database.searchStudent(value))
 
    elif choice == "2":
        student_id = input("Güncellemek istediğiniz öğrencinin ID'sini girin: ")
        column_choice = input("Hangi bilgiyi güncellemek istiyorsunuz? [1] Ad [2] Soyad: ")
 
        if column_choice == "1":
            new_name = input("Öğrencinin yeni adını girin: ")
            Database.updateStudent("studentName", new_name, student_id)
        elif column_choice == "2":
            new_surname = input("Öğrencinin yeni soyadını girin: ")
            Database.updateStudent("studentSurname", new_surname, student_id)
        else:
            print("Geçersiz seçim.")
 
    elif choice == "3":
        name = input("Öğrencinin adını girin: ")
        surname = input("Öğrencinin soyadını girin: ")
        Database.insertStudent(name, surname)
 
    elif choice == "4":
        student_id = input("Silmek istediğiniz öğrencinin ID'sini girin: ")
        Database.deleteStudent(student_id)
 
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
