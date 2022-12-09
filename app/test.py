import unittest

from .functions.clean.dataclean import DataClean

class TestdataClean(unittest.TestCase):
    def test_vp(self):
        """
        Test for the 'Vice President'  in the string
        """

        data = "Vice President of Supply Chain"
        should = {
            "test": data,
            "seniority": "VP",
            "functional": "Supply Chain"
        }

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)
    
    def test_director(self):
        """
        Test for the 'Director' in the string
        """

        data = "Director of Global Strategic Sourcing (IT)"
        should = {
            "test": data,
            "seniority": "Director",
            "functional": "Global Strategic Sourcing (IT)"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)
    
    def test_manager(self):
        """
        Test for the 'Manager' in the string
        """

        data = "General Manager Realty Supply Chain"
        should = {
            "test": data,
            "seniority": "Manager",
            "functional": "General"
        }

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)

    def test_manager_short(self):
        """
        Test for the 'Manager' in the string with abbreviated functional role
        """

        data = "Sr Manager - Sustainability, Product Regulatory Compliance & Social Responsibility"
        should = {
            "test": data,
            "seniority": "Manager",
            "functional": "Senior"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)

    def test_csuite(self):
        """
        Test for the 'C-Suite' in the string
        """

        data = "SVP, Chief Ethics & Compliance Officer - International"
        should = {
            "test": data,
            "seniority": "C-Suite",
            "functional": "Ethics & Compliance"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)

    def test_csuite(self):
        """
        Test for the 'Managing Director' in the string
        """

        data = "Managing Director, Supply Chain Technology"
        should = {
            "test": data,
            "seniority": "Director",
            "functional": "Executive"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)

    def test_ceo(self):
        """
        Test for the 'CEO' in the string
        """

        data = "CEO - Procurement, Supply Chain Systems, Process Excellence & Facilities"
        should = {
            "test": data,
            "seniority": "C-Suite",
            "functional": "Executive"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)

    def test_cofounder_1(self):
        """
        Test for the 'Co-Founder' in the string
        """

        data = "Co-Founder & Vice President Supply Chain, Joybirds"
        should = {
            "test": data,
            "seniority": "Owner",
            "functional": "Executive"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)
    
    def test_headof(self):
        """
        Test for the 'Head of' in the string
        """

        data = "Head of Supply Chain/Transportation Sourcing"
        should = {
            "test": data,
            "seniority": "Head of",
            "functional": "Supply Chain/Transportation Sourcing"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)
    
    def test_partner(self):
        """
        Test for the 'Head of' in the string
        """

        data = "Junior Partner, Global Supply Chain"
        should = {
            "test": data,
            "seniority": "Partner",
            "functional": "Junior"
        }   

        rules = DataClean.get_rules()
        result = DataClean.clean_functional_role(rules, data)

        self.assertEqual(result, should)
    
    
if __name__ == '__main__':
    unittest.main()