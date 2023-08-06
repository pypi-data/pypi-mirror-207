#!/usr/bin/env python

"""Tests for `np_image_buffer` package."""

import numpy as np
from np_image_buffer import ImageBuffer

def test_read_full_buffer():
    
    shape = (100, 256, 256)
    data = np.random.randint(0, 256, size=shape, dtype=np.uint8)
    buffer = ImageBuffer(shape, dtype=np.uint8)
    
    buffer.extend(data)
    
    assert len(buffer) == shape[0]
    
    buffer.extend(data)
    readout = buffer.popall()
    
    assert len(readout) == shape[0]
    assert len(buffer) == 0
    
