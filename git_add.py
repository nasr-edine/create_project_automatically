import os
import sys

str = ' '.join(sys.argv[1:])


print(f'git add {str}')
print(f'git commit -m "add files: {str}"')

os.system(f'git add {str}')
os.system(f'git commit -m "add files {str}"')
os.system('git push origin master')