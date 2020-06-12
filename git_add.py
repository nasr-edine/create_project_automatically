import os
import sys

str = ' '.join(sys.argv[1:])
msgCommit = input("message: ")

print(f'git add {str}')
if not msgCommit:
    print(f'git commit -m "add files: {str}"')
else:
    print(f'git commit -m "add files: {msgCommit}"')


os.system(f'git add {str}')
os.system(f'git commit -m "add files {str}"')
if not msgCommit:
    os.system(f'git commit -m "add files: {str}"')
else:
    os.system(f'git commit -m "{msgCommit}"')
os.system('git push origin master')