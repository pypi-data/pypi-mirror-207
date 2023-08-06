# Screeny
A simple python library for working with screens and images.

## Installation

```sh
pip install screeny
```

## Usage

```python
from screeny import Screeny

sc = Screeny()
img = sc.take_screenshot()
```

## API-Reference

* screeny.take_screenshot
* screeny.get_mouse_pos


### screeny.take_screenshot(rect: QRect = None)

Takes a screenshot of the complete monitor or a given area as "rect".

### get_mouse_pos()
        
Returns the current position of the mouse as a tuple of xy-coordinates.
