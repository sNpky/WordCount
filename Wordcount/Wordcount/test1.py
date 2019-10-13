from unittest import TestCase
from Wordcount import My_words_count
from Wordcount import My_lines_count
from Wordcount import My_chars_count
from Wordcount import word_count
from Wordcount import My_cmd
class TestMy_chars_count(TestCase):
    def test_My_chars_count(self):
        file_name=wc.txt
        self.assertEqual(240,My_chars_count(file_name))
        
