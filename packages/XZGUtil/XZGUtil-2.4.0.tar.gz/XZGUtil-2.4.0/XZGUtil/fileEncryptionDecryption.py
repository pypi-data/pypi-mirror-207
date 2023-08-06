#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023-05-10 10:40
# @Site    :
# @File    : fileEncryptionDecryption.py
# @Software: PyCharm
"""文件加密解密工具"""
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import os
from pathlib import Path
from retrying import retry


def encrypt_path_aes(path, password):
    # 对文件名进行AES加密
    key = SHA256.new(password.encode('utf-8')).digest()
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    path_encoded = iv + cipher.encrypt(path.encode('utf-8'))
    return path_encoded.hex()


def decrypt_path_aes(path_encoded, password):
    # 对文件名进行AES解密
    path_encoded = bytes.fromhex(path_encoded)
    key = SHA256.new(password.encode('utf-8')).digest()
    iv = path_encoded[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    path_decoded = cipher.decrypt(path_encoded[AES.block_size:]).decode('utf-8')
    return path_decoded


def rename_all_files_in_directory(dir_path, passwd, de=True):
    """
    获取文件夹下所有的子文件，将文件名加密解密，不包括文件夹
    :param dir_path:
    :param passwd:
    :param de: True加密  Fase 解密
    :return:
    """
    for root, directories, filenames in os.walk(dir_path):
        for filename in filenames:
            # 使用os.path.join()函数将文件名和文件夹路径拼接成完整的文件路径
            file_path = os.path.join(root, filename)
            # 生成新的文件名
            if de:# 加密
                if filename.endswith("#AES.bat"):  #已经加密过了
                    continue
                else:  # 没有加密，可以加密
                    new_filename = encrypt_path_aes(filename, passwd) + "#AES.bat"
            else:  # 解密
                if filename.endswith("#AES.bat"):  # 已经加密过了，可以解密
                    new_filename = decrypt_path_aes(filename.split("#AES.bat")[0], passwd)
                else:
                    continue
            # 使用os.path.join()函数将新的文件名和文件夹路径拼接成完整的文件路径
            new_file_path = os.path.join(root, new_filename)
            # 将文件重命名为新的文件名
            os.rename(file_path, new_file_path)
            print(f'Renamed file {file_path} to {new_file_path}')
    for i in range(1,5):
        try:
            get_all_subfolders(dir_path, passwd, de)
        except Exception as e:
            print(e)

@retry(stop_max_attempt_number=10)
def get_all_subfolders(folder_path, passwd, de=False):
    """获取文件夹下所有文件夹及子文件夹"""
    for root, dirs, files in os.walk(folder_path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if os.path.isdir(folder_path):
                if de:  # 加密
                    if folder.endswith("#AES"):  # 已经加密过了
                        continue
                    else:  # 没有加密，可以加密
                        new_folder_name = encrypt_path_aes(folder, passwd) + "#AES"
                else:  # 解密
                    if folder.endswith("#AES"):  # 已经加密过了，可以解密
                        new_folder_name = decrypt_path_aes(folder.split("#AES")[0], passwd)
                    else:
                        continue
                new_folder_name = os.path.join(root, new_folder_name)
                old_path = Path(folder_path)
                new_path = Path(new_folder_name)
                old_path.rename(new_path)
                print(f'Renamed dir {folder_path} to {new_folder_name}')


if __name__ == '__main__':
    path = 'G:\测试文件'
    password = "mySecretPassword"
    rename_all_files_in_directory(path, password, de=False)
