from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname  # имя пользователя, строка
        self.password = hash(password)  # пароль в хэшированном виде, число
        self.age = age  # возраст, число

    def __eq__(self, other):
        if isinstance(other, str):
            return self.nickname == other
        elif isinstance(other, User):
            return self.nickname == other.nickname
        else:
            return False

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # заголовок, строка
        self.duration = duration  # продолжительность, секунды
        self.time_now = 0  # секунда остановки, изначально 0
        self.adult_mode = adult_mode  # ограничение по возрасту, bool(False по умолчанию)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.title == other
        elif isinstance(other, Video):
            return self.title == other.title
        else:
            return False


class UrTube:
    def __init__(self):
        self.users = []  # список объектов User
        self.videos = []  # список объектов Video
        self.current_user = None  # текущий пользователь, User

    def __contains__(self, item):
        return item in self.videos

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user:  # если пользователь существует
                if user.password == hash(password):  # если пароль совпадает
                    self.current_user = user
                    break

    def register(self, nickname, password, age):
        permission_register = True  # разрешение на регистрацию
        for user in self.users:
            if nickname == user:  # если имя уже существует
                print(f'Пользователь {nickname} уже существует')
                permission_register = False  # запрет на регистрацию
                break
        if permission_register:  # если регистрация разрешена
            new_user = User(nickname, password, age)
            self.users.append(new_user)  # добавление пользователя в список
            self.current_user = new_user  # 'автоматический вход' после регистрации

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            if new_video in self:  # если уже существует видео с таким названием
                break  # не добавляем
            else:
                self.videos.append(new_video)  # добавляем видео в список

    def get_videos(self, word):
        result = []
        for video in self.videos:  # пробегаем по списку с видео
            if video.title.lower().find(word.lower()) == -1:  # если совпадений не найдено
                continue  # идем по списку дальше
            else:  # если совпадение найдено
                result.append(video.title)  # добавляем название видео в список
        return result

    def watch_video(self, name_video):
        def play(v):  # 'проигрывание' видео
            for sec in range(v.time_now, v.duration):
                print(sec + 1, end=' ')
                sleep(1)
            print('Конец видео')

        if self.current_user:  # если пользователь вошел в аккаунт
            for video in self.videos:
                if video == name_video:  # если точное совпадение
                    if video.adult_mode:
                        if self.current_user.age >= 18:  # если пользователь 18+
                            play(video)
                            break
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        play(video)
                        break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
