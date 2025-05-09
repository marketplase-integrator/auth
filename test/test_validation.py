import pytest
from pydantic import ValidationError, field_validator
from model.models import User


# Тест на успешную валидацию
def valid_password():
    user = User(email="Mikhail2121@gmail.com",
                password="1Qwerty}")
    assert user.password == "1Qwerty}"
# Тест на не успешную валидацию
def short_password():
    with pytest.raises(ValidationError) as exc_info:
        User(email="Mikhail2121@gmail.com",
             password="1Qwer}" )
    assert "минимум 8 символов" in str(exc_info.value)

def big_letter_password():
    with pytest.raises(ValidationError) as exc_info:
        User(email="Mikhail2121@gmail.com",
             password="1qwer}")
    assert "Должна быть хотя бы одна заглавная буква" in str(exc_info.value)

def special_character_password():
    with pytest.raises(ValidationError) as exc_info:
        User(email="Mikhail2121@gmail.com",
             password="1Qwerty1")
    assert "должен быть хотя бы один спец.символ" in str(exc_info.value)

def digit_password():
    with pytest.raises(ValidationError) as exc_info:
        User(email="Mikhail2121@gmail.com",
             password="Qwerty}")
    assert "должна быть хотя бы одна цифра" in str(exc_info.value)


# тест для нескольких случаев
@pytest.mark.parametrize("password,expected_error",[
    ("1Qwer}", "минимум 8 символов"),
    ("1qwerty}", "минимум одна большая буква"),
    ("1Qwertyy", "нет спец.символа"),
    ("Qwertyr}"), "отсутствуют цифры"
])

def password_validation(password, expected_error):
    with pytest.raises(ValidationError) as exc_info:
        User(email="Mikhail2121@gmail.com",
             password=password)
    assert expected_error in str(exc_info.value)