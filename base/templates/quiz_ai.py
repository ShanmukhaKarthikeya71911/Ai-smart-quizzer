class SuggestionEngine:
    def _init_(self, progress):
        """
        progress should be a dictionary like:
        {
            "easy": {"attempts": int, "average": float},
            "medium": {"attempts": int, "average": float},
            "hard": {"attempts": int, "average": float}
        }
        """
        self.progress = progress

    def get_suggestion(self):
        if self.progress["easy"]["attempts"] >= 5 and self.progress["easy"]["average"] >= 80:
            return "You’re doing great! Try Medium level MCQs."

        elif self.progress["medium"]["attempts"] >= 5 and self.progress["medium"]["average"] >= 75:
            return "Awesome work! Try Hard level MCQs."

        elif self.progress["hard"]["attempts"] >= 3 and self.progress["hard"]["average"] >= 80:
            return "Excellent! Move on to the next topic."

        else:
            return "Keep practicing at your current level."