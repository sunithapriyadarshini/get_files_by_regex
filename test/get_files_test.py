""" Unit test to test get_files
"""
import random
import string
import tempfile
import unittest

from get_files import get_files


class TestGetFiles(unittest.TestCase):
    """
       Class to test get_files module
    """

    def test_get_all_files(self):
        """ Tests get list of files in temp dir.
        """

        temp_dir = tempfile.gettempdir()
        all_files = get_files.get_files_by_regex(temp_dir, '')

        self.assertGreater(len(all_files), 0)

    def test_get_file_by_regex(self):
        """ Tests get list of files by regex.
        """

        temp_dir = tempfile.gettempdir()
        temp = tempfile.NamedTemporaryFile(
            prefix="dummyPrefix_", suffix="_dummySuffix")
        dummy_file = get_files.get_files_by_regex(temp_dir, 'dummyPrefix_')

        self.assertEqual(len(dummy_file), 1)

    def test_get_file_not_valid(self):
        """ Tests get list of files for invalid directory.
        """

        random_dir = ''.join(random.choice(string.ascii_lowercase)
                             for i in range(10))

        random_dir_files = get_files.get_files_by_regex(random_dir, '')

        self.assertEqual(len(random_dir_files), 0)

    def test_get_file_not_valid_regex(self):
        """ Tests get list of files for random regex.
        """

        temp_dir = tempfile.gettempdir()
        random_regex = ''.join(random.choice(
            string.ascii_lowercase) for i in range(10))
        regex_files = get_files.get_files_by_regex(temp_dir, random_regex)

        self.assertEqual(len(regex_files), 0)

    def test_get_not_valid_regex(self):
        """ Tests get list of files for random regex.
        """
        temp_dir = tempfile.gettempdir()
        random_regex = '**'
        try:
            get_files.get_files_by_regex(temp_dir, random_regex)
        except:
            pass


if __name__ == '__main__':
    unittest.main()
