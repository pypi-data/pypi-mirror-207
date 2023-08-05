from argparse import Namespace
import unittest
from unittest.mock import patch, mock_open
from unique_char_counter_cli_kir_boh import unique_char_counter_cli


class TestUniqueCharCounterCli(unittest.TestCase):
    def test_return_amount_once_occured_items_with_string(self):
        self.assertEqual(unique_char_counter_cli.return_amount_once_occured_items('11adadfgfgfacehgj'), 4)

    def test_return_amount_once_occured_items_with_empty_string(self):
        self.assertEqual(unique_char_counter_cli.return_amount_once_occured_items(''), 0)

    def test_return_amount_once_occured_items_with_space(self):
        self.assertEqual(unique_char_counter_cli.return_amount_once_occured_items(' '), 0)

    def test_return_amount_once_occured_items_with_unhashable_obj(self):
        with self.assertRaises(TypeError) as e:
            unique_char_counter_cli.return_amount_once_occured_items(['ff'])
        self.assertEqual("unhashable type: 'list'", e.exception.args[0])

    @patch('unique_char_counter_cli_kir_boh.unique_char_counter_cli.get_obj_from_cli')
    @patch('builtins.open', new_callable=mock_open, read_data='dataff')
    def test_main_with_mock_file(self, mock_open, mock_get_obj_from_cli):
        mock_get_obj_from_cli.return_value = Namespace(string=False, file=True, hashable_obj='some file')
        self.assertEqual(unique_char_counter_cli.main(), 2)

    @patch('unique_char_counter_cli_kir_boh.unique_char_counter_cli.get_obj_from_cli')
    def test_main_with_mock_file(self, mock_get_obj_from_cli):
        mock_get_obj_from_cli.return_value = Namespace(string=True, file=False, hashable_obj='some file')
        self.assertEqual(unique_char_counter_cli.main(), 7)


    @patch('builtins.open', new_callable=mock_open, read_data='dat\nafff')
    def test_read_file_in_chunks(self, mock_open):
        self.assertEqual(unique_char_counter_cli.read_file_in_chunks('file.txt', chunk_size=3), 'dat\nafff')
