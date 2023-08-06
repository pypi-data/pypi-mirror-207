import os
import shutil


def main():
    try: 
        package_dir = os.path.dirname(__file__)
        source_file = os.path.join(package_dir, 'mobile_case_template.docx')
        shutil.copy(source_file, './mobile_report.docx')
    except Exception as error:
        print(error)