# Python | Построение графиков
## Инвариантная самостоятельная работа (ИСР)

**Задание #1** 
Используя свободные источники (bn.ru, avito.ru и т.д.), собрать данные о
ценах на недвижимость, выставленную на продажу в разных районах города.
Преобразовать данные в формат csv. Разработать скрипт для визуализации
данных, используя библиотеку matplotlib. Для визуализации использовать
тип "точечная диаграмма" (scatterplot).

**Точечная диграмма:**

<img src = "https://github.com/python-advance/sem6-t4-Yalkinzsun/blob/master/%D0%98%D0%BD%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201/plot_v1.png" height = "350" />

**Столбчатая диграмма:**

<img src = "https://github.com/python-advance/sem6-t4-Yalkinzsun/blob/master/%D0%98%D0%BD%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201/plot_v2.png" height = "350" />

**Задания #2-3** 
Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей создавать изображение QR-кода на основе переданной в программу текстовой строки.
Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты изображения в несколько случайно определяемых цветов.
**Функция кодирования строки в QR-код:** 
```Python
def text_to_qrcode(text, module_color, background, file_format='eps', scale=6):
    qr = pyqrcode.create(text)
    if file_format == 'png':
        qr.png('qrcode.png', scale=scale, module_color=module_color, background=background)
    elif file_format == 'eps':
        qr.eps('qrcode.eps', scale=scale, module_color=module_color, background=background)
    elif file_format == 'svg':
qr.svg('qrcode.svg', scale=scale, module_color=module_color, background=background)
```
**Функция декодирования файла QR-кода:**
```Python
def decode_qrcode(file):
    result = decode(Image.open(file))
return result[0].data
```
**Функция изменения цвета для 3 участков QR-кода:** 
```Python
def color_qrcode(file, background):
    image = Image.open(file)  # Открываем изображение.
    image = image.convert("RGB")
    draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]  # Определяем высоту.
    pix = image.load()  # Выгружаем значения пикселей.
    for i in range(int(width / 2)):
        for j in range(int(height / 2)):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (255, 20, 147))

    for i in range(int(width / 2), width):
        for j in range(int(height / 2), height):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (0, 191, 255))

    for i in range(int(width / 2)):
        for j in range(int(height / 2), height):
            a, b, c = pix[i, j]
            if (a, b, c) == background:
                draw.point((i, j), (0, 255, 127))
    image.save("multicolored_qrcode.png", "PNG")
del draw
```
**Результат выполенния программы:**
```
Расшифровка: b"Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one - and preferably only one - obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than 'right now'.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea - let's do more of those!\n"
Расшифровка после перекрашивания: b"Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one - and preferably only one - obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than 'right now'.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea - let's do more of those!\n"
```
**QR-код:**

<img src = "https://github.com/python-advance/sem6-t4-Yalkinzsun/blob/master/%D0%98%D0%BD%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%202-3/qrcode.png" height = "350" />

**QR-код с разноцвеными фрагмантами :**

<img src = "https://github.com/python-advance/sem6-t4-Yalkinzsun/blob/master/%D0%98%D0%BD%D0%B2%D0%B0%D1%80%D0%B8%D0%B0%D0%BD%D1%82%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%202-3/multicolored_qrcode.png" height = "350" />

## Вариативная самостоятельная работа (ВСР)
**Задание #2** 
На основе кода, позволяющего визуализировать определённые данные  (точечная диаграмма), отобразить с помощью библиотеки matplotlib полиномиальный график (степеней полинома 3, 4, 10) 

**Результат выполнения программы :**

<img src = "https://github.com/python-advance/sem6-t4-Yalkinzsun/blob/master/%D0%92%D0%B0%D1%80%D0%B8%D0%B0%D1%82%D0%B8%D0%B2%D0%BD%D0%B0%D1%8F%20%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/plot.png" height = "350" />

