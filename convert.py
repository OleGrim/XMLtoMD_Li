import xmltodict
import markdown
import os

def convert_xml_to_md(xml_file_path, output_folder):
    with open(xml_file_path, 'r', encoding='windows-1251') as xml_file:
        xml_data = xml_file.read()
        data_dict = xmltodict.parse(xml_data)

        for entry in data_dict['item']['entry']:
            title = entry['title']
            content = entry['content']['#text']

            # Преобразование контента в Markdown
            md_content = markdown.markdown(content)

            # Создание файла Markdown
            md_file_path = os.path.join(output_folder, f'{title}.md')
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(md_content)

    print('Преобразование завершено!')

# Путь к файлу XML и папке для сохранения файлов Markdown
xml_file_path = 'C:\Home\Python\XMLtoMD\spring_2010.xml'
output_folder = 'C:\Home\Python\XMLtoMD'

convert_xml_to_md(xml_file_path, output_folder)