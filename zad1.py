class FizzBuzz:
    def game(self, x):
        if x % 15 == 0:
            return "FizzBuzz"
        elif x % 3 == 0:
            return "Fizz"
        elif x % 5 == 0:
            return "Buzz"
        else:
            return x

    def gameWithDocString(self, x):
        """
        # >>> f = FizzBuzz()
        >>> f.gameWithDocString(15)
        'FizzBuzz'
        >>> f.gameWithDocString(-30)
        'FizzBuzz'
        >>> f.gameWithDocString(3)
        'Fizz'
        >>> f.gameWithDocString(5)
        'Buzz'
        >>> f.gameWithDocString(7)
        7
        >>> f.gameWithDocString(-23)
        -23
        >>> f.gameWithDocString("11")
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 30, in <module>
            print(f.game("11"))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString(())
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game(()))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString([])
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game([]))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString({})
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game({}))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString(3.5)
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game(3.5))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString(None)
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game(None))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        >>> f.gameWithDocString(True)
        Traceback (most recent call last):
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 49, in <module>
            print(f.game(True))
          File "C:/Users/zosia/Desktop/uczelnia/testowanie/lab07/zad1.py", line 13, in game
            raise TypeError("Error")
        TypeError: Error
        """
        if type(x) is int:
            if x % 15 == 0:
                return "FizzBuzz"
            elif x % 3 == 0:
                return "Fizz"
            elif x % 5 == 0:
                return "Buzz"
            else:
                return x
        else:
            raise TypeError("Error")


if __name__ == "__main__":
    # print(FizzBuzz.gameWithDocString.__doc__)
    import doctest
    # doctest.testmod()
    doctest.testmod(extraglobs={'f': FizzBuzz()})
