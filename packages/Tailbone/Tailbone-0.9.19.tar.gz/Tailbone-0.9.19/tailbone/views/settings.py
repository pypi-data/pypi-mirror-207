# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2023 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
Settings Views
"""

import os
import re
import subprocess
import sys
from collections import OrderedDict

import json

from rattail.db import model
from rattail.settings import Setting
from rattail.util import import_module_path

import colander

from tailbone import forms
from tailbone.db import Session
from tailbone.views import MasterView, View
from tailbone.util import get_libver, get_liburl


class AppInfoView(MasterView):
    """
    Master view for the overall app, to show/edit config etc.
    """
    route_prefix = 'appinfo'
    model_key = 'UNUSED'
    model_title = "UNUSED"
    model_title_plural = "App Details"
    creatable = False
    viewable = False
    editable = False
    deletable = False
    filterable = False
    pageable = False
    configurable = True

    grid_columns = [
        'name',
        'version',
        'editable_project_location',
    ]

    def get_index_title(self):
        return "{} for {}".format(self.get_model_title_plural(),
                                  self.rattail_config.app_title())

    def get_data(self, session=None):
        pip = os.path.join(sys.prefix, 'bin', 'pip')
        output = subprocess.check_output([pip, 'list', '--format=json'])
        data = json.loads(output.decode('utf_8').strip())

        for pkg in data:
            pkg.setdefault('editable_project_location', '')

        return data

    def configure_grid(self, g):
        super(AppInfoView, self).configure_grid(g)

        g.sorters['name'] = g.make_simple_sorter('name', foldcase=True)
        g.set_sort_defaults('name')
        g.set_searchable('name')

        g.sorters['version'] = g.make_simple_sorter('version', foldcase=True)

        g.sorters['editable_project_location'] = g.make_simple_sorter(
            'editable_project_location', foldcase=True)
        g.set_searchable('editable_project_location')

    def template_kwargs_index(self, **kwargs):
        kwargs = super(AppInfoView, self).template_kwargs_index(**kwargs)
        kwargs['configure_button_title'] = "Configure App"
        return kwargs

    def configure_get_context(self, **kwargs):
        context = super(AppInfoView, self).configure_get_context(**kwargs)

        weblibs = OrderedDict([
            ('vue', "Vue"),
            ('vue_resource', "vue-resource"),
            ('buefy', "Buefy"),
            ('buefy.css', "Buefy CSS"),
            ('fontawesome', "FontAwesome"),
        ])

        for key in weblibs:
            title = weblibs[key]
            weblibs[key] = {
                'key': key,
                'title': title,

                # nb. these values are exactly as configured, and are
                # used for editing the settings
                'configured_version': get_libver(self.request, key, fallback=False),
                'configured_url': get_liburl(self.request, key, fallback=False),

                # these are for informational purposes only
                'default_version': get_libver(self.request, key, default_only=True),
                'live_url': get_liburl(self.request, key),
            }

        context['weblibs'] = list(weblibs.values())
        return context

    def configure_get_simple_settings(self):
        return [

            # basics
            {'section': 'rattail',
             'option': 'app_title'},
            {'section': 'rattail',
             'option': 'node_type'},
            {'section': 'rattail',
             'option': 'node_title'},
            {'section': 'rattail',
             'option': 'production',
             'type': bool},
            {'section': 'rattail',
             'option': 'running_from_source',
             'type': bool},
            {'section': 'rattail',
             'option': 'running_from_source.rootpkg'},

            # display
            {'section': 'tailbone',
             'option': 'background_color'},

            # grids
            {'section': 'tailbone',
             'option': 'grid.default_pagesize',
             # TODO: seems like should enforce this, but validation is
             # not setup yet
             # 'type': int
            },

            # web libs
            {'section': 'tailbone',
             'option': 'libver.vue'},
            {'section': 'tailbone',
             'option': 'liburl.vue'},
            {'section': 'tailbone',
             'option': 'libver.vue_resource'},
            {'section': 'tailbone',
             'option': 'liburl.vue_resource'},
            {'section': 'tailbone',
             'option': 'libver.buefy'},
            {'section': 'tailbone',
             'option': 'liburl.buefy'},
            {'section': 'tailbone',
             'option': 'libver.buefy.css'},
            {'section': 'tailbone',
             'option': 'liburl.buefy.css'},
            {'section': 'tailbone',
             'option': 'libver.fontawesome'},
            {'section': 'tailbone',
             'option': 'liburl.fontawesome'},

            # nb. these are no longer used (deprecated), but we keep
            # them defined here so the tool auto-deletes them
            {'section': 'tailbone',
             'option': 'buefy_version'},
            {'section': 'tailbone',
             'option': 'vue_version'},

        ]


class SettingView(MasterView):
    """
    Master view for the settings model.
    """
    model_class = model.Setting
    model_title = "Raw Setting"
    model_title_plural = "Raw Settings"
    bulk_deletable = True
    feedback = re.compile(r'^rattail\.mail\.user_feedback\..*')

    grid_columns = [
        'name',
        'value',
    ]

    def configure_grid(self, g):
        super(SettingView, self).configure_grid(g)
        g.filters['name'].default_active = True
        g.filters['name'].default_verb = 'contains'
        g.set_sort_defaults('name')
        g.set_link('name')

    def configure_form(self, f):
        super(SettingView, self).configure_form(f)
        if self.creating:
            f.set_validator('name', self.unique_name)

    def unique_name(self, node, value):
        setting = self.Session.get(model.Setting, value)
        if setting:
            raise colander.Invalid(node, "Setting name must be unique")

    def editable_instance(self, setting):
        if self.rattail_config.demo():
            return not bool(self.feedback.match(setting.name))
        return True

    def after_edit(self, setting):
        # nb. force cache invalidation - normally this happens when a
        # setting is saved via app handler, but here that is being
        # bypassed and it is saved directly via standard ORM calls
        self.rattail_config.beaker_invalidate_setting(setting.name)

    def deletable_instance(self, setting):
        if self.rattail_config.demo():
            return not bool(self.feedback.match(setting.name))
        return True

    def delete_instance(self, setting):

        # nb. force cache invalidation
        self.rattail_config.beaker_invalidate_setting(setting.name)

        # otherwise delete like normal
        super(SettingView, self).delete_instance(setting)


# TODO: deprecate / remove this
SettingsView = SettingView


class AppSettingsForm(forms.Form):

    def get_label(self, key):
        return self.labels.get(key, key)


class AppSettingsView(View):
    """
    Core view which exposes "app settings" - aka. admin-friendly settings with
    descriptions and type-specific form controls etc.
    """

    def __call__(self):
        settings = sorted(self.iter_known_settings(),
                          key=lambda setting: (setting.group,
                                               setting.namespace,
                                               setting.name))
        groups = sorted(set([setting.group for setting in settings]))
        current_group = None

        form = self.make_form(settings)
        form.cancel_url = self.request.current_route_url()
        if form.validate(newstyle=True):
            self.save_form(form)
            group = self.request.POST.get('settings-group')
            if group is not None:
                self.request.session['appsettings.current_group'] = group
            self.request.session.flash("App Settings have been saved.")
            return self.redirect(self.request.current_route_url())

        if self.request.method == 'POST':
            current_group = self.request.POST.get('settings-group')

        if not current_group:
            current_group = self.request.session.get('appsettings.current_group')

        possible_config_options = sorted(
            self.request.registry.settings['tailbone_config_pages'],
            key=lambda p: p['label'])

        config_options = []
        for option in possible_config_options:
            perm = option.get('perm', option['route'])
            if self.request.has_perm(perm):
                option['url'] = self.request.route_url(option['route'])
                config_options.append(option)

        context = {
            'index_title': "App Settings",
            'form': form,
            'dform': form.make_deform_form(),
            'groups': groups,
            'settings': settings,
            'config_options': config_options,
        }
        context['buefy_data'] = self.get_buefy_data(form, groups, settings)
        # TODO: this seems hacky, and probably only needed if theme changes?
        if current_group == '(All)':
            current_group = ''
        context['current_group'] = current_group
        return context

    def get_buefy_data(self, form, groups, settings):
        dform = form.make_deform_form()
        grouped = dict([(label, [])
                        for label in groups])

        for setting in settings:
            field = dform[setting.node_name]
            s = {
                'field_name': field.name,
                'label': form.get_label(field.name),
                'data_type': setting.data_type.__name__,
                'choices': setting.choices,
                'helptext': form.render_helptext(field.name) if form.has_helptext(field.name) else None,
                'error': False, # nb. may set to True below
            }

            # we want the value from the form, i.e. in case of a POST
            # request with validation errors.  we also want to make
            # sure value is JSON-compatible, but we must represent it
            # as Python value here, and it will be JSON-encoded later.
            value = form.get_vuejs_model_value(field)
            value = json.loads(value)
            s['value'] = value

            # specify error / message if applicable
            # TODO: not entirely clear to me why some field errors are
            # represented differently?  presumably it depends on
            # whether Buefy is used by the theme.
            if field.error:
                s['error'] = True
                if isinstance(field.error, colander.Invalid):
                    s['error_messages'] = [field.errormsg]
                else:
                    s['error_messages'] = field.error_messages()

            grouped[setting.group].append(s)

        data = []
        for label in groups:
            group = {'label': label, 'settings': grouped[label]}
            data.append(group)

        return data

    def make_form(self, known_settings):
        schema = colander.MappingSchema()
        helptext = {}
        for setting in known_settings:
            kwargs = {
                'name': setting.node_name,
                'default': self.get_setting_value(setting),
            }
            if kwargs['default'] is None or kwargs['default'] == '':
                kwargs['default'] = colander.null
            if not setting.required:
                kwargs['missing'] = colander.null
            if setting.choices:
                kwargs['validator'] = colander.OneOf(setting.choices)
                kwargs['widget'] = forms.widgets.JQuerySelectWidget(
                    values=[(val, val) for val in setting.choices])
            schema.add(colander.SchemaNode(self.get_node_type(setting), **kwargs))
            helptext[setting.node_name] = setting.__doc__.strip()
        return AppSettingsForm(schema=schema, request=self.request, helptext=helptext)

    def get_node_type(self, setting):
        if setting.data_type is bool:
            return colander.Bool()
        elif setting.data_type is int:
            return colander.Integer()
        return colander.String()

    def save_form(self, form):
        for setting in self.iter_known_settings():
            value = form.validated[setting.node_name]
            if value is colander.null:
                value = ''
            self.save_setting_value(setting, value)

    def iter_known_settings(self):
        """
        Iterate over all known settings.
        """
        modules = self.rattail_config.getlist('rattail', 'settings')
        if modules:
            core_only = False
        else:
            modules = ['rattail.settings']
            core_only = True

        for module in modules:
            module = import_module_path(module)
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, type) and issubclass(obj, Setting) and obj is not Setting:
                    if core_only and not obj.core:
                        continue
                    # NOTE: we set this here, and reference it elsewhere
                    obj.node_name = self.get_node_name(obj)
                    yield obj

    def get_node_name(self, setting):
        return '[{}] {}'.format(setting.namespace, setting.name)

    def get_setting_value(self, setting):
        if setting.data_type is bool:
            return self.rattail_config.getbool(setting.namespace, setting.name)
        if setting.data_type is list:
            return '\n'.join(
                self.rattail_config.getlist(setting.namespace, setting.name,
                                            default=[]))
        return self.rattail_config.get(setting.namespace, setting.name)

    def save_setting_value(self, setting, value):
        existing = self.get_setting_value(setting)
        if existing != value:
            legacy_name = '{}.{}'.format(setting.namespace, setting.name)
            if setting.data_type is bool:
                value = 'true' if value else 'false'
            elif setting.data_type is list:
                entries = [self.clean_list_entry(entry)
                           for entry in value.split('\n')]
                value = ', '.join(entries)
            else:
                value = str(value)
            app = self.get_rattail_app()
            app.save_setting(Session(), legacy_name, value)

    def clean_list_entry(self, value):
        value = value.strip()
        if '"' in value and "'" in value:
            raise NotImplementedError("don't know how to handle escaping 2 "
                                      "different types of quotes!")
        if '"' in value:
            return "'{}'".format(value)
        if "'" in value:
            return '"{}"'.format(value)
        return value

    @classmethod
    def defaults(cls, config):
        config.add_route('appsettings', '/settings/app/')
        config.add_view(cls, route_name='appsettings',
                        renderer='/appsettings.mako',
                        permission='settings.edit')


def defaults(config, **kwargs):
    base = globals()

    AppInfoView = kwargs.get('AppInfoView', base['AppInfoView'])
    AppInfoView.defaults(config)

    AppSettingsView = kwargs.get('AppSettingsView', base['AppSettingsView'])
    AppSettingsView.defaults(config)

    SettingView = kwargs.get('SettingView', base['SettingView'])
    SettingView.defaults(config)


def includeme(config):
    defaults(config)
