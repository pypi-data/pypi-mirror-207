"""
The entry point for the sqlalchemy test suite.

Command line args are added and the test collector
is modified to check them.
 """

from sqlalchemy.engine.url import URL
from sqlalchemy.dialects import registry
from sqlalchemy.testing import config
from sqlalchemy.testing.plugin import pytestplugin
from sqlalchemy.testing.plugin import plugin_base
from sqlalchemy.testing.plugin.pytestplugin import *
from sqlalchemy.testing.plugin.pytestplugin import (
    pytest,
    inspect,
)
from sqlalchemy.testing import asyncio

import os

registry.register('hawq.psycopg2', 'sqlalchemy_hawq.dialect', 'HawqDialect')
registry.register('hawq', 'sqlalchemy_hawq.dialect', 'HawqDialect')


def pytest_addoption(parser):
    """
    Adds custom args, then calls the sqlalchemy pytest_addoption method to handle the rest
    """
    parser.addoption(
        "--custom-only",
        action="store_true",
        default=False,
        help="run only sqlalchemy_hawq custom tests",
    )
    parser.addoption(
        "--unit-only",
        action="store_true",
        default=False,
        help="run only sqlalchemy_hawq custom unit tests",
    )
    parser.addoption(
        "--sqla-only", action="store_true", default=False, help="run only the sqlalchemy test suite"
    )
    parser.addoption(
        "--offline-only",
        action="store_true",
        default=False,
        help="run only the tests that don't require a live connection",
    )
    parser.addoption('--db-uri', default=os.environ.get('HAWQ_DB_URI'))
    parser.addoption(
        '--hawq-db-user',
        help='The username for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_USER'),
    )
    parser.addoption(
        '--hawq-db-pass',
        help='The password for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_PASS'),
    )
    parser.addoption(
        '--hawq-db-driver',
        help='The password for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_DRIVER'),
    )
    parser.addoption(
        '--hawq-db-port',
        help='The password for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_PORT'),
    )
    parser.addoption(
        '--hawq-db-host',
        help='The password for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_HOST'),
    )
    parser.addoption(
        '--hawq-db-name',
        help='The password for connecting to the hawq db',
        default=os.environ.get('HAWQ_DB_NAME'),
    )

    pytestplugin.pytest_addoption(parser)


def pytest_sessionstart(session):
    if plugin_base.options.offline_only:
        plugin_base.post_configure = [
            item for item in plugin_base.post_configure if item.__qualname__ != '_engine_uri'
        ]
        asyncio._assume_async(plugin_base.post_begin)

    else:
        if not plugin_base.options.dburi:
            urlArgs = dict(
                host=plugin_base.options.hawq_db_host,
                port=plugin_base.options.hawq_db_port,
                drivername=plugin_base.options.hawq_db_driver,
                database=plugin_base.options.hawq_db_name,
                username=plugin_base.options.hawq_db_user,
                password=plugin_base.options.hawq_db_pass,
            )
            dburl = URL.create(**urlArgs)
            plugin_base.options.dburi = [dburl]

        asyncio._assume_async(plugin_base.post_begin)


def pytest_collection_modifyitems(session, config, items):
    if plugin_base.options.offline_only:
        return
    pytestplugin.pytest_collection_modifyitems(session, config, items)


def pytest_pycollect_makeitem(collector, name, obj):
    """
    Decides which tests not to run, then passes the rest of the work to
    the sqla method with the same name
    """

    # if --offline_only, fixtures have not been initialized.
    # only run custom unit tests:
    if plugin_base.options.offline_only:
        if collector.name == 'test_suite.py':
            return []
        elif collector.name == 'test_live_connection.py':
            return []
        elif inspect.isclass(obj) and name.startswith('Test'):
            return pytest.Class.from_parent(collector, name=name)
        elif inspect.isfunction(obj) and name.startswith('test_'):
            return pytest.Function.from_parent(collector, name=name)
        else:
            return []

    if inspect.isclass(obj) and plugin_base.want_class(name, obj):
        # only run custom tests, not sqla_tests
        if config.options.custom_only:
            if collector.name == 'test_suite.py':
                return []

        # only run custom unit tests
        if config.options.unit_only:
            if collector.name == 'test_suite.py':
                return []
            if collector.name == 'test_live_connection.py':
                return []

        # only run the sqla test suite
        if config.options.sqla_only:
            if collector.name != 'test_suite.py':
                return []

    return pytestplugin.pytest_pycollect_makeitem(collector, name, obj)


def pytest_runtest_setup(item):
    if plugin_base.options.offline_only:
        return
    pytestplugin.pytest_runtest_setup(item)


def pytest_runtest_teardown(item, nextitem):
    if plugin_base.options.offline_only:
        return
    pytestplugin.pytest_runtest_teardown(item, nextitem)


def pytest_sessionfinish(session):
    if plugin_base.options.offline_only:
        return
    plugin_base.final_process_cleanup()
