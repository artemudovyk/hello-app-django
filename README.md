# hello-app-django

## How to run app (with docker):
```
git clone https://github.com/artemudovyk/hello-app-django
cd hello-app-django
docker-compose build
docker-compose up -d
```
And then visit http://localhost:3000/


To shutdown:
```
docker-compose down
```

## Preview:

![image](https://user-images.githubusercontent.com/58283675/148697676-7b13f5a3-bd5d-4e1b-ace0-6a6a13585c94.png)
![image](https://user-images.githubusercontent.com/58283675/148697662-2a115351-ef62-4434-bd45-f0211fc4a2dd.png)


## Task description:
>Завдання №2
>
>Потрібно написати веб-сервіс. На головній сторінці форма з полем введення імені та кнопкою "Привітатись". При натисканні на кнопку, якщо ім'я зустрілося вперше, виведи "Привіт, <Ім'я+Прізвище> або "Привіт, <email>" (на твій вибір). Якщо таке ім'я вже зустрічалося, виведи "Вже бачилися, ім'я".
>
>Також на головній має бути посилання, при натисканні на яке потрібно показати список усіх, з ким уже привіталися.
>
>Подумай, де краще зберігати стан (state). Як його краще зберігати? Чи можливо оптимізувати по пам'яті, якщо ми очікуємо, що до нас прийдуть вітатись користувачі всього Інтернету. >Зроби проект на Github із репозиторієм.
>
>Плюс, якщо є зрозумілий README, проект загорнутий у Docker, застосовані GitHub Actions, проект розгорнутий на будь-якому хостингу (heroku, digitalocean, будь-який інший)
>
>Якщо хочеться додати щось до цього завдання - не соромся проявити творчість.
