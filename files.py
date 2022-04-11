import os  # для работы с операционной системой
import shutil  # для работы с файлами
import time
import schedule  # для запуска скрипта в определенное время


# Очистка старых папок, удаляются папки и файлы которые старше переменной days
def delete_old_files():
    # переменные для подсчета удаленных файлов или директорий
    deleted_files_count = 0
    deleted_folders_count = 0

    # Путь к директории с файлами
    path = ''
    # если кол-во дней больше days - удаляем файлы
    days = 0
    seconds = time.time() - (days * 24 * 60 * 60)

    # если в переменной path находится существующая директория
    if os.path.exists(path):
        # проходимся циклом по подпапкам и файлам
        for root_folder, folders, files in os.walk(path):
            # сравниваем время файлов с days, если больше то удалим
            if seconds >= get_files_age(root_folder):
                # удаляем
                remove_folder(root_folder)
                deleted_folders_count += 1
                # так как корневая папка удалена, можно сразу сделать break
                break

            else:
                # проверяем папки внутри корневой папки
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    # если папка старше days, удаляем
                    if seconds >= get_files_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders_count += 1

                # проверяем файлы в текущей директории
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= get_files_age(file_path):
                        remove_file(file_path)
                        deleted_files_count += 1

        # если в переменной path находится файл, а не директория
        else:
            if seconds >= get_files_age(path):
                remove_file(path)
                deleted_files_count += 1

    # если в переменной path находится несуществующий путь
    else:
        print(f'{path} не найден')

    print(f'Удалено {deleted_folders_count} папок')
    print(f'Удалено {deleted_files_count} файлов')


# Функция удаления найденных директорий
def remove_folder(path):
    if not shutil.rmtree(path):
        print(f'{path} удалён')

    else:
        print(f'{path} невозможно удалить')


# функция удаления найденных файлов
def remove_file(path):
    if not os.remove(path):
        print(f'{path} удалён')

    else:
        print(f'{path} невозможно удалить')


# функция определяющая время существования файлов для их послудующего сравнения
def get_files_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


# функция удаления файлов по выбранному расширению
def delete_files_by_extension():
    # путь к директории с файлами
    path = ''
    # файлы с указанным расширением будем удалять
    extension = ''
    # если указанный путь существует
    if os.path.exists(path):
        # если по указанному пути директория
        if os.path.isdir(path):
            # проходимся по всем подпапкам
            for root_folder, folders, files in os.walk(path):
                # проверяем файлы
                for file in files:
                    # путь к файлу
                    file_path = os.path.join(root_folder, file)
                    # вытаскиваем расширение файла
                    file_extension = os.path.splitext(file_path)[1]
                    # если указанное нами расширение совпадает с расширением найденого файла
                    if extension == file_extension:
                        if not os.remove(file_path):
                            print(f'{file_path} удалён')
                        else:
                            print(f'{file_path} удалить невозможно')

        # если в переменной path не директория
        else:
            print(f'{path} не является директорией')

    # если такого пути не существует
    else:
        print(f'{path} не существует')

# Удаление файлов по расширениям каждый понедельник
# if __name__ == '__main__':
#     schedule.every().monday.do(delete_files_by_extension())

# Удаление старых файлов каждый понедельник
# if __name__ == '__main__':
#     schedule.every().monday.do(delete_old_files())
