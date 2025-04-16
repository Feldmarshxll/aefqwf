import random
word_list = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар',
             'территория', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'население', 'большинство',
             'музыка', 'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
             'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ', 'журнал', 'руководитель', 'специалист',
             'оценка', 'регион', 'процент', 'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
             'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
             'граница', 'модель', 'операция', 'название', 'старик', 'миллион', 'счастье', 'ребята', 'кабинет',
             'магазин', 'пространство', 'знание', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник',
             'участок', 'желание', 'доктор', 'председатель', 'представление', 'солдат', 'художник', 'оружие',
             'соответствие', 'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга', 'содержание',
             'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сотрудник', 'предложение', 'технология',
             'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'продукция', 'техника',
             'здание', 'необходимость', 'подготовка', 'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
             'обстоятельство', 'победа', 'источник', 'звезда', 'сестра', 'практика', 'проведение', 'карман',
             'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан', 'работник', 'обеспечение',
             'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'теория', 'разработка', 'личность',
             'праздник', 'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель', 'множество',
             'особенность', 'показатель', 'корабль', 'впечатление', 'частность', 'детство', 'профессор', 'прошлое',
             'командир', 'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка', 'заявление', 'попытка', 'сравнение',
             'расчет', 'депутат', 'комитет', 'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
             'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица', 'механизм',
             'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'сожаление', 'заместитель',
             'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист', 'фигура', 'субъект', 'реакция',
             'список', 'фотография', 'журналист', 'нарушение', 'заседание', 'больница', 'существо', 'свойство',
             'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник', 'реализация', 'страница',
             'формирование', 'житель', 'красота', 'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
             'университет', 'традиция', 'декабрь', 'ладонь', 'сведение', 'цветок', 'октябрь', 'занятие', 'сентябрь',
             'помещение', 'январь', 'зритель', 'редакция', 'фактор', 'август', 'известие', 'зависимость', 'охрана',
             'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция', 'переход', 'произведение',
             'родина', 'собственность', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'клиент', 'отрасль',
             'беседа', 'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение', 'понимание', 'апрель',
             'кодекс', 'настроение', 'должность', 'преступление', 'лестница', 'установка', 'появление', 'получение',
             'образец', 'главное', 'костюм', 'ценность', 'обязанность', 'таблица', 'воспоминание', 'лошадь', 'коллега',
             'организм', 'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение', 'оборона', 'выступление',
             'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан', 'километр', 'признак',
             'промышленность', 'американец', 'заключение', 'восток', 'исключение', 'постановление', 'перевод',
             'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина',
             'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка', 'изучение', 'просьба', 'публика', 'сообщение',
             'угроза', 'достижение', 'назначение', 'реклама', 'портрет', 'стакан', 'творчество', 'телевизор',
             'инструмент', 'концепция', 'лейтенант', 'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
             'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство', 'вещество',
             'категория', 'гостиница', 'издание', 'объединение', 'темнота', 'человечество', 'колесо', 'опасность',
             'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат', 'родственник', 'давление',
             'присутствие', 'взаимодействие', 'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание', 'оплата',
             'разница', 'водитель', 'снижение', 'формула', 'капитал', 'новость', 'эффект', 'губернатор', 'доклад',
             'убийство', 'эксперт', 'автобус', 'платье', 'общение', 'психология', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
             'признание', 'постель', 'владелец', 'компьютер', 'инженер', 'старуха', 'ракета', 'вершина', 'выпуск',
             'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность', 'талант', 'эффективность', 'полоса',
             'основное', 'рассмотрение', 'следователь', 'описание', 'редактор', 'дворец', 'забота', 'столик',
             'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'дружба',
             'окончание', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кредит', 'господь',
             'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'металл', 'молоко', 'прокурор',
             'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
             'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король', 'подъезд', 'автомат', 'мальчишка',
             'чтение', 'поселок', 'свидетель', 'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение', 'статус',
             'параметр', 'сказка', 'тенденция', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'эксплуатация',
             'коммунист', 'пенсия', 'приятель', 'объяснение', 'производитель', 'философия', 'мощность', 'обязательство',
             'кризис', 'указание', 'яблоко', 'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
             'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица', 'обработка', 'чемпионат']
def get_word():
    result = random.choice(word_list).upper()
    return result
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |     💀
                   |     /|\\
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |     😭
                   |     /|\\
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |     😨
                   |     /|\\
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |     😖
                   |     /|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |     😩
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |     🥺
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []               
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    while True:
        word_input = input('Введи букву или слово: ').upper()
        if not word_input.isalpha():
            print('Ошибочка, давай по новой')
            continue
        if word_input in guessed_words or word_input in guessed_letters:
            print('повтор? серьезно?')
            continue
        if len(word_input) > 1:
            if word_input == word:
                print('Да! И это правильный ответ! Вы отгадали слово!')
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print('Эээ? в какое место вы хотите поставить эту букву?')
                print(f'осталось {tries} попыток')
                print(display_hangman(tries))
                print(*guessed_letters)
                if tries == 0:
                    print(f'ну ты лошара, слово было {word}')
                    break
                continue
        


        if word_input in word:
            guessed_letters.append(word_input)
            for c in word:
                if c not in guessed_letters:
                    print('Хорош, угадал букву')
                    print(guessed_letters)
                    guessed = False
                    break
                guessed = True
            if guessed:    
                print(word, guessed_letters)
                print('Да! И это правильный ответ! Вы отгадали слово!')
                break
        else:
            guessed_letters.append(word_input)
            tries -= 1
            print(f'Не верно, осталось попыток {tries}')
            print(display_hangman(tries))
            print(guessed_letters)
        if tries == 0:
            print(f'ну ты лошара, слово было {word}')
            break

def main():
    print('Добро пожаловать!')
    play(get_word())
    contin_game = input('Хочешь еще? д/н')
    while True:
        if contin_game.upper() == 'Д':
            play(get_word())
        if contin_game.upper() == 'Н':
            print('Всего хорошего, до новых встреч!')
            break
        else:
            contin_game = input('Для новой игры нажми "д", для выхода из игры "н": ')
            continue
main()