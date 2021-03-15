import unittest
from HW_04 import get_repo

class TestgetRepo(unittest.TestCase):
    def test_repo(self):
        expected = ['User: HeliPatel98',
                    'Repository: helloworld Number of commits: 2',
                    'Repository: SSW-567 Number of commits: 2',
                    'Repository: SSW-695_COOKIT Number of commits: 1',
                    'Repository: SSW567_HW04 Number of commits: 13',
                    'Repository: Student_Repository Number of commits: 23',
                    'Repository: Triangle567 Number of commits: 17']

        self.assertEqual(get_repo(), expected)

if __name__ == '__main__':
    unittest.main()
