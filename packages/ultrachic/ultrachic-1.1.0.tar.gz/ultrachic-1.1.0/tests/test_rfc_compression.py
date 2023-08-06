import pytest
import threading
import random

def _notifcb(self,msg):
    print("notification: {}".format(msg))

@pytest.fixture(scope="module")
def connectedUltraChic():
    import ultrachic
    return ultrachic.UltraChic.UltraChic(_notifcb)

@pytest.mark.functional
def test_full_sequence(connectedUltraChic):
    from ultrachic import UltraPackets
    
    connectedUltraChic.reset()
    for tv in UltraPackets.TVS:
        resp = connectedUltraChic.tv_load(tv["bytes"])
        assert(resp['num_bytes']==17)
    for (i,rulerow) in enumerate(UltraPackets.RULEROWS):
        resp = connectedUltraChic.rulerow_load(rulerow)
        assert(resp['num_rulerows']==i+1)
    for (i,rule) in enumerate(UltraPackets.RULES):
        resp = connectedUltraChic.rule_load(rule)
        assert(resp['num_rules']==i+1)
    resp = connectedUltraChic.footprint()
    assert(resp['num_bytes']==117)
    for packet in UltraPackets.PACKETS:
        resp = connectedUltraChic.packet_compress(packet['decompressed'])
        assert(resp['compressed']==packet['compressed'])
