import string

class ValidPassword:

    def validateWithDocString(self, x):
        """
        >>> v = ValidPassword()
        >>> v.validateWithDocString("Aaaaa!1a")
        True
        >>> v.validateWithDocString("HgyUutb76-&^%&57GVFMKHCUmkcd")
        True
        >>> v.validateWithDocString("#%*%54&%%fbret$$@C")
        True
        >>> v.validateWithDocString("AbcD10$#")
        True
        >>> v.validateWithDocString("bB&83856726564258dvdsD")
        True
        >>> v.validateWithDocString("73274164865618562")
        False
        >>> v.validateWithDocString("")
        False
        >>> v.validateWithDocString("aA!1aaa")
        False
        >>> v.validateWithDocString("aA!aaaaa")
        False
        >>> v.validateWithDocString("aA11aaaa")
        False
        >>> v.validateWithDocString("aa!1aaaa")
        False
        >>> v.validateWithDocString("abshtray")
        False
        >>> v.validateWithDocString("12345678")
        False
        >>> v.validateWithDocString("!@#$%^&*")
        False
        >>> v.validateWithDocString(123)
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(123))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString(-2)
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(-2))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString(2.5)
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(2.5))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString({})
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString({}))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString([])
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString([]))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString(())
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(()))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString(None)
        Traceback (most recent call last):
          File "CC:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(None))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        >>> v.validateWithDocString(False)
        Traceback (most recent call last):
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 66, in <module>
            print(v.validateWithDocString(False))
          File "C:/Users/zosia/testowanie/lab07/zad2/zad2_doctest.py", line 61, in validateWithDocString
            raise TypeError("Error")
        TypeError: Error
        """
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

if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'v': ValidPassword()})