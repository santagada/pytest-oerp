e60 = {'company': u'OpenERP S.A.',
       'company_count': 1}

e61 = {'company': u'Your Company',
       'company_count': 3}

example_data = {'6.0': e60,
                '6.1': e61}


def test_browse(oerp):
    assert oerp.pool.get('res.company').browse(oerp.cr, 1, 1).name == example_data[oerp.major_version]['company']


def test_search(oerp):
    assert len(oerp.pool.get('res.company').search(oerp.cr, 1, [])) == example_data[oerp.major_version]['company_count']


def test_write(oerp):
    company = oerp.pool.get('res.company')
    company_ids = list(company.search(oerp.cr, 1, []))
    assert len(company_ids) == example_data[oerp.major_version]['company_count']
    vals = {'name': u'Test Company'}
    res = company.create(oerp.cr, 1, vals)
    company_ids.append(res)
    assert sorted(company.search(oerp.cr, 1, [])) == sorted(company_ids)
    assert company.browse(oerp.cr, 1, res).name == u'Test Company'
