import os
import pandas as pd
import time
from tabulate import tabulate as tb
import csv

def utama():
    os.system('cls')
    print('='*40)
    print('PILIH ROLE'.center(40)) 
    print('='*40)
    print('''1. Admin
2. User''')
    # try:
    pilihan = int(input('Masukkan pilihan : '))
    if pilihan == 1:
        login_admin()
    elif pilihan == 2:
        login_user()
    else:
        print('pilihan tidak ada...')
        time.sleep(2)
        utama()
    # except ValueError:
    #     print('Harus angka...')
    #     time.sleep(2)
    #     utama()

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

