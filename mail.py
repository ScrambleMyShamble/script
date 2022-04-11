# библиотеки для работы с электронной почтой
import imaplib
import schedule  # для запуска скрипта в определенное время


def mail_cleaner():
    # Логинимся в почту
    username = ''
    password = ''
    # домен gmail,yandex,rambler нужное вставить
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    log = mail.login(username, password)
    # В INBOX хранится ВСЯ ПОЧТА
    mail.select("INBOX")

    # проверяем есть ли нежелательные письма, например спам или старые письма
    # вместо '(SUBJECT "Title")' нужно добавить нежелательные темы писем, например реклама.
    results, messages = mail.search(None, '(SUBJECT "Title")')
    # создаём список нежелательных писем
    messages = messages[0].split()
    # проходимся по ним в цикле и помещаем в корзину, т.е. удаляем
    for x in messages:
        result, message = mail.store(x, '+X-GM-LABELS', '\\Trash')
    # закрываем клиент, закрываем сессию
    mail.close()
    mail.logout()


# Каждый день в 20.00 запуск функции mail_cleaner которая будет логиниться в почту и удалять ненужные письма
# if __name__ == '__main__':
#     schedule.every().day.at("20:00").do(mail_cleaner())
