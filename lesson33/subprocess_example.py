import subprocess

result = subprocess.run(['python', 'thread_example.py'], shell=True, capture_output=True, text=True)
print(result.stdout)