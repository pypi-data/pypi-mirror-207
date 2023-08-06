import os
import shutil
import argparse

def main():
    try: 
        parser = argparse.ArgumentParser()
        parser.add_argument('-t', '--type', type=str, help='Specify type of the report')
        args = parser.parse_args()

        package_dir = os.path.dirname(__file__)
        source_file = os.path.join(package_dir, f'{args.type}_case_template.docx')

        destination_file = f'./{args.type}_report.docx' if args.type else './mobile_report.docx'

        shutil.copy(source_file, destination_file)
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()
