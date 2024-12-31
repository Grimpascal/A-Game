import os
import pandas as pd
import time
from tabulate import tabulate as tb
import csv
import random

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
    if not os.path.exists('csv/user.csv'):
        with open('csv/user.csv','w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','password','saldo','poin'])
        input('Tekan ENTER untuk refresh >>>')
        login_user()
    elif os.path.exists('csv/user.csv'):
        data = pd.read_csv('csv/user.csv')
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
    os.system('cls')
    print('='*40)
    print('MENU PENGGUNA A-GAME'.center(40))
    print('='*40)
    print('''1. Lihat profil
2. Bermain
3. isi saldo
4. Tukar poin
5. Ketentuan
6. Keluar''')
    inputUser = int(input('Masukkan pilihan anda : '))
    if inputUser == 1:
        os.system('cls')
        print('Membawa anda ke halaman...')
        time.sleep(2)
        lihat_profil()
    if inputUser == 2:
        bermain()

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
2. Batu Kertas Gunting''')
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
    print('='*40)
    print('BATU - KERTAS - GUNTING'.center(40))
    print('='*40)
    print('''1. Kertas
2. gunting
3. Batu''')
    inputuser = int(input('Masukkan pilihan anda : ')) - 1
    if tanganLawanSistem[inputuser] == 'batu':
        if sistemTangan == 'kertas':
            print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
            time.sleep(4)
            bermain()
        elif sistemTangan == 'gunting':
            print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
            data.loc[data['username'] == username, 'saldo'] += taruhan * 2
            data.loc[data['username'] == username, 'poin'] += 100
            data.to_csv('csv/user.csv',index=False)
            time.sleep(4)
            bermain()
    elif tanganLawanSistem[inputuser] == 'kertas':
        if sistemTangan == 'gunting':
            print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
            time.sleep(4)
            bermain()
        elif sistemTangan == 'batu':
            print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
            data.loc[data['username'] == username, 'saldo'] += taruhan * 2
            data.loc[data['username'] == username, 'poin'] += 100
            data.to_csv('csv/user.csv',index=False)
            time.sleep(4)
            bermain()
    elif tanganLawanSistem[inputuser] == 'gunting':
        if sistemTangan == 'batu':
            print(f'Sayangnya anda kalah, sistem memilih {sistemTangan} dan anda memilih {tanganLawanSistem[inputuser]}')
            time.sleep(4)
            bermain()
        elif sistemTangan == 'kertas':
            print('Selamat anda menang, Saldo anda akan ditambah dengan total taruhan x 2')
            data.loc[data['username'] == username, 'saldo'] += taruhan * 2
            data.loc[data['username'] == username, 'poin'] += 100
            data.to_csv('csv/user.csv',index=False)
            time.sleep(4)
            bermain()
    else:
        print('Tidak ada di pilihan...')
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
            writer.writerow([inputUser,inputPass,saldo,poin])
        print('Selamat kamu berhasil terdaftar di A-Game...')
        time.sleep(2)
        login_user()


def menu_admin():
    os.system('cls')
    print('='*40)
    print('MENU ADMIN'.center(40))
    print('='*40) 
    print('''1. Cek User
2. Kelola User
3. Laporan
4. History Deposit
5. Keluar''')
    try:
        inputUser = int(input('Masukkan Pilihan : '))
        if inputUser == 1:
            cek_user()
        elif inputUser == 2:
            kelola_user()
        elif inputUser == 3:
            laporan()
        elif inputUser == 4:
            history_depo()
        elif inputUser == 5:
            utama()
        else:
            print('tidak ada di pilihan...')
            time.sleep(2)
            menu_admin()
    except ValueError:
        print('Harus angka...')
        time.sleep(2)
        utama()

def cek_user():
    os.system('cls')
    saldo = 0
    if not os.path.exists('csv/user.csv'):
        with open('csv/user.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username','password','saldo','poin'])
        print('File belum ada, dan baru saja dibuat')
        input('Tekan ENTER untuk refresh >>>')
        cek_user()
    elif os.path.exists('csv/user.csv'):
        data = pd.read_csv('csv/user.csv')
        data.index = range(1,len(data)+1)
        print(tb(data,headers='keys',tablefmt='grid'))
        input('Tekan ENTER untuk kembali >>>')
        menu_admin()

def kelola_user():
    os.system('cls')

def laporan():
    os.system('cls')

def history_depo():
    os.system('cls')


utama()