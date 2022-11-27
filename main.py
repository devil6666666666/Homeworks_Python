# Создать прототип интерактивной базы данных, содержащей информацию о сотрудниках
#  некой компании / студентах вуза / учениках школы в виде одной таблицы
#   (кто желает, может создать несколько связанных таблиц или полноценную базу данных).
# Программа должна иметь возможность изменять данные (редактировать добавлять, удалять),
#  осуществлять сохранение и загрузку. А также выводить данные в консоль.

import fileio
import display
import UI

def start():
    mode = UI.start_message()
    match mode:
        case 1:
            data = fileio.read_data("E:\Курс GeekBrains\Python\Homework_8\data.csv")
        case 2:
            fileio.write_data("E:\Курс GeekBrains\Python\Homework_8\data.csv", data)

data = fileio.read_data("E:\Курс GeekBrains\Python\Homework_8\data.csv")
UI.menu(data)