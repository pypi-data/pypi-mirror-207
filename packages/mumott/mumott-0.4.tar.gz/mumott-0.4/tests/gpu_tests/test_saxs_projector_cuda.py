import pytest
import numpy as np

from numba import cuda

from mumott.methods.projectors.saxs_projector_cuda import SAXSProjectorCUDA
from mumott.data_handling import DataContainer
from mumott.data_handling.geometry import GeometryTuple

dc = DataContainer('tests/test_half_circle.h5')
gm = dc.geometry
gm.rotations[0] = np.eye(3)

gm_tuples = [GeometryTuple(rotation=np.eye(3), j_offset=0.2, k_offset=0.5),
             GeometryTuple(rotation=np.eye(3)[[2, 0, 1]], j_offset=0.2453, k_offset=0.5222),
             GeometryTuple(rotation=np.eye(3)[[1, 0, 2]], j_offset=-0.2453, k_offset=0.2)]

gm_hash_table = ['277106', '902494', '161751']

kernel_hash = ['222572', '167889', '185810']

fields = [np.arange(192, dtype=np.float32).reshape(4, 4, 4, 3)]
test_projs = [np.array([[[[174., 178., 182.],
                         [186., 190., 194.],
                         [198., 202., 206.],
                         [204., 208., 212.]],
                        [[366., 370., 374.],
                         [378., 382., 386.],
                         [390., 394., 398.],
                         [396., 400., 404.]],
                        [[558., 562., 566.],
                         [570., 574., 578.],
                         [582., 586., 590.],
                         [588., 592., 596.]],
                        [[654., 658., 662.],
                         [666., 670., 674.],
                         [678., 682., 686.],
                         [684., 688., 692.]]]])]

adjs = [np.arange(48)]
projs = [np.arange(48, dtype=np.float32).reshape(1, 4, 4, 3)]


@pytest.mark.parametrize('gm_tuple, expected_value', [(g, h) for g, h in zip(gm_tuples, gm_hash_table)])
def test_gm_hash(gm_tuple, expected_value):
    dc = DataContainer('tests/test_half_circle.h5')
    geom = dc.geometry
    pr = SAXSProjectorCUDA(geom)
    geom[0] = gm_tuple
    assert pr.is_dirty
    pr._update()
    assert expected_value == str(pr._geometry_hash)[:6]


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, test_projs)])
def test_forward(field, proj):
    pr = SAXSProjectorCUDA(gm)
    p = pr.forward(field)
    assert np.allclose(proj, p)


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, test_projs)])
def test_forward_subset(field, proj):
    dc = DataContainer('tests/test_half_circle.h5')
    geo = dc.geometry
    geo.rotations[0] = np.eye(3)
    geo.append(geo[0])
    pr = SAXSProjectorCUDA(geo)
    p = pr.forward(field, indices=0)
    assert np.allclose(proj, p)
    with pytest.raises(TypeError, match='integer kind'):
        pr.forward(field, indices=np.array('abc'))


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_adj(proj, adj):
    pr = SAXSProjectorCUDA(gm)
    a = pr.adjoint(proj)
    assert np.allclose(adj, a[:, 0].ravel())


@pytest.mark.parametrize('field, proj', [f for f in zip(fields, test_projs)])
def test_device_forward(field, proj):
    pr = SAXSProjectorCUDA(gm)
    p = pr.forward(cuda.to_device(field))
    assert np.allclose(proj, p.copy_to_host())


@pytest.mark.parametrize('proj, adj', [f for f in zip(projs, adjs)])
def test_device_adj(proj, adj):
    pr = SAXSProjectorCUDA(gm)
    a = pr.adjoint(cuda.to_device(proj))
    print(a)
    assert np.allclose(adj, a.copy_to_host()[:, 0].ravel())


def test_str():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorCUDA(dc.geometry)
    string = str(pr)
    assert '11291c' in string


def test_html():
    dc = DataContainer('tests/test_half_circle.h5')
    pr = SAXSProjectorCUDA(dc.geometry)
    html = pr._repr_html_()
    assert '11291c' in html
