# task_accounting_system

# Planning system

As a user I want to have a system that allows to create tasks and proceed with them
 
# 1 Introduce a task system 
  1.1 Task can be created\
  1.2 Task description can be updated\
  1.3 Task can be rejected\
  1.4 Task status can be set completed\
  1.5 Task status should be changed with any of (TODO, READY, IN PROGRESS, COMPLETED)\
  1.6 Task can be rejected if it's not started in configurable amount of time
  1.7 User authentication
  1.8 User authorization (with JWT access token lifetime 30 mins, refresh token lifetime 2 days)
  1.9 Managers gives task to developers
# 2 Task should have the following properties:
  2.1 ID                - digit, sequential number by adding for a current number\
  2.2 Name          - name of the task\
  2.3 Description - informative description of\
  2.4 Date            - date/time when task has been added\
  2.5 Status          - status of the current task (TODO, READY, IN PROGRESS, COMPLETED)\
  2.6 Priority        - priority of the task
  2.7 created_by - User who created task (UID)
  2.8 executor - User who execute task (UID)
# 3 Tasks can be sorted
  3.1 by date/time\
  3.2 by priority\
  3.3 by status\
  3.4 by ID\
  3.5 Multiple sorts are not allowed
# 4. Task rejection can be scheduled
  4.1 Tasks can be rejected by configurable time\
  4.2 Task rejection time can be set using appropriate setting 
# *5. Notification about task creation/updating/deleting should be sent to the message broker
 
Application should be applicable with REST approaches and have documented REST API for all resources\
Application should have UML diagrams that have entities relations\
Application should have UML diagrams for internal-services rejections\
Application should have unit-tests\
Application should have logs
Application should have Readme with an explanation of how to run
Application should be Dockered






# Система планирования
# Как пользователь я хочу иметь систему, которая позволяет создавать задачи и выполнять их.

# 1 Представьте систему задач
1.1 Задача может быть создана\
1.2 Описание задачи может быть обновлено\
1.3 Задача может быть отклонена\
1.4 Статус задачи может быть установлен завершенным\
1.5 Статус задачи должен быть изменен на любое из (ЗАДАЧА, ГОТОВ, В ПРОЦЕССЕ, ЗАВЕРШЕНО).\
1.6 Задача может быть отклонена, если она не была запущена в настраиваемое количество времени 
1.7 Аутентификация пользователя
1.8 Авторизация пользователя (со временем жизни токена доступа JWT 30 минут, сроком жизни токена обновления 2 дня)
1.9 Менеджеры дают задание разработчикам

# 2 Задача должна иметь следующие свойства:
2.1 ID - цифра, порядковый номер путем добавления к текущему номеру\
2.2 Имя - название задачи\
2.3 Описание - информативное описание \
2.4 Дата - дата / время, когда задача была добавлена\
2.5 Статус - статус текущей задачи (TODO, READY, IN PROGRESS, COMPLETED)\
2.6 Priority - приоритет задачи
2.7 created_by - Пользователь, создавший задачу (UID)
2.8 исполнитель - Пользователь, выполняющий задачу (UID)

# 3 Задачи можно отсортировать
3.1 по дате / времени\
3.2 по приоритету\
3.3 по статусу\
3.4 по ID\
3.5 Множественные сортировки не допускаются 

# 4. Отказ от задачи можно запланировать
4.1 Задачи могут быть отклонены в настраиваемое время\
4.2 Время отклонения задания можно установить с помощью соответствующей настройки\

# * 5. Уведомление о создании / обновлении / удалении задачи должно быть отправлено брокеру сообщений
Приложение должно быть применимо с подходами REST и иметь задокументированный REST API для всех ресурсов.\
Приложение должно иметь диаграммы UML, которые имеют отношения сущностей\
Приложение должно иметь диаграммы UML для отклонения внутренних сервисов\
В приложении должны быть юнит-тесты\
Приложение должно иметь логи
Приложение должно иметь Readme с объяснением, как запускать
Приложение должно быть Docker



# Server:
Python3\
Django\
DRF\
Unittest\
logging service\
Celery\
Rabbitmq
# REST operation:
Postman\
CURL
# DB: 
postgresql

# Code management tools:
gitlab\
git cli\
git gui tools(pycharm Idea)

# Diagram tools:
 draw.io 
