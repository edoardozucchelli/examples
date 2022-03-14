from unittest import mock
from unittest import TestCase
import json


def open_json_file(filename):
    """
    Attempt to open and deserialize a JSON file.

    :param filename: name of the JSON file
    :type filename: str
    :return: dict of log
    :rtype: dict
    """
    try:
        with open(filename) as f:
            try:
                return json.load(f)
            except ValueError:
                raise ValueError('{} is not valid JSON.'.format(filename))
    except IOError:
        raise IOError('{} does not exist.'.format(filename))


class TestOpen(TestCase):
    def test_open_json_file(self):
        # test valid JSON
        read_data = json.dumps({'a': 1, 'b': 2, 'c': 3})
        mock_open = mock.mock_open(read_data=read_data)

        with mock.patch(open, mock_open):
            result = open_json_file('filename')

        self.assertEqual({'a': 1, 'b': 2, 'c': 3}, result)

        # test invalid JSON
        read_data = ''
        mock_open = mock.mock_open(read_data=read_data)

        with mock.patch("__builtin__.open", mock_open):
            with self.assertRaises(ValueError) as context:
                open_json_file('filename')
            self.assertEqual('filename is not valid JSON.', str(context.exception))

        # test file does not exist
        with self.assertRaises(IOError) as context:
            open_json_file('null')
        self.assertEqual('null does not exist.', str(context.exception))
