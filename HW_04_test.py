import unittest
from HW_04 import get_repo
from unittest.mock import patch

class TestgetRepo(unittest.TestCase):
    @patch('HW_04.get_repo')
    def test_repo(self, mock_get_repo):
        mock_get_repo.return_value = ['user_name']
        expected = ['User: HeliPatel98',
                    'Repository: helloworld Number of commits: 2',
                    'Repository: SSW-567 Number of commits: 2',
                    'Repository: SSW-695_COOKIT Number of commits: 1',
                    'Repository: SSW567_HW04 Number of commits: 6',
                    'Repository: Student_Repository Number of commits: 23',
                    'Repository: Triangle567 Number of commits: 17']

        self.assertEqual(get_repo(), expected)

if __name__ == '__main__':
    unittest.main()
