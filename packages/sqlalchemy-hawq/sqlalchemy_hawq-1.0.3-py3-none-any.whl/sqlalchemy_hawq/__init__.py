"""
Extends postgres dialect to support Apache HAWQ db ddl and dml.
"""

from sqlalchemy.dialects import registry as _registry
import pkg_resources


_registry.register('hawq', 'sqlalchemy_hawq.dialect', 'HawqDialect')
_registry.register('hawq.psycopg2', 'sqlalchemy_hawq.dialect', 'HawqDialect')


__version__ = pkg_resources.require('sqlalchemy_hawq')[0].version
