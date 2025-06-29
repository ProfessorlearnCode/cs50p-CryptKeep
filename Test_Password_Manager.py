import os
import pytest
from Password_Manager import PasswordManager
from cryptography.fernet import Fernet

@pytest.fixture
def password_manager(tmpdir):
    pm = PasswordManager()
    key_path = os.path.join(tmpdir, 'key.key')
    password_path = os.path.join(tmpdir, 'passwords.txt')
    pm.create_key(key_path)
    pm.create_password_file(password_path)
    yield pm, key_path, password_path
    os.remove(key_path)
    os.remove(password_path)

def test_create_key(password_manager):
    pm, key_path, _ = password_manager
    assert os.path.exists(key_path)

def test_loading_key(password_manager):
    pm, key_path, _ = password_manager
    pm.loading_key(key_path)
    assert pm.key is not None

def test_create_password_file(password_manager):
    pm, _, password_path = password_manager
    password_data = {
        "email": "1234567",
        "Facebook": "Meta1234",
        "Youtube": "CS50_",
        "Instagram": "Professor"
    }
    pm.create_password_file(password_path, password_data)
    assert os.path.exists(password_path)

def test_load_password_file(password_manager):
    pm, _, password_path = password_manager
    password_data = {
        "email": "1234567",
        "Facebook": "Meta1234",
        "Youtube": "CS50_",
        "Instagram": "Professor"
    }
    pm.create_password_file(password_path, password_data)
    pm.load_password_file(password_path)
    assert len(pm.password_dictionary) == len(password_data)

def test_add_password(password_manager):
    pm, _, password_path = password_manager
    site = "Twitter"
    password = "Twitter123"
    pm.add_password(site, password)
    with open(password_path, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        stored_site, encrypted_password = last_line.strip().split(":")
        decrypted_password = Fernet(pm.key).decrypt(encrypted_password.encode()).decode()
        assert stored_site == site
        assert decrypted_password == password


