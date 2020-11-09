import subprocess
import os
import re

# get the current script path.
here = os.path.dirname(os.path.realpath(__file__))
subdir = "userfiles"

def lint_code(data):
    linter = data['linter']
    code = data['code']
    filename = data['uuid'] + ('.py' if linter == 'pylint' else '.js')

    filepath = os.path.join(here, subdir, filename)
    file = open(filepath, "w")
    file.write(code)
    file.close()

    if linter == 'eslint':
        return eslint(linter, filename)
    elif linter == 'pylint':
        return pylint(linter, filename)

def eslint(linter, filename):
    result = subprocess.run([linter, '-f', 'html', f'./userfiles/{filename}'],
                            stdout=subprocess.PIPE).stdout.decode("utf-8")

    result = result.replace('style="display:none"', 'style="display:table-row"')
    result = re.sub(r'\[\+\].*.js', 'eslint', result)
    return {
        'linter': linter,
        'output': result,
        'filename': filename
    }

def pylint(linter, filename):
    print(linter)