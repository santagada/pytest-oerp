py.test plugin for testing OpenERP modules

Usage
-----

install/update via::

    pip install -U pytest-oerp

and to run tests type::

    py.test --oerp-server-path=<path to openerp server directory> \
            --oerp-db=<db name, default is test>

this will load OpenERP using the config on ``~/.openerp_serverrc`` and create a pool and transaction for the choosen database for the testcases where you receive an ``oerp`` attribute.

Writting tests
--------------

Testcases only need to receive ``oerp`` to create a transaction on oerp an example follows::

    def test_simple(oerp):
        product_obj = oerp.pool.get('product.product')
        product_ids = product_obj.search(oerp.cr, 1, [])

this will be run inside OpenERP like code in modules and you can use the full openerp api. You can only load stuff from OpenERP library inside functions, because the library is added to sys.path dynamically.

OpenERP API
-----------

As pytest-oerp is running inside OpenERP everything you need to do that can be done inside a module can be done in a pytest-oerp test. The usual ``cr``, ``uid`` attributes are ``oerp.cr`` and ``1`` (that means the first user, usually admin). ``oerp`` also has a ``pool`` attribute that is useful.

Todo
----

There are a lot of polish and features that should be done but a tentative list would be:

- support passing a configuration to OpenERP
- more tests (always a good thing)
- don't depend on mock (great lib but probably unnecessary for this)
- redirect print log
- addini in pytest so you can configure with pytest.ini
- lettuce support, but this will probably go in another package


Notes
-----

The official repository of this plugin is at http://github.com/santagada/pytest-oerp

For more info on py.test see http://pytest.org

All work on the plugin has been sponsored by PROGE (http://www.proge.com.br)
