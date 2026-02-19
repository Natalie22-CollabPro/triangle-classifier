# Natalie Aragon 
# Assignment 3a - Github Test API
#02/18/2026 

import unittest
from unittest.mock import patch, Mock

from HW3a_github_api.github_api import get_repo_commit_counts


class TestGitHubAPIMocked(unittest.TestCase):

    @patch("HW3a_github_api.github_api.requests.get")
    def test_repo_commit_counts_mocked(self, mock_get):
        # Mock response for: GET /users/<id>/repos
        repos_response = Mock()
        repos_response.status_code = 200
        repos_response.json.return_value = [
            {"name": "Triangle567"},
            {"name": "Square567"}
        ]

        # Mock response for: GET /repos/<id>/Triangle567/commits
        commits_triangle = Mock()
        commits_triangle.status_code = 200
        commits_triangle.json.return_value = [{}, {}, {}]  # 3 commits

        # Mock response for: GET /repos/<id>/Square567/commits
        commits_square = Mock()
        commits_square.status_code = 200
        commits_square.json.return_value = [{}, {}]  # 2 commits

        # requests.get will be called 3 times total
        mock_get.side_effect = [
            repos_response,
            commits_triangle,
            commits_square
        ]

        result = get_repo_commit_counts("fakeuser")

        self.assertEqual(result, [
            ("Triangle567", 3),
            ("Square567", 2)
        ])

        # Optional: verify number of API calls
        self.assertEqual(mock_get.call_count, 3)


if __name__ == "__main__":
    unittest.main()
