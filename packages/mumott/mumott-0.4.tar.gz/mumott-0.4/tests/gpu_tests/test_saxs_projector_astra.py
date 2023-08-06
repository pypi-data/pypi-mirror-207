import pytest
import numpy as np

from mumott.methods.projectors.saxs_projector_astra import SAXSProjectorAstra as SAXSProjectorAstra
from mumott.data_handling import DataContainer

dc = DataContainer('tests/test_half_circle.h5')
gm = dc.geometry

fields = [np.array(((0.2, 0.1)*64)).reshape(4, 4, 4, 2)]

projs = [np.array(
             [[[[0.8, 0.4],
              [0.8, 0.4],
              [0.8, 0.4],
              [0.8, 0.4]],
              [[0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4]],
              [[0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4]],
              [[0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4],
               [0.8, 0.4]]]])]

adjs = [np.array([[[[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]]],
                  [[[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]]],
                  [[[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]]],
                  [[[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]],
                   [[0.8, 0.4], [0.8, 0.4], [0.8, 0.4], [0.8, 0.4]]]])]


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, projs)])
def test_forward(field, proj):
    pr = SAXSProjectorAstra(gm)
    assert np.allclose(proj, pr.forward(field), rtol=1, atol=0.1)


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_adj(proj, adj):
    pr = SAXSProjectorAstra(gm)
    assert np.allclose(adj, pr.adjoint(proj), rtol=1, atol=0.1)


def test_str():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorAstra(dc.geometry)
    string = str(pr)
    assert '3c1566' in string


def test_html():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorAstra(dc.geometry)
    html = pr._repr_html_()
    assert '3c1566' in html


if __name__ == '__main__':

    test_forward(fields[0], projs[0])
    test_adj(projs[0], adjs[0])
    test_str()
    test_html()
