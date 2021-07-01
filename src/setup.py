"""
Uso: Setup
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 16 Junio 2021
"""

from distutils.core import setup
import py2exe

setup(
name = 'Payload',
description = 'Python-based App',
version = '1.0',
console=['payload.pyw'],
options = {'py2exe': {'bundle_files': 2,
                      'packages':'ctypes',
                      'includes': 'base64,sys,socket,struct,time,code,platform,getpass,shutil'
                      ,}},
zipfile = None,
)


