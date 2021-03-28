import json


class Election:
    def __init__(self, candidates: list[str], multiple: bool):
        self.__candidates = candidates
        self.__votes = {candidate: 0 for candidate in candidates}
        self.__votes["empty"] = 0
        self.__multiple = multiple

    def write_json(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.__votes, f)

    def __vote(self, candidate: str):
        self.__votes[candidate] += 1

    def __empty_vote(self):
        self.__votes["empty"] += 1

    def __candidate_exists(self, candidate: str):
        return candidate in self.__candidates

    def vote(self, candidates: list[str]):
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
        return False

    def __str__(self):
        return str(self.__votes)
