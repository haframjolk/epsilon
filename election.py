import json


class Election:
    """Represents an election's current state"""
    def __init__(self, candidates: list[str], json_filename: str, max_candidates: int = 1):
        """Creates a new Election object with specified candidates (only allows voting for 1 candidate by default)"""
        self.__candidates = candidates
        self.__votes = {candidate: 0 for candidate in candidates}
        self.__votes["empty"] = 0
        self.__json_filename = json_filename
        self.__max_candidates = max_candidates

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

    def write_json(self):
        """Write current vote tally to JSON file"""
        with open(self.__json_filename, "w") as f:
            json.dump(self.__votes, f)

    def vote(self, candidates: set[str]):
        """Vote for specified candidates"""
        # Prevent voters from voting for more candidates than is allowed
        if len(candidates) > self.__max_candidates:
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
