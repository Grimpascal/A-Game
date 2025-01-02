import os
import pandas as pd
import time
from tabulate import tabulate as tb
import csv
import random
import datetime

def utama():
    os.system('cls')
    print('='*40)
    print('PILIH ROLE'.center(40)) 
    print('='*40)
    print('''1. Admin
2. User''')
    try:
        pilihan = int(input('Masukkan pilihan : '))
        if pilihan == 1:
            login_admin()
        elif pilihan == 2:
            login_user()
        else:
            print('pilihan tidak ada...')
            time.sleep(2)
            utama()
    except ValueError:
        print('Harus angka...')
        time.sleep(2)
        utama()

def login_admin():
    os.system('cls')
    print('='*40)
    print('LOGIN SEBAGAI ADMIN'.center(40))
    print('='*40)
    inputUsername = input('Masukkan Username : ').lower()
    inputPassword = input('Masukkan Password : ').lower()
    if inputUsername == 'admin' and inputPassword == '123':
        os.system('cls')
        print('Membawa anda ke halaman admin...')
        time.sleep(2)
        menu_admin()
    else:
        print('Akun tidak ditemukan...')
        time.sleep(2)
        utama()

def login_user():
    os.system('cls')
    print('='*40)
    print('LOGIN USER'.center(40))
    print('='*40)
    global username
    username = input('Masukkan username : ').lower()
    password = input('Masukkan password : ').lower()
    data = pd.read_csv('csv/user.csv')
    if not os.path.exists('csv/user.csv'):
        with open('csv/user.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','password','saldo','poin','total menang','total kekalahan','total permainan'])
        input('Tekan ENTER untuk refresh >>>')
        login_user()
    elif os.path.exists('csv/user.csv'):
        user = data[(data['username'] == username) & (data['password'] == password)]
        if not user.empty:
            print(f'Selamat datang {username}...')
            time.sleep(2)
            menu_user()
        elif user.empty:
            os.system('cls')
            print('Akun tidak ditemukan...')
            isian = input('Ingin mendaftar? [y][t] : ').lower()
            if isian == 'y':
                daftar_user()
            elif isian == 't':
                utama()
            else:
                print('Tidak sesuai...')
                time.sleep(2)
                login_user()
    else:
        print('Tidak ditemukan')
        time.sleep(2)
        login_user()

def menu_user():
    while True:
        os.system('cls')
        print('='*40)
        print('MENU PENGGUNA A-GAME'.center(40))
        print('='*40)
        print('''1. Lihat profil
2. Bermain
3. isi saldo
4. History isi saldo
5. Tukar poin
6. Ketentuan
7. Keluar''')
        try:
            inputUser = int(input('Masukkan pilihan anda : '))
        except ValueError:
            print('Harus berupa angka dan tidak boleh kosong')
            time.sleep(2)
            continue
        if inputUser == 1:
            os.system('cls')
            print('Membawa anda ke halaman...')
            time.sleep(2)
            lihat_profil()
        elif inputUser == 2:
            bermain()
        elif inputUser == 3:
            isi_saldo()
        elif inputUser == 4:
            histori_saldo()
        elif inputUser == 5:
            tukar_poin()
        elif inputUser == 6:
            ketentuan()
        elif inputUser == 7:
            utama()
        else:
            print('Tidak ada di pilihan...')
            time.sleep(2)
            continue

def ketentuan():
    os.system('cls')
    print('='*40)
    print('KETENTUAN'.center(40))
    print('='*40)
    print('1. TIDAK MINIMAL UNTUK PENUKARAN POIN MENJADI SALDO')
    print('2. PENGGUNA BERMAIN DENGAN KESADARAN SENDIRI')
    print('3. TIDAK ADA REFUND JIKA KALAH BERMAIN GAME KAMI (LOL)')
    print('4. PASTIKAN KALIAN PAHAM JIKA KATA KAK GEM')
    input('Tekan ENTER untuk kembali >>> ')
    menu_user()

