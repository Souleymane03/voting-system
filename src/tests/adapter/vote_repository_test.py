import unittest
from app.adapter.inmemory_vote_repository import InMemoryVoteRepository
from app.domain.vote import Vote


class MyTestCase(unittest.TestCase):
    def save_vote(self):
        vote = Vote()
        vote_repository = InMemoryVoteRepository()
        self.assertEqual(vote.save(vote_repository).vote_id, vote.vote_id)

    def test_vote_repository_all(self):
        vote_repository = InMemoryVoteRepository()
        vote_1 = Vote().save(vote_repository)
        vote_2 = Vote().save(vote_repository)
        self.assertSetEqual(vote_repository.all(), {vote_1, vote_2})

    def test_vote_repository_total(self):
        vote_repository = InMemoryVoteRepository()
        Vote().save(vote_repository)
        Vote().save(vote_repository)
        self.assertEqual(vote_repository.total(), 2)


if __name__ == '__main__':
    unittest.main()
