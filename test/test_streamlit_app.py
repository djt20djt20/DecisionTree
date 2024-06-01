import unittest
from app.utils import add_numbers

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

import unittest
import subprocess
import time
import requests
import psutil

class TestStreamlitApp(unittest.TestCase):
    
    @classmethod
    def terminate_process_using_port(cls, port):
        for proc in psutil.process_iter(['pid', 'name', 'connections']):
            try:
                for conn in proc.info['connections'] or []:
                    if conn.laddr.port == 8501:
                        print(f"Port 8501 is in use by process {proc.info['name']} (PID {proc.info['pid']})")
                        proc.kill()
                        try:
                            proc.wait(timeout=5)  # Wait up to 5 seconds for the process to terminate
                            print('Terminated process')
                        except psutil.TimeoutExpired:
                            print(f"Process {proc.info['name']} (PID {proc.info['pid']}) did not terminate in time")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                print(f"Could not terminate process {proc.info['name']} (PID {proc.info['pid']}): {e}")

    @classmethod
    def setUpClass(cls):
        cls.terminate_process_using_port(8501) 
        cls.process = subprocess.Popen(['streamlit', 'run', 'app/streamlit_app.py', '--server.port=8501'])
        time.sleep(10)
    
    @classmethod
    def tearDownClass(cls):
        cls.process.terminate()
        cls.process.wait()

    def test_app_starts(self):
        # Check if the app is running on port 8501
        try:
            response = requests.get('http://localhost:8501')
            self.assertEqual(response.status_code, 200, "Streamlit app did not start successfully")
        except requests.ConnectionError:
            self.fail("Failed to connect to the Streamlit app")