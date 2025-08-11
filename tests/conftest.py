# tests/conftest.py
import os
import sys

# Добавляем в sys.path корень репо, чтобы импортировался пакет "praktikum"
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)
