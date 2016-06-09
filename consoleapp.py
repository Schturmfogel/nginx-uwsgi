#~*~ coding: utf-8 ~*~
import dnuconfig.settings
from dnuconfig.dnuconfig import DNUConfig

YES = 'Yes'
NO = 'No'


if __name__ == '__main__':
    config = DNUConfig()
    config.set_domain(raw_input('Domain (site address): '))
    uses_virtualenv = False
    VIRTUALENV_DIR = None
    if (raw_input('Do You using virtealenv? y/n: ').lower() in ['y', 'yes']):
        config.set_virtualenv(uses=True, directory=raw_input('Path to virtualenv: '))

    config.set_django_settings_module(
        module=raw_input('Define django settings module [settings]: '.format(dnuconfig.settings.DJANGO_SETTINGS_MODULE)))

    config.set_module_to_run(raw_input('Define module to run [{}]'.format(dnuconfig.settings.MODULE_TO_RUN)))
    config.set_project_dir(directory=raw_input('Define project directory: '))
    config.set_app_name(raw_input('Define main application name (where is the wsgi module): '))
