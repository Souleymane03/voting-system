import unittest
import uuid

from app.domain.vote import Vote


class MyTestCase(unittest.TestCase):

    def test_vote_existing_vote_id(self):
        vote_id = str(uuid.uuid4())
        self.assertEqual(Vote(vote_id).vote_id, vote_id)

    def test_vote_defaults(self):
        vote_id = str(uuid.uuid4())
        self.assertNotEqual(Vote().vote_id, vote_id)


if __name__ == '__main__':
    unittest.main()
