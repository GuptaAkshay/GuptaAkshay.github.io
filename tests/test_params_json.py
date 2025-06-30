import json
import pathlib

# Run with: pytest

def test_tagline_contains_enthusiast():
    params_path = pathlib.Path(__file__).resolve().parents[1] / 'params.json'
    with params_path.open() as f:
        data = json.load(f)
    assert 'Enthusiast' in data.get('tagline', '')
