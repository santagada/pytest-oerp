py.test plugin for testing OpenERP modules

Usage
-----

install/update via::

    easy_install -U pytest-oerp # or preferably
    pip install -U pytest-oerp

and then type::

    py.test --oerp-server-path=<path to openerp server/bin directory>

to load OpenERP. You will need to have openerp configured and a test
database (if it is not named test pass --oerp-db with the name). look
at the examples for more information.

Todo
----

Tons of stuff but a tentative list would be:

- have a simplified openerp api (eg. oerp['res.company'].search(1) )
- more tests (always a good thing)
- don't depend on mock (great lib but probably unnecessary for this)
- redirect logger
- only load openerp if a test needs it
- addini in pytest so you can configure with pytest.ini
- lettuce support, but this will probably go in another package
- make openerp better (that is always our idea)

Notes
-----

The repository of this plugin is at http://github.com/santagada/pytest-oerp

For more info on py.test see http://pytest.org
