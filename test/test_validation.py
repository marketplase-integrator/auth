import pytest
from pydantic import ValidationError, field_validator, EmailStr
from model.models import User


# Тест на успешную валидацию
def test_valid_password():
    user = User(name="Михаил",
                email="Mikhail2121@gmail.com",
                password="1Qwerty}")
    assert user.password == "1Qwerty}"
# Тест на не успешную валидацию
def test_short_password():
    with pytest.raises(ValidationError) as exc_info:
        User(name="Михаил",
             email="Mikhail2121@gmail.com",
             password="1Qwer}" )
    assert "минимум 8 символов" in str(exc_info.value)

def test_big_letter_password():
    """Тест на обязательное наличие заглавной буквы"""
    with pytest.raises(ValidationError) as exc_info:
        User(
            name="Михаил",
            email="Mikhail2121@gmail.com",
            password="10qwerty}"  # Специально без заглавных букв
        )
    assert "Пароль должен содержать хотя бы одну заглавную букву" in str(exc_info.value)

def test_special_character_password():
    """Тест на обязательное наличие спецсимвола"""
    with pytest.raises(ValidationError) as exc_info:
        User(
            name="Михаил",
            email="Mikhail2121@gmail.com",
            password="1Qwerty1"  # Специально без спецсимволов
        )
    assert "Пароль должен содержать хотя бы один специальный символ" in str(exc_info.value)

def test_digit_password():
    """Тест на обязательное наличие цифры"""
    with pytest.raises(ValidationError) as exc_info:
        User(
            name="Михаил",
            email="Mikhail2121@gmail.com",
            password="Qwerty!!"  # Специально без цифр
        )
    assert "Пароль должен содержать хотя бы одну цифру" in str(exc_info.value)


# тест для нескольких случаев
test_cases = [
    ("qwerty11!", "Пароль должен содержать хотя бы одну заглавную букву"),
    ("Qwerty11", "Пароль должен содержать хотя бы один специальный символ"),
    ("Qwerty!!", "Пароль должен содержать хотя бы одну цифру"),
    ("Qw1!", "Пароль должен содержать минимум 8 символов"),
    ("ValidPass123!", None)  # Успешный случай
]


@pytest.mark.parametrize("password,expected_error", test_cases)
def test_password_validation(password, expected_error):
    if expected_error:
        with pytest.raises(ValidationError) as exc_info:
            User(
                name="Михаил",
                email="Mikhail2121@gmail.com",
                password=password
            )
        assert expected_error in str(exc_info.value)
    else:
        user = User(
            name="Михаил",
            email="Mikhail2121@gmail.com",
            password=password
        )
        assert user.password == password
