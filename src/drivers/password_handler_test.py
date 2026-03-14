from src.drivers.password_handler import PasswordHandler


def test_encrypt():
    minha_senha = "123RocketENois"
    passord_handler = PasswordHandler()

    hashed_password = passord_handler.encrypt_password(minha_senha)
    password_checked = passord_handler.check_password(minha_senha, hashed_password)
    assert password_checked