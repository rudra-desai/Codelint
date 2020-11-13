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
    result = subprocess.run(['./node_modules/.bin/eslint', '-f', 'html', f'./userfiles/{filename}'],
                            stdout=subprocess.PIPE)

    result = result.stdout.decode("utf-8")
    result = result.replace('style="display:none"', 'style="display:table-row"')
    result = re.sub(r'\[\+\].*.js', 'eslint', result)
    return {
        'linter': linter,
        'output': result,
        'filename': filename
    }

def pylint(linter, filename):
    ps = subprocess.Popen(('pylint', f'./userfiles/{filename}'), stdout=subprocess.PIPE)
    result = subprocess.check_output(('pylint-json2html'), stdin=ps.stdout).decode("utf-8")
    try:
        result = re.sub(r'<h2>Metrics<\/h2>(?s).*', '', result)
        result = re.sub(r'<h1>Pylint report from report.jinja2(?s).+?<\/h3>', '', result)
        result = re.sub(r'(<tr>(?s).+?<\/tr>)(?s).+?<td>1<\/td>(?s).+?Module name.+?<\/tr>', r'\g<1> ', result)
    except Exception as e:
        print(e)

    return {
        'linter': linter,
        'output': result,
        'filename': filename
    }
