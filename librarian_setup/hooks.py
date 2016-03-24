import importlib

from .setup import Setup, SetupWizard
from .steps import setup_language, setup_language_form, is_language_invalid


def component_member_loaded(supervisor, member, config):
    mod_path = '{0}.setup'.format(member['pkg_name'])
    try:
        importlib.import_module(mod_path)  # they autoregister themselves
    except ImportError:
        pass  # no setup wizard steps in this component


def initialize(supervisor):
    # install app-wide access to setup parameters
    supervisor.exts.setup = Setup(supervisor)
    setup_wizard = SetupWizard(name='setup')
    supervisor.exts.setup_wizard = setup_wizard
    setup_wizard.register('language',
                          setup_language_form,
                          template='setup/step_language.tpl',
                          method='GET',
                          index=1,
                          test=is_language_invalid)
    setup_wizard.register('language',
                          setup_language,
                          template='setup/step_language.tpl',
                          method='POST',
                          index=1,
                          test=is_language_invalid)
