import unittest

# Function lineare_suche:
# Parameter:
#   liste: Array aus Elementen
#   wert:  Wert, nach dem in der Liste gesucht wird
# Result:
#   Index des 1. Treffers
#   oder -1, falls kein Treffer


def lineare_suche(liste, wert):
    pass

# Testcases


class TestLineareSuche(unittest.TestCase):
    def test_1(self):
        # Arrange
        liste = [1,2,3,4,5,6,7,8]
        wert = 4
        expected = 3

        # Act
        result = lineare_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)


# Run Tests
if __name__ == "__main__":
    unittest.main()