def tukar_poin():
    while True:
        os.system('cls')
        print('='*40)
        print('TUKAR POIN'.center(40))
        print('='*40)
        data = pd.read_csv('csv/user.csv')
        cek = data.loc[data['username'] == username]
        poin = cek['poin'].values[0]
        print(f'Poin anda sebanyak = ', poin)
        try:
            inputUser = int(input('Masukkan jumlah poin yang ingin ditukar : '))
        except ValueError:
            print('Harus berupa angka dan tidak boleh kosong')
            time.sleep(2)
            continue
        if inputUser > poin:
            print('Poin anda kurang, mohon input dengan benar')
            time.sleep(2)
            continue
        elif inputUser < 1:
            print('Maaf tidak valid...')
            time.sleep(2)
            continue
        elif inputUser <= poin:
            data.loc[data['username'] == username, 'poin'] -= inputUser
            data.loc[data['username'] == username, 'saldo'] += inputUser
            data.to_csv('csv/user.csv',index=False)
            print('Selamat, anda berhasil mengubah poin menjadi saldo...')
            time.sleep(2)
            menu_user()


def isi_saldo():
    os.system('cls')
    hari = datetime.datetime.today()
    va = random.randint(10000,99000)
    data = pd.read_csv('csv/user.csv')
    print('='*40)
    print('ISI SALDO'.center(40))
    print('='*40)
    inputUser = int(input('Jumlah saldo : '))
    print('Sedang memverifikasi pembayaran...')
    time.sleep(2)
    if not os.path.exists('csv/historisaldo.csv'):
        with open('csv/historisaldo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','jumlah saldo', 'nomor pembayaran', 'tanggal'])
        input('Terjadi update tekan ENTER untuk refresh >>> ')
        isi_saldo()
    elif os.path.exists('csv/historisaldo.csv'):
        with open('csv/historisaldo.csv','a',newline='') as file:
            tulis = csv.writer(file)
            tulis.writerow([username,inputUser,va,hari])
        data.loc[data['username'] == username, 'saldo'] += inputUser
        data.to_csv('csv/user.csv',index=False)
        print('Selamat saldo anda telah terisi...')
        time.sleep(2)
        menu_user()

def histori_saldo():
    os.system('cls')
    data = pd.read_csv('csv/historisaldo.csv')
    if not os.path.exists('csv/historisaldo.csv'):
        with open('csv/historisaldo.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','jumlah saldo', 'nomor pembayaran', 'tanggal'])
        input('Terjadi update tekan ENTER untuk refresh >>> ')
        histori_saldo()
    else:
        data.index = range(1,len(data)+1)
        sesuaiUsername = data.loc[data['username'] == username]
        print(tb(sesuaiUsername,headers='keys',tablefmt='grid'))
        input('Tekan ENTER untuk kembali >>> ')
        menu_user()


def bermain():
    global taruhan
    os.system('cls')
    data = pd.read_csv('csv/user.csv')
    cek = data.loc[data['username'] == username]
    saldo = cek['saldo'].values[0]
    print('='*40)
    print('PERMAINAN'.center(40))
    print('='*40)
    print('''1. Tebak angka
2. Batu Kertas Gunting
3. Keluar''')
    print(f'Saldo = {saldo}')
    try:
        inputUser = int(input('Masukkan pilihan permainan : '))
    except ValueError:
        print('Hanya boleh angka...')
        time.sleep(1)
        bermain()
    if inputUser == 1:
        if saldo == 0:
            print('Anda tidak memiliki saldo, silahkan isi dahulu')
            time.sleep(2)
            bermain()
        else:
            os.system('cls')
            taruhan = int(input('Masukkan total taruhan anda : '))
            if taruhan > saldo:
                print(f'Saldo anda tidak mencukupi untuk taruhan, silahkan isi dahulu')
                time.sleep(2)
                bermain()
            elif taruhan <= saldo:
                print(f'Taruhan anda sebesar {taruhan}')
                data = pd.read_csv('csv/user.csv')
                data.loc[data['username'] == username, 'saldo'] -= taruhan
                data.to_csv('csv/user.csv',index=False)
                time.sleep(2)
                tebak_angka()
    elif inputUser == 2:
        if saldo == 0:
            print('Anda tidak memiliki saldo, silahkan isi dahulu')
            time.sleep(2)
            bermain()
        else:
            os.system('cls')
            taruhan = int(input('Masukkan total taruhan anda : '))
            if taruhan > saldo:
                print(f'Saldo anda tidak mencukupi untuk taruhan, silahkan isi dahulu')
                time.sleep(2)
                bermain()
            elif taruhan <= saldo:
                print(f'Taruhan anda sebesar {taruhan}')
                data = pd.read_csv('csv/user.csv')
                data.loc[data['username'] == username, 'saldo'] -= taruhan
                data.to_csv('csv/user.csv',index=False)
                time.sleep(2)
                jankepon()
    elif inputUser == 3:
        menu_user()
    else:
        print('Tidak ada di pilihan...')
        time.sleep(2)
        bermain()

