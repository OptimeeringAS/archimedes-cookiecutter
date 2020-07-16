from cookiecutter.main import cookiecutter

create_examples = '{{cookiecutter.examples}}' == 'yes'

if create_examples:
  cookiecutter('https://git.optimeering.no/archimedes/archimedes-cookiecutter-examples.git',
             no_input=True,
             extra_context={'repo_name': 'examples'})
