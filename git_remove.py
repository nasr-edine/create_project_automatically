import os
import sys

str = ' '.join(sys.argv[1:])


print(f'git rm {str}')
print(f'git commit -m "remove {str}"')

os.system(f'git rm {str}')
os.system(f'git commit -m "remove {str}"')
os.system('git push origin master')