# Natalie Aragon 
# Assignment 3a - Github Test API
#02/18/2026 

import unittest
from unittest.mock import patch, Mock

from HW3a_github_api.github_api import get_repo_commit_counts


class TestGitHubAPIMocked(unittest.TestCase):

    @patch("HW3a_github_api.github_api.requests.get")
    def test_mocked_api(self, mock_get):
        # Fake repo list response
        repos_response = Mock()
        repos_response.status_code = 200
        repos_response.json.return_value = [
            {"name": "TestRepo1"},
            {"name": "TestRepo2"}
        ]

        # Fake commits response for repo1 (3 commits)
        commits_response_1 = Mock()
        commits_response_1.status_code = 200
        commits_response_1.json.return_value = [{}, {}, {}]

        # Fake commits response for repo2 (2 commits)
        commits_response_2 = Mock()
        commits_response_2.status_code = 200
        commits_response_2.json.return_value = [{}, {}]

        # requests.get called 3 times total
        mock_get.side_effect = [repos_response, commits_response_1, commits_response_2]

        result = get_repo_commit_counts("fakeuser")
        self.assertEqual(result, [("TestRepo1", 3), ("TestRepo2", 2)])


if __name__ == "__main__":
    unittest.main()
