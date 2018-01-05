import sys
import os
from pypinyin import lazy_pinyin


def main():
    try:
        if len(sys.argv) >= 3:
            file_path, encoding = sys.argv[1:3]
            if os.path.isfile(file_path):
                with open(file_path, encoding=encoding, errors='ignore') as f:
                    result = []
                    for line in f.readlines():
                        try:
                            result.append(lazy_pinyin(line))
                        except Exception as e:
                            print('convert error line: {}\r\n'.format(line))
                            print('error message: {}'.format(e))
                    new_file_path = file_path+'.pinyin'
                    with open(new_file_path, 'w', encoding=encoding, errors='ignore') as w:
                        for line in result:
                            w.write(''.join(line))
                        print('{} generated'.format(new_file_path))
            else:
                raise FileNotFoundError
        else:
            raise AttributeError
    except FileNotFoundError or AttributeError:
        print('How?\r\n'
              '===============\r\n'
              'main.exe ${file_name} ${file_encoding}\r\n'
              'example:\r\nmain.exe test.csv big5')


if __name__ == '__main__':
    main()
