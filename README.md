Telegram MultiСhat Message - это асинхронный Python скрипт, использующий Pyrogram, для отправки сообщений в несколько Telegram чатов. Этот инструмент идеально подходит для разработчиков и маркетологов, которым необходимо распространять информационные или рекламные сообщения среди различных групп или каналов в Telegram.

Особенности
Асинхронная отправка сообщений для оптимальной производительности.
Поддержка отправки сообщений в множество чатов, указанных в файле.
Возможность задать интервал между пакетами сообщений для избежания ограничений Telegram.
Простая настройка через конфигурационный файл и текстовые файлы.

Как использовать
Заполните файлы config.ini, chats.txt, и message.txt соответствующей информацией:

config.ini: Ваши API ID, API Hash, имя сессии и интервал между отправками сообщений.

chats.txt: Список идентификаторов чатов или их @username, куда будут отправлены сообщения.

message.txt: Текст сообщения для отправки.

Автоматическое создание файлов
Для удобства пользователей скрипт автоматически создает необходимые файлы с образцовыми значениями, если они отсутствуют.
