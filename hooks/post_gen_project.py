import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_db_related(project_directory):
    """Removes everything related with database."""
    models_location = os.path.join(
        project_directory,
        'models.py'
    )
    os.remove(models_location)
    templates_location = os.path.join(
        project_directory,
        'templates'
    )
    shutil.rmtree(templates_location)


if '{{ cookiecutter.use_db }}'.lower() == 'n':
    remove_db_related(PROJECT_DIRECTORY)
