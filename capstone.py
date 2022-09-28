dataSiswa = {}

kode=1

def tambah():
    sub_menu = 0
    while(sub_menu != 2):
        print("--------------------------------------")
        print("========  Tambah Data Siswa  =========")
        print("--------------------------------------")
        print("    [1] Tambah Data Nilai Siswa       ")
        print("    [2] Kembali Ke Menu Utama         ")
        print("--------------------------------------")
        sub_menu = int(input('Silahkan Pilih Sub Menu Create Data [1-2] : '))
        
        if sub_menu == 1:
            
            key = input("Masukkan NIM : ")
            if key in dataSiswa:
                print("Maaf NIM telah terdaftar!")
            else:
                nama = input("Masukkan Nama : ")
                kelas = input("Masukkan Kelas : ")
                mata_kuliah = input("Masukkan Mata Kuliah : ")
                nilai = input("Masukkan Nilai : ")
                
                temp = {"nama":nama,"kelas":kelas,"mata_kuliah":mata_kuliah,"nilai":nilai} #Bikin dict sementara
                
                yakin='A'
                while (yakin != 'N' or yakin !='n'):
                    yakin = input("Apakah Data Akan Disimpan? (Y/N) : ")
                    if(yakin=='y' or yakin=='Y'):
                        dataSiswa.update({key : temp}) #disimpen di dictionary format {1:{nim:1212,nama:yaya,gender:laki,kota:bdg}, 2:{} dst...}
                        print("Data Tersimpan!")
                        break

def lihat():
    sub_menu = 0
    while(sub_menu != 3):
        print ("--------------------------------------")
        print ("++++++++  Report Data Siswa  +++++++++")
        print ("--------------------------------------")
        print ("      [1] Report Seluruh Data         ")
        print ("      [2] Report Data Tertentu        ")
        print ("      [3] Kembali Ke Menu Utama       ")
        print ("--------------------------------------")
        sub_menu = int(input('Silahkan Pilih Sub Menu Read Data [1-3] : '))
        
        if sub_menu==1:
            if(len(dataSiswa)>0):
                i = 0
                for nim, siswa in dataSiswa.items():
                    print("%d. NIM : %s, Nama : %s, Kelas : %s, mata_kuliah : %s, nilai : %s" % (i+1,nim,siswa['nama'],siswa['kelas'],siswa['mata_kuliah'],siswa['nilai']))
            else:
                print("Tidak Ada Data Siswa")
        elif sub_menu==2:
            nim = input('Masukan NIM  :')
            if nim in dataSiswa:
                print("Data Siswa Dengan NIM "+nim)
                print("1. NIM : %s, Nama : %s, Kelas : %s, mata_kuliah : %s, nilai : %s" % (nim,dataSiswa[nim]['nama'],dataSiswa[nim]['kelas'],dataSiswa[nim]['mata_kuliah'],dataSiswa[nim]['nilai']))
            else:
                print("Tidak Ada Data Siswa")

def update():
    sub_menu = 0
    while(sub_menu != 2):
        print ("--------------------------------------")
        print ("+++++++  Mengubah Data Siswa  ++++++++")
        print ("--------------------------------------")
        print ("      [1] Ubah Data Nilai Siswa       ")
        print ("      [2] Kembali Ke Menu Utama       ")
        print ("--------------------------------------")
        sub_menu = int(input('Silahkan Pilih Sub Menu Update Data [1-2] : '))
        
        if sub_menu == 1:
            
            key = input("Masukkan NIM : ")
            if key in dataSiswa:
                print("Data Siswa Dengan NIM "+key)
                print("1. NIM : %s, Nama : %s, Kelas : %s, mata_kuliah : %s, nilai : %s" % (key,dataSiswa[key]["nama"],dataSiswa[key]["kelas"],dataSiswa[key]["mata_kuliah"],dataSiswa[key]["nilai"] ))
                
                yakin='A'
                while (yakin != 'N' or yakin !='n'):
                    yakin = input("Tekan Y jika ingin lanjut Update, tekan N jika ingin batalkan? (Y/N) : ")
                    if(yakin=='y' or yakin=='Y'):
                        col = input("Masukan kolom/keterangan yang ingin diedit:")
                        if col in dataSiswa[key]:
                            new_value = input("Masukan %s Baru : "%col)
                            y_up='A'
                            while (y_up != 'N' or y_up !='n'):
                                y_up = input("Apakah Data akan diupdate? (Y/N) : ")
                                if(y_up=='y' or y_up=='Y'):
                                    dataSiswa[key][col] = new_value
                                    print("Data Berhasil Di Update!")
                                    break
                                elif(y_up=='n' or y_up=="N"):
                                    print("Data Gagal di Update!")
                        else:
                            print("Maaf Kolom/Keterangan tidak ada!")
                            
                        break
                            
                    elif(yakin=='N' or yakin !='n'):
                        print("Data Tidak Jadi di Update!")                
            else:
                print("Maaf Data dengan NIM %s tidak terdaftar!"%(key))
                

def delete():
    sub_menu = 0
    while(sub_menu != 2):
        print ("--------------------------------------")
        print ("+++++++  Menghapus Data Siswa  +++++++")
        print ("--------------------------------------")
        print ("      [1] Hapus Data Nilai Siswa      ")
        print ("      [2] Kembali Ke Menu Utama       ")
        print ("--------------------------------------")
        sub_menu = int(input('Silahkan Pilih Sub Menu Update Data [1-2] : '))
        
        if sub_menu == 1:
            key = input("Masukkan NIM : ")
            if key in dataSiswa:
                yakin='A'
                while (yakin != 'N' or yakin !='n'):
                    yakin = input("Apakah Data yakin dihapus? (Y/N) : ")
                    if(yakin=='y' or yakin=='Y'):
                        del dataSiswa[key]
                        print("Data Terhapus!")
                        break
                    elif(yakin=='n' or yakin=="N"):
                        print("Data Gagal dihapus!")
            else:
                print("Data dengan NIM %s tidak ditemukan!"%(key))
            

while kode !=5 :
    print ("--------------------------------------")
    print ("====       Data Record Siswa      ====")
    print ("--------------------------------------")
    print ("    [1] Report Data Nilai Siswa       ")
    print ("    [2] Menambahkan Data Nilai Siswa  ")
    print ("    [3] Mengubah Data Nilai Siswa     ")
    print ("    [4] Menghapus Data Nilai Siswa    ")
    print ("    [5] Exit                          ")
    print ("--------------------------------------")
    kode = int(input('Silahkan Pilih Main Menu [1-5] : '))

    if kode == 1:
        lihat()
    elif kode ==2:
        tambah()
    elif kode == 3:
        update()
    elif kode == 4:
        delete()
    elif kode == 5:
        print("Thank You and Good Bye!!!")
        break
    else :
        print("****** Pilihan yang anda masukan salah! ******")
        
     
     
