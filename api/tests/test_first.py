from unittest import mock

def test_first(django_app_factory):
    #with mock.patch('canopusweb.utils.get_canvas_user', return_value=100): <-- DOESN'T WORK
    with mock.patch('canopusweb.urls.get_canvas_user', return_value=100):
        fac = django_app_factory()
        resp = fac.post('/test/')
    print('WOW')
    assert False


def test_second(django_app_factory):
    #with mock.patch('canopusweb.utils.get_canvas_user', return_value=200): <-- DOESN'T WORK
    with mock.patch('canopusweb.urls.get_canvas_user', return_value=200):
        fac = django_app_factory()
        resp = fac.post('/test/')
    print('WOW')
    assert False