import subprocess
import io
import sys
import runpy
from os import path

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists("lib/app.py"))

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path("lib/app.py")

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please."
        '''
        # Capture the output of the script
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path("lib/app.py")
        sys.stdout = sys.__stdout__

        # Check if the expected string is in the captured output
        assert captured_out.getvalue().strip() == "Hello World! Pass this test, please."

if __name__ == "__main__":
    pytest.main()
