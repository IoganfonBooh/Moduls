[pytest]
markers =
   api: тесты API
   ui: тесты UI
   event: тесты мероприятий
   auth: тесты авторизации


# pytest test.py -v -m "api" # test.py замените на имя своего файла в проекте
# pytest test.py -v -m "ui and auth"
# pytest test.py -v -m "auth or event"