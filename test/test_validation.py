import pytest
from pydantic import ValidationError, field_validator
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
    with pytest.raises(ValidationError) as exc_info:
        User(name="Михаил",
             email="Mikhail2121@gmail.com",
             password="1qwer}")
    assert "Должна быть хотя бы одна заглавная буква" in str(exc_info.value)

def test_special_character_password():
    with pytest.raises(ValidationError) as exc_info:
        User(name="Михаил",
             email="Mikhail2121@gmail.com",
             password="1Qwerty1")
    assert "должен быть хотя бы один спец.символ" in str(exc_info.value)

def test_digit_password():
    with pytest.raises(ValidationError) as exc_info:
        User(name="Михаил",
             email="Mikhail2121@gmail.com",
             password="Qwerty}")
    assert "должна быть хотя бы одна цифра" in str(exc_info.value)


# тест для нескольких случаев
test_cases = [
    ("Qwerty1", "минимум 8 символов"),
    ("Qwerty1!", "заглавная буква"),
    ("Qwertyu1", "специальный символ"),
    ("Qwerty!!!", "хотя бы одну цифру"),
    ("Qwerty1!", None)  # Успешный случай
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
