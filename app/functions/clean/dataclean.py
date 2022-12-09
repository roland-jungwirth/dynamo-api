import re

class DataClean:
    @staticmethod
    def clean_functional_role(rules, string_to_clean: str):
        for index, rule in enumerate(rules):
            search = re.search(rule['rule'], string_to_clean.strip(), re.IGNORECASE)
            
            if search:
                if (isinstance(rule['functional'], int)):
                    functional = DataClean.convert_abbreviations(search.group(rule['functional']))
                else:
                    functional = rule['functional']

                return {
                    "test": string_to_clean.strip(),
                    "seniority": rule['seniority'],
                    "functional": functional
                }
        return "Nothing found"

    @staticmethod
    def get_rules():
        # @todo: this needs to be stored in a database for easy manipulation
        return [
            {
                "name": "check for Vice President",
                "rule": r"\b(vice president|vp)\b( ?of |, )(.*)",
                "seniority": "VP",
                "functional": 3
            },
            {
                "name": "check for Managing Director",
                "rule": r"\b(managing director)\b",
                "seniority": "Director",
                "functional": "Executive"
            },
            {
                "name": "check for Director",
                "rule": r"\b(director|dir)\b( ?of |, )(.*)",
                "seniority": "Director",
                "functional": 3
            },
            {
                "name": "check for Manager",
                "rule": "([a-z]*) (manager)",
                "seniority": "Manager",
                "functional": 1
            },
            {
                "name": "check for C-Suite",
                "rule": "chief (.*) officer",
                "seniority": "C-Suite",
                "functional": 1
            },
            {
                "name": "check for CEO",
                "rule": r"\bceo\b",
                "seniority": "C-Suite",
                "functional": "Executive"
            },
            {
                "name": "check for Co-Founder",
                "rule": r"\b(co-founder|cofounder)\b",
                "seniority": "Owner",
                "functional": "Executive"
            },
            {
                "name": "check for Head of",
                "rule": r"\bhead of\b (.*)",
                "seniority": "Head of",
                "functional": 1
            },
            {
                "name": "check for Partner",
                "rule": r"\b([a-z]*) partner\b",
                "seniority": "Partner",
                "functional": 1
            }
        ]

    def convert_abbreviations(string_to_check):
        abbreviations = dict()
        abbreviations['jr'] = 'junior'
        abbreviations['sr'] = 'senior'

        if string_to_check.strip().lower() in abbreviations:
            return abbreviations[string_to_check.strip().lower()].capitalize()
        else:
            return string_to_check