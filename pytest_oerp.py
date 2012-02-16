import sys
import os.path as p
from optparse import OptionParser

from mock import patch
import pytest


def pytest_addoption(parser):
    parser.addoption("--oerp-db",
                     action="store",
                     default="test",
                     dest="oerp_dbname")
    parser.addoption("--oerp-server-path",
                     action="store",
                     dest="oerp_server_path")


def pytest_funcarg__oerp(request):
    if request.config.oerp_db:
        oerp = OpenERP(request.config.oerp_db,
                       request.config.oerp_pool,
                       request.config.oerp_major)
        request.addfinalizer(oerp.rollback)
        return oerp
    else:
        pytest.skip('No OpenERP server path set')


class NoArgsParser(OptionParser):
    '''An OptionParser that don't parse args'''
    def _get_args(self, args):
        if args is None:
            # here it would try to read sys.args, which we don't want
            return []
        else:
            return args[:]


def pytest_configure(config):
    if config.option.oerp_server_path:
        server_path = p.abspath(p.expanduser(config.option.oerp_server_path))
        if p.exists(p.join(server_path, 'openerp')):
            # this is an OpenERP 6.1 or earlier:
            sys.path.insert(0, server_path)
            import openerp
            import openerp.tools.config as c
            import openerp.release as release
            from openerp import pooler
            c.parse_config()
        else:
            # OpenERP 6.0
            sys.path.insert(0, p.join(server_path, 'bin'))
            # We need to import the modules from OpenERP in the correct order
            with patch('optparse.OptionParser', NoArgsParser) as optmock:
                import netsvc  # somehow this will build the config object
                import pooler  # needed to open the database
                import workflow  # without workflow nothing works
                import release
        db, pool = pooler.get_db_and_pool(config.option.oerp_dbname,
                                          update_module=False,
                                          pooljobs=False)
        config.oerp_db = db
        config.oerp_pool = pool
        config.oerp_major = release.major_version


class OpenERP(object):
    def __init__(self, db, pool, major_version):
        self.pool = pool
        # probably messing around with db will break things
        self._db = db
        self.cr = db.cursor()
        self.major_version = major_version

    def rollback(self):
        self.cr.rollback()
        # this might be necessary, but only OpenERP guys might know why
        # self.pool.get('ir.cron')._poolJobs(db.dbname)
        self.cr.close()
