import unittest

# Function binaere_suche:
# Parameter:
#   liste: Array aus Elementen
#   wert:  Wert, nach dem in der Liste gesucht wird
# Result:
#   Index des 1. Treffers
#   oder -1, falls kein Treffer


def binaere_suche(liste, wert):
    links = 0
    rechts = len(liste) - 1
    while links <= rechts:
        mitte = (rechts-links) // 2
        if liste[mitte] == wert:
            return mitte
        if liste[mitte] < wert:
            links = mitte + 1
        else:
            rechts = mitte - 1
    return -1

# Testcases


class TestLineareSuche(unittest.TestCase):
    def test_0(self):
        # Arrange
        liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        wert = 'H'
        expected = 7

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_1(self):
        # Arrange
        liste = [1, 2, 3, 4, 5, 6, 7, 8]
        wert = 4
        expected = 3

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_2(self):
        # Arrange
        liste = [1, 2, 3, 4, 5, 6, 7, 8]
        wert = 9
        expected = -1

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_3(self):
        # Arrange
        liste = [2, 3, 1, 5, 8, 6, 7, 4]
        liste.sort()
        wert = 1
        expected = liste.index(wert)

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_4(self):
        # Arrange
        liste = []
        wert = 1
        expected = -1

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)

    def test_5(self):
        # Arrange
        liste = range(0, 200000001)
        wert = 200000000
        expected = 200000000

        # Act
        result = binaere_suche(liste, wert)

        # Assert
        self.assertEqual(result, expected)


# Run Tests
if __name__ == "__main__":
    unittest.main()
