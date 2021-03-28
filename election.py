import json


class Election:
    """Represents an election's current state"""
    def __init__(self, candidates: list[str], multiple: bool = False):
        """Creates a new Election object with specified candidates (multiple votes disallowed by default)"""
        self.__candidates = candidates
        self.__votes = {candidate: 0 for candidate in candidates}
        self.__votes["empty"] = 0
        self.__multiple = multiple

    def __vote(self, candidate: str):
        """Registers a vote for candidate"""
        self.__votes[candidate] += 1

    def __empty_vote(self):
        """Registers an empty vote"""
        self.__votes["empty"] += 1

    def __candidate_exists(self, candidate: str):
        """Returns True if candidate exists in election, False otherwise"""
        return candidate in self.__candidates

    def __str__(self):
        """Represents the current election state as a string"""
        return str(self.__votes)

    def write_json(self, filename: str):
        """Write current vote tally to JSON file"""
        with open(filename, "w") as f:
            json.dump(self.__votes, f)

    def vote(self, candidates: list[str]):
        """Vote for specified candidates"""
        # Prevent multiple votes in single-vote elections
        if not self.__multiple and len(candidates) > 1:
            return False

        # If no candidates are selected, register an empty vote
        if not candidates:
            self.__empty_vote()
            return True

        # If all candidates exist, vote for every one
        if all(self.__candidate_exists(candidate) for candidate in candidates):
            for candidate in candidates:
                self.__vote(candidate)
            return True

        # If voting fails
        return False