def jankepon():
    os.system('cls')
    tanganSistem = ['batu','kertas','gunting']
    acak = random.randint(0,2)
    sistemTangan = tanganSistem[acak]
    tanganLawanSistem = ['kertas','gunting','batu']
    data = pd.read_csv('csv/user.csv')
    cek = data.loc[data['username'] == username]
    saldo = cek['saldo'].values[0]
    while True:
        print('='*40)
        print('BATU - KERTAS - GUNTING'.center(40))
        print('='*40)
        print('''1. Kertas
2. gunting
3. Batu''')
        inputuser = int(input('Masukkan pilihan anda : ')) - 1
        if tanganLawanSistem[inputuser] == sistemTangan:
            print('Seri, tidak ada yang menang saldo akan dikembalikan...')
            data.loc[data['username'] == username, 'saldo'] += taruhan
            data.to_csv('csv/user.csv',index=False)
            time.sleep(2)
        elif tanganLawanSistem[inputuser] == 'batu':
            if sistemTangan == 'kertas':
                print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
                data.loc[data['username'] == username, 'total kekalahan'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
            elif sistemTangan == 'gunting':
                print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
                data.loc[data['username'] == username, 'saldo'] += taruhan * 2
                data.loc[data['username'] == username, 'poin'] += 100
                data.loc[data['username'] == username, 'total menang'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
        elif tanganLawanSistem[inputuser] == 'kertas':
            if sistemTangan == 'gunting':
                print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
                data.loc[data['username'] == username, 'total kekalahan'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
            elif sistemTangan == 'batu':
                print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
                data.loc[data['username'] == username, 'saldo'] += taruhan * 2
                data.loc[data['username'] == username, 'poin'] += 100
                data.loc[data['username'] == username, 'total menang'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
        elif tanganLawanSistem[inputuser] == 'gunting':
            if sistemTangan == 'batu':
                print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
                data.loc[data['username'] == username, 'total kekalahan'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
            elif sistemTangan == 'kertas':
                print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
                data.loc[data['username'] == username, 'saldo'] += taruhan * 2
                data.loc[data['username'] == username, 'poin'] += 100
                data.loc[data['username'] == username, 'total menang'] += 1
                data.to_csv('csv/user.csv',index=False)
                time.sleep(4)
        else:
            print('Tidak ada di pilihan...')
            time.sleep(2)
            bermain()

        pilihan = input('Apakah anda ingin bermain lagi [y][t] : ')
        if pilihan == 'y':
            if saldo < taruhan:
                print('Saldo tidak mencukupi...')
                time.sleep(2)
                bermain()
            else:
                data.loc[data['username'] == username, 'saldo'] -= taruhan
                data.to_csv('csv/user.csv',index=False)
                os.system('cls')
                continue
        else:
            print('terima kasih telah bermain...')
            time.sleep(2)
            bermain()

def tebak_angka():
    os.system('cls')
    print('Membawa anda ke halaman permainan...')
    time.sleep(2)
    os.system('cls')
    print('Memproses permainan...')
    time.sleep(1)
    os.system('cls')
    print('='*40)
    print('TEBAK ANGKA 1 - 10'.center(40))
    print('='*40)
    while True:
        acak = random.randint(1,10)
        tebakUser = int(input('Masukkan angka tebakan anda : '))
        if tebakUser == acak:
            data = pd.read_csv('csv/user.csv')
            data.loc[data['username'] == username, 'saldo'] += taruhan * 2
            data.loc[data['username'] == username, 'poin'] += 100
            data.loc[data['username'] == username, 'total menang'] += 1
            data.to_csv('csv/user.csv',index=False)
            print('Selamat anda menang, taruhan anda akan dikali 2 dan menjadi saldo...')
            time.sleep(2)
            a = input('ingin bermain lagi dgn taruhan tetap? [y][t] : ')
            if a == 'y':
                if saldo <= taruhan:
                    print('Gagal, karena saldo anda tidak mencukupi')
                    time.sleep(1)
                    bermain()
                elif saldo >= taruhan:
                    os.system('cls')
                    data.loc[data['username'] == username, 'saldo'] -= taruhan
                    data.to_csv('csv/user.csv',index=False)
                    continue
            elif a == 't':
                bermain()
            else:
                print('tidak ada di pilihan...')
                time.sleep(1)
                bermain()
        else:
            data = pd.read_csv('csv/user.csv')
            cek = data.loc[data['username'] == username]
            saldo = cek['saldo'].values[0]
            data.loc[data['username'] == username, 'total kekalahan'] += 1
            data.to_csv('csv/user.csv',index=False)
            print(f'Tebakan anda salah, angka yang benar adalah {acak}')
            a = input('ingin bermain lagi dgn taruhan tetap? [y][t] : ')
            if a == 'y':
                if saldo <= taruhan:
                    print('Gagal, karena saldo anda tidak mencukupi')
                    time.sleep(1)
                    bermain()
                elif saldo >= taruhan:
                    os.system('cls')
                    data.loc[data['username'] == username, 'saldo'] -= taruhan
                    data.to_csv('csv/user.csv',index=False)
                    continue
            elif a == 't':
                bermain()
            else:
                print('tidak ada di pilihan...')
                time.sleep(1)
                bermain()


def lihat_profil():
    os.system('cls')
    print('Sedang membawa anda ke halaman...')
    time.sleep(2)
    os.system('cls')
    print('='*40)
    print('PROFIL'.center(40))
    print('='*40)
    global cekSaldo
    data = pd.read_csv('csv/user.csv')
    cek = data.loc[data['username'] == username]
    cekUsername = cek['username'].values[0]
    cekSaldo = cek['saldo'].values[0]
    cekPassword = cek['password'].values[0]
    cekPoin = cek['poin'].values[0]
    print('Username = ',cekUsername)
    print('Password = ',cekPassword)
    print('Total saldo = ',cekSaldo)
    print('Total poin = ',cekPoin)
    input('Tekan ENTER untuk kembali >>>')
    menu_user()

def daftar_user():
    os.system('cls')
    print('='*40)
    print('REGISTER PENGGUNA'.center(40))
    print('='*40)
    data = pd.read_csv('csv/user.csv')
    saldo = 0
    poin = 0
    inputUser = input('Username : ')
    inputPass = input('Password : ')
    if inputUser in data['username'].values:
        print('Username sudah digunakan, gunakan username lain atau tambahkan angka...')
        time.sleep(2)
        daftar_user()
    else:
        with open('csv/user.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([inputUser,inputPass,saldo,poin, 0,0,0])
        print('Selamat kamu berhasil terdaftar di A-Game...')
        time.sleep(2)
        login_user()


def menu_admin():
    while True:
        os.system('cls')
        print('='*40)
        print('MENU ADMIN'.center(40))
        print('='*40) 
        print('''1. Cek User
2. Kelola User
3. History Deposit
4. Keluar''')
        try:
            inputUser = int(input('Masukkan Pilihan : '))
            if inputUser == 1:
                os.system('cls')
                print('Membawa anda ke halaman...')
                time.sleep(2)
                cek_user()
            elif inputUser == 2:
                kelola_user()
            elif inputUser == 3:
                history_depo()
            elif inputUser == 4:
                utama()
            else:
                print('tidak ada di pilihan...')
                time.sleep(2)
                continue
        except ValueError:
            print('Harus angka...')
            time.sleep(2)
            continue

def cek_user():
    os.system('cls')
    if not os.path.exists('csv/user.csv'):
        with open('csv/user.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','password','saldo','poin','total menang','total kekalahan','total permainan'])
        print('File belum ada, dan baru saja dibuat')
        input('Tekan ENTER untuk refresh >>>')
        cek_user()
    elif os.path.exists('csv/user.csv'):
        data = pd.read_csv('csv/user.csv')
        data['total permainan'] = data['total menang'] + data['total kekalahan']
        data.to_csv('csv/user.csv',index=False)
        data.index = range(1,len(data)+1)
        print(tb(data,headers='keys',tablefmt='grid'))
        input('Tekan ENTER untuk kembali >>>')
        menu_admin()

def kelola_user():
    while True:
        os.system('cls')
        print('='*40)
        print('KELOLA USER'.center(40))
        print('='*40)
        print('''1. Tambah pengguna
2. Hapus pengguna
3. Tambah poin pengguna
4. Tambah saldo pengguna
5. Keluar''')
        try:
            inputUser = int(input('Masukkan pilihan : '))
        except ValueError:
            print('Harus angka dan tidak boleh kosong...')
            time.sleep(2)
            continue
        if inputUser == 1:
            tambah_pengguna()
        elif inputUser == 2:
            hapus_pengguna()
        elif inputUser == 3:
            tambah_poin()
        elif inputUser == 4:
            tambah_saldo()
        elif inputUser == 5:
            menu_admin()

def tambah_saldo():
    while True:
        os.system('cls')
        data = pd.read_csv('csv/user.csv')
        print('='*40)
        print('TAMBAH SALDO'.center(40))
        print('='*40)
        inputUser = input('Masukkan username yang ingin ditambah : ')
        if inputUser in data['username'].values:
            try:
                inputSaldo = int(input('Masukkan jumlah saldo yang ditambah : '))
            except ValueError:
                print('Harus angka dan tidak boleh kosong!')
                time.sleep(2)
                continue
            if inputSaldo < 5000:
                print('Minimal 5000 untuk melakukan pengisian...')
            else:
                data.loc[data['username'] == inputUser, 'saldo'] += inputSaldo
                data.to_csv('csv/user.csv',index=False)
                print('selamat, saldo pengguna telah terisi sebesar', inputSaldo)
                time.sleep(2)
                kelola_user()
        else:
            print('Username tidak ditemukan...')
            time.sleep(2)
            continue

def tambah_poin():
    while True:
        os.system('cls')
        data = pd.read_csv('csv/user.csv')
        print('='*40)
        print('TAMBAH POIN'.center(40))
        print('='*40)
        inputUser = input('Masukkan username yang ingin ditambah : ')
        if inputUser in data['username'].values:
            try:
                inputPoin = int(input('Masukkan poin yang ingin ditambah : '))
            except ValueError:
                print('Harus angka dan tidak boleh kosong!')
                time.sleep(2)
                continue
            if inputPoin <= 0:
                print('Minimal adalah 1 untuk menambah...')
                time.sleep(2)
                continue
            data.loc[data['username'] == inputUser, 'poin'] += inputPoin
            data.to_csv('csv/user.csv',index=False)
            print(f'Selamat, poin user telah ditambah sebesar {inputPoin} ')
            time.sleep(2)
            kelola_user()
        else:
            print('Username tidak ditemukan...')
            time.sleep(2)
            continue



def hapus_pengguna():
    while True:
        os.system('cls')
        print('='*40)
        print('HAPUS PENGGUNA'.center(40))
        print('='*40)
        data = pd.read_csv('csv/user.csv')
        inputUser = input('Masukkan username yang ingin dihapus : ')
        if inputUser in data['username'].values:
            data = data.loc[data['username'] != inputUser]
            data.to_csv('csv/user.csv',index=False)
            print('Selamat username telah berhasil dihapus...')
            time.sleep(2)
            kelola_user()
        else:
            print('Username tidak ditemukan...')
            time.sleep(2)
            continue

def tambah_pengguna():
    while True:
        os.system('cls')
        data = pd.read_csv('csv/user.csv')
        print('='*40)
        print('TAMBAH PENGGUNA'.center(40))
        print('='*40)
        inputUsername = input('Masukkan username baru : ')
        if inputUsername in data['username'].values:
            print('Username Telah Digunakan, Gunakan Username Lain...')
            time.sleep(2)
            continue
        else:
            inputPassword = input('Masukkan password : ')
            if not os.path.exists('csv/user.csv'):
                with open('csv/user.csv','w',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['username','password','saldo','poin','total menang','total kekalahan','total permainan'])
                input('Terjadi Update silahkan ENTER untuk merefresh >>> ')
                time.sleep(2)
                continue
            else:
                with open('csv/user.csv','a',newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([inputUsername,inputPassword,0,0,0,0,0])
                print('Selamat pengguna baru telah ditambahkan...')
                time.sleep(2)
                kelola_user()

def history_depo():
    os.system('cls')
    data = pd.read_csv('csv/historisaldo.csv')
    data.index = range(1,len(data)+1)
    print(tb(data,headers='keys',tablefmt='grid'))
    input('Tekan ENTER untuk kembali >>> ')
    menu_admin()


utama()
