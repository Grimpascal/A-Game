import os
import pandas as pd
import time
from tabulate import tabulate as tb

hapus = os.system('cls')

def utama():
    hapus
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
    hapus
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

