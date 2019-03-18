from record import Record


def test__init__():
    rec = Record()
    assert isinstance(rec.record, dict)
    assert len(rec.record) == 8
    assert not rec.record["u"]
    assert not rec.record["d"]
    assert not rec.record["l"]
    assert not rec.record["r"]
    assert not rec.record["ul"]
    assert not rec.record["ur"]
    assert not rec.record["dl"]
    assert not rec.record["dr"]


def test_update():
    rec = Record()
    rec.update("u", 1)
    rec.update("d", 2)
    rec.update("l", 3)
    rec.update("r", 4)
    rec.update("ul", 5)
    rec.update("ur", 6)
    rec.update("dl", 7)
    rec.update("dr", 8)
    assert rec.record["u"] == 1
    assert rec.record["d"] == 2
    assert rec.record["l"] == 3
    assert rec.record["r"] == 4
    assert rec.record["ul"] == 5
    assert rec.record["ur"] == 6
    assert rec.record["dl"] == 7
    assert rec.record["dr"] == 8
