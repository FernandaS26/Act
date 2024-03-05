# Import modul yang diperlukan
import pytest

# Contoh fungsi sederhana untuk diuji
def add(a, b):
    return a + b

# Fungsi pytest untuk menguji fungsi add
def test_add():
    assert add(1, 2) == 3  # Menyimpulkan bahwa 1 + 2 = 3
    assert add(0, 0) == 0   # Menyimpulkan bahwa 0 + 0 = 0
    assert add(-1, 1) == 0  # Menyimpulkan bahwa -1 + 1 = 0
