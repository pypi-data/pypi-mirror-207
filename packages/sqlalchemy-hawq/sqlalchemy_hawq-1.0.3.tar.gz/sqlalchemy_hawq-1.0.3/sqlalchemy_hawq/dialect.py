""" Customizes the postgresql.psycopg2 dialect to work with Hawq. """

from sqlalchemy.dialects import postgresql
from sqlalchemy import schema
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import Delete
from sqlalchemy.sql.schema import Table


from .ddl import HawqDDLCompiler


class HawqDialect(postgresql.psycopg2.PGDialect_psycopg2):
    '''
    Main dialect class. Used by the engine to compile sql
    '''

    construct_arguments = [
        (
            schema.Table,
            {
                'partition_by': None,
                'inherits': None,
                'distributed_by': None,
                'bucketnum': None,
                'appendonly': None,
                'orientation': None,
                'compresstype': None,
                'compresslevel': None,
                'on_commit': None,
                'tablespace': None,
            },
        )
    ]
    ddl_compiler = HawqDDLCompiler
    name = 'hawq'
    supports_statement_cache = False

    def initialize(self, connection):
        """
        Override implicit_returning = True of postgresql dialect
        """
        super().initialize(connection)

        self.implicit_returning = False
        self.supports_native_uuid = False
        self.update_returning = False
        self.delete_returning = False
        self.insert_returning = False
        self.update_returning_multifrom = False
        self.delete_returning_multifrom = False

    @compiles(Delete, 'hawq')
    def visit_delete_statement(element, compiler, **kwargs):  # pylint: disable=no-self-argument
        """
        Allows a version of the delete statement to get compiled - the version
        that is effectively the same as truncate.

        Any filters on the delete statement result in an Exception.
        """
        delete_stmt_table = compiler.process(element.table, asfrom=True, **kwargs)
        filters_tuple = element.get_children()
        if not filters_tuple:
            return 'TRUNCATE TABLE {}'.format(delete_stmt_table)
        items = [item for item in element.get_children()]

        # check if filters_tuple contains only one item, and it's the table
        if (
            len(items) == 1
            and isinstance(items[0], Table)
            and compiler.process(items[0], asfrom=True, **kwargs) == delete_stmt_table
        ):
            return 'TRUNCATE TABLE {}'.format(delete_stmt_table)

        raise NotImplementedError('Delete statement with filter clauses not implemented for Hawq')

    def get_isolation_level_values(self, dbapi_conn):
        # note the generic dialect doesn't have AUTOCOMMIT, however
        # all postgresql dialects should include AUTOCOMMIT.
        # NB hawq doesn't support REPEATABLE READ
        return (
            "AUTOCOMMIT",
            "SERIALIZABLE",
            "READ UNCOMMITTED",
            "READ COMMITTED",
        )
