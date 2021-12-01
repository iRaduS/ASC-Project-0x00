from unittest import TestCase, main
from random import choice
from string import printable
from pathlib import Path
from itertools import cycle

def xor(contents, passphrase) -> bytes:
    return bytes(content ^ passchr for content, passchr in zip(contents, cycle(passphrase)))

class UnitXor(TestCase):
    def test_generate_input(self):
        with open('dump_input.txt', 'wb') as inputFile:
            inputFile.write(str.encode(''.join(choice(printable) for i in range(1024))))
            inputFile.close()

        current_path = Path('.')
        file_path = current_path / 'dump_input.txt'
        self.assertEqual(file_path.exists(), True, 'An input file must exist to continue this operation')

    def test_generate_output(self):
        with open('dump_input.txt', 'rb') as inputFile, open('dump_output', 'wb') as outputFile:
            outputFile.write(xor(inputFile.read(),  b'Special20465'))
            outputFile.close()

        current_path = Path('.')
        file_path = current_path / 'dump_output'
        self.assertEqual(file_path.exists(), True, 'An output file must exist to continue this operation')
    
    def test_generate_recover_input_file(self):
        with open('dump_output', 'rb') as inputFile, open('dump_resotre_input.txt', 'wb') as outputFile:
            outputFile.write(xor(inputFile.read(), b'Special20465'))
            outputFile.close()
        
        current_path = Path('.')
        file_path = current_path / 'dump_resotre_input.txt'
        self.assertEqual(file_path.exists(), True, 'A restore input file must exist to continue this operation')
    
    def test_xor_components(self):
        with open('dump_input.txt', 'rb') as inputFile, open('dump_resotre_input.txt', 'rb') as inputRestoreFile:
            self.assertEqual(inputFile.read(), inputRestoreFile.read(), 'The contents should be the same')

if __name__ == '__main__':
    main()