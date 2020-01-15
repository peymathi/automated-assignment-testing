import subprocess
import io

args = ['python', 'test.py']
process = subprocess.run(args, input="2\n2\n", universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="UTF-8")
result = process.stdout
print(result)
# processResponse = process.communicate(input="2 \n")
# print(processResponse[0])
# #process.terminate()