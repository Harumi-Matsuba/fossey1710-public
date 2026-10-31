import os
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'src'))

import decode  # noqa: E402


class TestKey(unittest.TestCase):
    def test_key_is_the_nine_commonest_letters(self):
        self.assertEqual(''.join(decode.KEY[d] for d in '123456789'), 'aeioulmnr')

    def test_digits_only(self):
        self.assertEqual(set(decode.KEY), set('123456789'))
        self.assertNotIn('0', decode.KEY)


class TestDecode(unittest.TestCase):
    def test_known_plaintext_line(self):
        # p. 19 in cipher against the same phrase written in clear on p. 18.
        # "uu" is the notebook's spelling of w (blouu = blow).
        self.assertEqual(decode.decode('f49 a b6455 38 a h49s2s ey2'),
                         'for a blouu in a horses eye')

    def test_other_letters_are_left_alone(self):
        self.assertEqual(decode.decode('that'), 'that')
        self.assertEqual(decode.decode('C9217'), 'Cream')

    def test_case_and_punctuation_survive(self):
        self.assertEqual(decode.decode('B462: 19729y.'), 'Bole: armery.')

    def test_zero_is_not_a_cipher_sign(self):
        self.assertEqual(decode.decode('30'), 'i0')

    def test_empty(self):
        self.assertEqual(decode.decode(''), '')


class TestStream(unittest.TestCase):
    def test_comments_are_passed_through(self):
        got = list(decode.decode_stream(['# f49 a b6455\n', 'f49\n']))
        self.assertEqual(got, ['# f49 a b6455', 'for'])

    def test_crlf_and_blank_lines(self):
        got = list(decode.decode_stream(['\n', 'f49\r\n']))
        self.assertEqual(got, ['', 'for\r'])


class TestCli(unittest.TestCase):
    def run_cli(self, args, stdin=''):
        return subprocess.run([sys.executable, os.path.join(ROOT, 'src', 'decode.py')] + args,
                              input=stdin, capture_output=True, text=True)

    def test_reads_stdin(self):
        r = self.run_cli(['-'], 'f49 a h49s2\n')
        self.assertEqual(r.returncode, 0)
        self.assertEqual(r.stdout, 'for a horse\n')

    def test_missing_file_fails_loudly(self):
        r = self.run_cli([os.path.join(ROOT, 'no_such_file.txt')])
        self.assertNotEqual(r.returncode, 0)
        self.assertIn('No such file', r.stderr)

    def test_binary_input_does_not_crash_silently(self):
        r = self.run_cli(['-'], '\x00\x01 f49\n')
        self.assertEqual(r.returncode, 0)
        self.assertIn('for', r.stdout)


if __name__ == '__main__':
    unittest.main()
