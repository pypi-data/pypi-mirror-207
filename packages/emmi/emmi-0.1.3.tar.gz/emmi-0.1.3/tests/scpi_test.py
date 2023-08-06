#!/usr/bin/python3

import pytest
from emmi import scpi


def test_MagicScpi():
    
    dev_port = 'ASRL2::INSTR'
    rm_sim = 'tests/pytest_dev.yaml@sim'
    device = scpi.MagicScpi(dev_port, resource_manager=rm_sim)
    
    assert device.dev.resource_name == dev_port    
    assert device.port == dev_port  
    assert device.id() == 'SCPI, PyTest'
    
    device.write("*IDN?")
    assert device.dev.read_bytes(4) == b'SCPI'
          
    # test error 
    with pytest.raises(KeyError) as e:
        getattr(*(scpi.MagicScpi()))
        assert str(e.value) == 'MAGICSCPI_ADDRESS'


# In class MockPropertyBranch() line 210 was changed:
# self._val = val --> self._val = args[0] 
def test_MockPropertyBranch():
    
    foo = scpi.MockPropertyBranch()
    
    assert foo._val == 3.14
    assert foo.__pcache() == 3.14

    foo.__pcache(1000)
    assert foo.__pcache() == 1000
    assert foo() == 3.14
  
    foo(2.72)
    assert foo() == 2.72
    assert foo._val == 2.72

    foo.enable()
    assert foo.set() == 1.0

    foo.disable()
    assert foo.set() == 0.0
    
    
# In class MockScpi() line 231 was changed:
# def id(): --> def id(self):   
def test_MockScpi(): 

    mock = scpi.MockScpi()

    assert mock.__pcache() == 3.14    
    assert mock.id() == "Mock SCPI Device"
