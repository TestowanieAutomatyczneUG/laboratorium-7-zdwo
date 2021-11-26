import string
import unittest


class ValidPassword:
    def psw(self, x):
        up = 0
        sp = 0
        numb = 0
        ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        special = string.punctuation
        if type(x) is str:
            if len(x) >= 8:
                for i in x:
                    if i.isupper():
                        up += 1
                    if i in special:
                        sp += 1
                    if i in ints:
                        numb += 1
                if up >= 1 and sp >= 1 and numb >= 1:
                    return True
                else:
                    return False
            else:
                return False
        else:
            raise TypeError("Error")


v = ValidPassword().psw

class ValidatePasswordTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(v("Aaaaa!1a"))

    def test_true_long(self):
        self.assertTrue(v("HgyUutb76-&^%&57GVFMKHCUmkcd"))

    def test_true_special(self):
        self.assertTrue(v("#%*%54&%%fbret$$@C"))

    def test_true_short(self):
        self.assertTrue(v("AbcD10$#"))

    def test_true_ints(self):
        self.assertTrue(v("bB&83856726564258dvdsD"))

    def test_true_only_numbs(self):
        self.assertFalse(v("73274164865618562"))

    def test_true_empty(self):
        self.assertFalse(v(""))

    def test_false_too_short(self):
        self.assertFalse(v("aA!1aaa"))

    def test_false_wo_int(self):
        self.assertFalse(v("aA!aaaaa"))

    def test_false_wo_sp(self):
        self.assertFalse(v("aA11aaaa"))

    def test_false_wo_upp(self):
        self.assertFalse(v("aa!1aaaa"))

    def test_false_only_letters(self):
        self.assertFalse(v("abshtray"))

    def test_false_only_numbers(self):
        self.assertFalse(v("12345678"))

    def test_false_only_specials(self):
        self.assertFalse(v("!@#$%^&*"))

    def test_exc_int(self):
        self.assertRaises(TypeError, v, 123)

    def test_exc_tup(self):
        self.assertRaises(TypeError, v, -2)

    def test_exc_arr(self):
        self.assertRaises(TypeError, v, 2.5)

    def test_exc_arr_numb(self):
        self.assertRaises(TypeError, v, [])

    def test_exc_dict(self):
        self.assertRaises(TypeError, v, {})

    def test_exc_flo(self):
        self.assertRaises(TypeError, v, ())

    def test_exc_bool(self):
        self.assertRaises(TypeError, v, False)

    def test_exc_none(self):
        self.assertRaises(TypeError, v, None)

if __name__ == "__main__":
    unittest.main()
