import unittest
import json
import requests
from unittest import mock
from HW05 import list_repo
from HW05 import commits

class Response:
    def __init__(self,json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data

example = {"https://api.github.com/users/richkempinski/repos": "Repository.json",
            "https://api.github.com/repos/richkempinski/csp/commits": "csp.json",
            "https://api.github.com/repos/richkempinski/hellogitworld/commits": "hellogitworld.json",
            "https://api.github.com/repos/richkempinski/helloworld/commits": "helloworld.json",
            "https://api.github.com/repos/richkempinski/Mocks/commits": "Mocks.json",
            "https://api.github.com/repos/richkempinski/Project1/commits": "Project1.json",
            "https://api.github.com/repos/richkempinski/richkempinski.github.io/commits":
                "richkempinski.github.io.json",
            "https://api.github.com/repos/richkempinski/try_nbdev/commits": "try_nbdev.json",
            "https://api.github.com/repos/richkempinski/try_nbdev2/commits": "try_nbdev2.json",
            "https://api.github.com/repos/richkempinski/threads-of-life/commits": "threads-of-life.json"}

def request_commit(*args):
    if args[0] in example:
        with open(example[args[0]]) as f:
            return Response(json.load(f))
    return Response(None)

def request_get(*args):
    if args[0] in example:
        with open(example[args[0]]) as f:
            return Response(json.load(f))
    return Response(None)

class GitResponse(unittest.TestCase):
    @mock.patch('requests.get',side_effect = request_get)
    def test_repo(self, mock_get):
        expected = ['csp', 'hellogitworld', 'helloworld', 'Mocks', 'Project1',
                            'richkempinski.github.io', 'threads-of-life', 'try_nbdev', 'try_nbdev2']
        self.assertEqual(list_repo("richkempinski"), expected)

    @mock.patch('requests.get',side_effect = request_commit)
    def test_commits(self,mock_get):
        self.assertEqual(commits("richkempinski", "csp"), 2)
        self.assertEqual(commits("richkempinski", 'hellogitworld'), 30)
        self.assertEqual(commits("richkempinski", 'helloworld'), 6)
        self.assertEqual(commits("richkempinski", 'Mocks'), 10)
        self.assertEqual(commits("richkempinski", 'Project1'), 2)
        self.assertEqual(commits("richkempinski", 'richkempinski.github.io'), 9)
        self.assertEqual(commits("richkempinski", 'threads-of-life'), 1)
        self.assertEqual(commits("richkempinski", 'try_nbdev'), 2)
        self.assertEqual(commits("richkempinski", 'try_nbdev2'), 5)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)