# Imput Output Tables to Brazil IOTBR

Generate **I O - T A B L E** IOTBR.

## Instructions

1. Install:

```
pip install iotbr
```

2. Generate an aesthetic ASCII visual:

```python3
from iotbr import tru as tru

# import data from [2010] with level [68] about [Total product - PT]
tru.read_var('2010','68','PT')
# import data from [2010] with level [68] about [Total product - PT] with last year prices [t-1]
tru.read_var('2010','68','t-1')
```

