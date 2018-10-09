# -*- coding: utf-8 -*-
# Copyright (C) 2017 - 2018 Tim Hütz
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not,
# see <http://www.gnu.org/licenses/>.

from datetime import datetime

from tomaatti import TimerType, ConfigHelper


class Configuration(object):
	def __init__(self, configuration_parser=None):
		from os.path import expanduser, exists, join
		from os import makedirs
		from configparser import ConfigParser

		# ensure the root directory for the configuration files exist
		self._config_directory = expanduser('~/.config/tomaatti')
		if not exists(self._config_directory):
			makedirs(self._config_directory)

		# determine the name of some essential configuration files
		self._config_app_state = join(self._config_directory, 'application_state.ini')

		# if a configuration file exists, read it or use the injected configuration parser
		if configuration_parser:
			self._application_config = configuration_parser
		else:
			self._application_config = ConfigParser()
			self._create_initial_config()
		if exists(self._config_app_state):
			self._application_config.read(self._config_app_state)

	def _create_initial_config(self):
		# create the sections for the confiugration
		self._application_config.add_section('timer')
		self._application_config.add_section('periods')
		self._application_config.add_section('experimental')
		self._application_config.add_section('ui')

		# assign the default values to the configuration sections
		self._application_config.set('timer', 'mode', str(TimerType.WORKING))
		self._application_config.set('timer', 'is_running', ConfigHelper.bool_to_config_str(False))
		self._application_config.set('timer', 'end_time', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

		self._application_config.set('periods', 'working', '25')
		self._application_config.set('periods', 'break', '5')

		self._application_config.set('ui', 'fontawesome', ConfigHelper.bool_to_config_str(False))

		self._application_config.set('experimental', 'overlay', ConfigHelper.bool_to_config_str(False))
		self._application_config.set('experimental', 'blur', ConfigHelper.bool_to_config_str(False))

	def _persist_current_state(self) -> None:
		with open(self._config_app_state, 'w') as configfile:
			self._application_config.write(configfile)
