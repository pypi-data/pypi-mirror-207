## Utils for Intel® Integrated Performance Primitives
```python
from ipp_utils import interpolation, rfft

with interpolation(...) as ret:
    print(ret)

with rfft(...) as ret:
    print(ret)
```