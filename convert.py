import xmltodict
import markdown
import os

def convert_xml_to_md(xml_file_path, output_folder):
    with open(xml_file_path, 'r', encoding='windows-1251') as xml_file:
        xml_data = xml_file.read()
        data_dict = xmltodict.parse(xml_data)

        items = data_dict['item']  # Получение всех элементов <item>

        if isinstance(items, list):  # Если есть несколько элементов <item>
            for item in items:
                convert_item_to_md(item, output_folder)
        elif isinstance(items, dict):  # Если только один элемент <item>
            convert_item_to_md(items, output_folder)

    print('Преобразование завершено!')

def convert_item_to_md(item, output_folder):
    title = item['title']
    content = item['description']

    # Преобразование контента в Markdown
    md_content = markdown.markdown(content)

    # Создание файла Markdown
    md_file_path = os.path.join(output_folder, f'{title}.md')
    with open(md_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

# Путь к файлу XML и папке для сохранения файлов Markdown
xml_file_path = 'C:\Home\Python\XMLtoMD\spring_2010.xml'
output_folder = 'C:\Home\Python\XMLtoMD'

convert_xml_to_md(xml_file_path, output_folder)