from requests import get
temp = input('Введите температуру тела в градусах цельсиях(temp) = ')
pulse = input('Введите пульс(pulse) = ')
pain_level = input('Введите уровень боли(pain_level) = ')
print(get(f'http://localhost:5000/api?temp={temp}&pulse={pulse}&pain_level={pain_level}').json())