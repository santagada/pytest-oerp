
def test_browse(oerp):
    assert oerp.pool.get('res.company').browse(oerp.cr, 1, 1).name == u'OpenERP S.A.'

def test_search(oerp):
    assert len(oerp.pool.get('res.company').search(oerp.cr, 1, [])) == 1

def test_write(oerp):
    company = oerp.pool.get('res.company')
    assert len(company.search(oerp.cr, 1, [])) == 1
    vals = {'name': u'Test Company'}
    res = company.create(oerp.cr, 1, vals)
    assert company.search(oerp.cr, 1, []) == [1, res]
    assert company.browse(oerp.cr, 1, res).name == u'Test Company'





