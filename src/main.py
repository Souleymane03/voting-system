from app.adapter.inmemory_vote_repository import InMemoryVoteRepository
from app.domain.vote import Vote



def main():
    """
    Main function that initializes an in-memory vote repository, saves two vote instances, prints all votes, and prints the total number of votes.
    """
    vote_repository = InMemoryVoteRepository()

    Vote().save(vote_repository)
    Vote().save(vote_repository)

    print(vote_repository.all())
    print(f'Total votes: {vote_repository.total()}')


if __name__ == '__main__':
    main()