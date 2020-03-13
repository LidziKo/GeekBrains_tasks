def personal_data(**kwargs):
    name = kwargs.get('name', 'N/A')
    surname = kwargs.get('surname', 'N/A')
    age = kwargs.get('age', 'N/A')
    phone = kwargs.get('phone', 'N/A')
    email = kwargs.get('email', 'N/A')
    city = kwargs.get('city', 'N/A')
    print(f'Имя: {name}, Фамилия: {surname}, Возраст: {age}, Телефон: {phone}, Email: {email}, Город: {city}')


n = input('имя ')
sn = input('фамилия ')
a = input('возраст ')
ph = input('номер телефона ')
e = input('почта ')
c = input('город проживания ')

personal_data(name=n, surname=sn, age=a, phone=ph, email=e, city=c)

