import pytest
import graphics.rough_refraction_dispersion as mod

CASES = [
    ("roughness_lut_levels", (1,)),
    ("dispersion_world_scale", (1,)),
    ("refract_current_bg", (1,)),
    ("total_internal_reflect", (1,)),
    ("layer_by_depth", (1,)),
    ("stable_transparent_order", (1,)),
    ("load", (1,)),
    ("refract", (1,)),
    ("compose", (1,)),
    ("present", (1,)),
    ("validate_refraction", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
