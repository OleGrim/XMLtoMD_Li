import os
import xmltodict
import markdown
import html2text

# Укажите путь к XML-файлу
xml_file = 'c:\Home\Python\XMLtoMD\spring_2010.xml'

# Укажите папку для сохранения Markdown-файлов
output_folder = 'c:\Home\Python\XMLtoMD'

# Создание папки для сохранения файлов, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Преобразование XML в словарь
with open(xml_file, 'r', encoding='windows-1251') as file:
    data = xmltodict.parse(file.read(), encoding='windows-1251')

# Проход по каждой записи и сохранение в отдельном Markdown-файле
items = data['rss']['channel']['item']
if not isinstance(items, list):
    items = [items]

for item in items:
    title = item['title']
    link = item['link']
    description_html = item['description']

    # Преобразование HTML в Markdown
    h = html2text.HTML2Text()
    h.body_width = 0
    description = h.handle(description_html)

    # Очистка заголовка для использования в имени файла
    filename = "".join(x for x in title if x.isalnum() or x.isspace()).rstrip()
    filename = f"{filename}.md"

    # Преобразование содержимого в Markdown
    markdown_content = f"# {title}\n\n{description}\n\n"

    # Сохранение Markdown-файла
    markdown_output = os.path.join(output_folder, filename)
    with open(markdown_output, 'w', encoding='utf-8') as file:
        file.write(markdown_content)

print("Преобразование XML в Markdown завершено.")