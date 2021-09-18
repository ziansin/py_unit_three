import unittest
import egg

class MyTestCase(unittest.TestCase):
    def test_egg(self):
        import sys
        from io import StringIO

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            output = out.getvalue().strip()
            assert output == "_______" + "\n" + " /       \\\n" + "/         \\\n" + "\\         /\n" + " \\_______/\n" + \
                   "-\"-'-\"-'-\"-\n" + "  _______\n" + " /       \\\n" + "/         \\\n" + "\\         /\n" + " \\_______/\n" + \
                   "-\"-'-\"-'-\"-\n" + "\\         /\n" + " \\_______/\n" + "  _______\n" + " /       \\\n" + "/         \\\n" + \
                   "-\"-'-\"-'-\"-\n" + "\\         /\n" + " \\_______/"
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
