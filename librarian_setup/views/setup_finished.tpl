<%inherit file='/base.tpl'/>

<%block name="title">
## Translators, used as page title
${_('Setup Completed')}
</%block>

<div class="setup-finished">
    <span class="all-ok"></span>
    <p class="main">${_('Settings are saved.')}</p>
    <p class="sub">${_('Welcome to outernet.')}</p>
    <a class="button confirm" href="${i18n_path('setup:exit')}?next=${i18n_url('/')}">${_('Start using Outernet')}</a>
</div>
