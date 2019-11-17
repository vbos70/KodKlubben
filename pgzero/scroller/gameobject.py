class GameObject:

    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __getitem__(self, k):
        return self.__dict__[k]

    def __setitem__(self, k, v):
        self.__dict__[k] = v

    def __delitem__(self, k):
        del self.__dict__[k]

    def __len__(self):
        return len(self.__dict__)
    
    def __iter__(self):
        return iter(self.__dict__)

    def keys(self):
        return self.__dict__.keys()


if __name__ == '__main__':

    alphabet = { chr(ord('a') + i) : i for i in range(26) }

    go1 = GameObject()
    go2 = GameObject(**alphabet)

    assert len(go1) == 0
    assert len(go2) == len(alphabet)
    assert len([e for e in go1]) == 0

    assert 'A' not in go1
    assert 'a' not in go1
    for ch in alphabet:
        assert ch not in go1
        assert ch in go2
    
    assert go2.a == 0
    assert go2.b == 1
    assert go2['c'] == 2

    del go2.a
    try:
        assert go2.a == 0
    except AttributeError as ae:
        print('Expected exception: {ae}: {s}'.format(ae=str(ae.__class__.__name__), s=str(ae)))

