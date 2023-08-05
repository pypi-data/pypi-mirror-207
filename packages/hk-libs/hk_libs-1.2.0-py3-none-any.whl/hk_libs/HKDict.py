from copy import deepcopy
from collections import deque

class HKDict:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            assert type(key) in [int, str], f"invalid key type {type(key)} : only int, str are available"
            self.__dict__[key] = self._deep_convert(value)
    
    def _deep_convert(self, value):
        # Note:
        # _deep_convert() makes new copy for for collections(list, dict, set, etc.),
        # so it can cause memory explosion.
        if isinstance(value, dict):
            return HKDict.from_dict(value)
        elif isinstance(value, list):
            return [self._deep_convert(x) for x in value]
        elif isinstance(value, tuple):
            return tuple(self._deep_convert(x) for x in value)
        elif isinstance(value, set):
            return {self._deep_convert(x) for x in value}
        elif isinstance(value, frozenset):
            return frozenset(self._deep_convert(x) for x in value)
        elif isinstance(value, deque):
            return deque(self._deep_convert(x) for x in value)
        else:
            return value
    
    def to_dict(self):
        def _convert(value):
            if isinstance(value, HKDict):
                return value.to_dict()
            elif isinstance(value, list):
                return [_convert(x) for x in value]
            elif isinstance(value, tuple):
                return tuple(_convert(x) for x in value)
            elif isinstance(value, set):
                return {_convert(x) for x in value}
            elif isinstance(value, frozenset):
                return frozenset(_convert(x) for x in value)
            elif isinstance(value, deque):
                return deque(_convert(x) for x in value)
            else:
                return value
            
        return {key: _convert(value) for key, value in self.__dict__.items()}

    @classmethod
    def from_dict(cls, input):
        assert type(input) == dict, f"invalid input type {type(input)}: only dict is available"
        return cls(**input)
    
    # for attribute access
    def __getattr__(self, key):
        # Note:
        # Python calls __getattr__() only when key not exists in self.__dict__, so it is not necessary to check key existance.
        # But I put it for __getitem__() method, which calls __getattr__() method.
        return self.__dict__[key] if key in self.__dict__ else None
    
    def __setattr__(self, key, value):
        assert type(key) in [int, str], f"invalid key type {type(key)} : only int, str are available"
        self.__dict__[key] = self._deep_convert(value)
    
    def __delattr__(self, key):
        del self.__dict__[key]

    # for item access
    def __getitem__(self, key):
        return self.__getattr__(key)
    
    def __setitem__(self, key, value):
        self.__setattr__(key, value)
        
    def __delitem__(self, key):
        self.__delattr__(key)
    
    # for print
    def __repr__(self):
        dict_str = [ repr(key) + ": " + repr(value) for key, value in self.__dict__.items() ]
        return "{" + ', '.join(dict_str) + "}"
    
    def __str__(self):
        return self.__repr__()
    
    # for comparison
    def __len__(self):
        return len(self.__dict__)
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # for pickle
    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, state):
        self.__dict__.update(state)

    # for iteration
    def __iter__(self):
        return iter(self.__dict__)
    
    # for existence check
    def __contains__(self, key):
        return key in self.__dict__
    
    # for copy
    def __copy__(self):
        # Note:
        # HKDict does not support shallow copy because of its deep copy nature.
        # so __copy__() is same as __deepcopy__().
        return self.__deepcopy__(None)

    def __deepcopy__(self, memo):
        new_HKDict = HKDict()
        for key, value in self.__dict__.items():
            new_HKDict[key] = deepcopy(value, memo)
        return new_HKDict
    
    # for operator overridings
    def __add__(self, other):
        assert type(other) in [HKDict, dict], f"invalid type {type(other)}: only HKDict, dict are available"
        if isinstance(other, dict):
            other = HKDict.from_dict(other)
        return HKDict.from_dict({**self.__dict__, **other.__dict__})
    
    def __iadd__(self, other):
        assert type(other) in [HKDict, dict], f"invalid type {type(other)}: only HKDict, dict are available"
        if isinstance(other, dict):
            other = HKDict.from_dict(other)
        self.__dict__ = {**self.__dict__, **other.__dict__}
        return self
    
    def __sub__(self, other):
        assert type(other) in [HKDict, dict], f"invalid type {type(other)}: only HKDict, dict are available"
        if isinstance(other, dict):
            other = HKDict.from_dict(other)
        return HKDict.from_dict({key: value for key, value in self.__dict__.items() if key not in other.__dict__})
    
    def __isub__(self, other):
        assert type(other) in [HKDict, dict], f"invalid type {type(other)}: only HKDict, dict are available"
        if isinstance(other, dict):
            other = HKDict.from_dict(other)
        self.__dict__ = {key: value for key, value in self.__dict__.items() if key not in other.__dict__}
        return self

    @staticmethod
    def add(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        return a + b
    
    @staticmethod
    def sub(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        return a - b
    
    # for element-wise operation
    @staticmethod
    def elem_add(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        
        assert all([type(value) in [int, float] for value in a.values()]), f"invalid type {type(a)}: only int, float are available"
        assert all([type(value) in [int, float] for value in b.values()]), f"invalid type {type(b)}: only int, float are available"
        
        assert a.keys() == b.keys(), f"keys of a and b must be same"

        return HKDict.from_dict({key: a[key] + b[key] for key in a.keys()})
    
    @staticmethod
    def elem_sub(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        
        assert all([type(value) in [int, float] for value in a.values()]), f"invalid type {type(a)}: only int, float are available"
        assert all([type(value) in [int, float] for value in b.values()]), f"invalid type {type(b)}: only int, float are available"

        assert a.keys() == b.keys(), f"keys of a and b must be same"
        
        return HKDict.from_dict({key: a[key] - b[key] for key in a.keys()})
    
    @staticmethod
    def elem_mul(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        
        assert all([type(value) in [int, float] for value in a.values()]), f"invalid type {type(a)}: only int, float are available"
        assert all([type(value) in [int, float] for value in b.values()]), f"invalid type {type(b)}: only int, float are available"

        assert a.keys() == b.keys(), f"keys of a and b must be same"

        return HKDict.from_dict({key: a[key] * b[key] for key in a.keys()})
    
    @staticmethod
    def elem_div(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"
        
        assert all([type(value) in [int, float] for value in a.values()]), f"invalid type {type(a)}: only int, float are available"
        assert all([type(value) in [int, float] for value in b.values()]), f"invalid type {type(b)}: only int, float are available"
        
        assert a.keys() == b.keys(), f"keys of a and b must be same"
        assert all([value != 0 for value in b.values()]), f"invalid value in b: cannot divide by zero"

        return HKDict.from_dict({key: a[key] / b[key] for key in a.keys()})
    
    @staticmethod
    def elem_quot(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"

        assert all([type(value) in [int] for value in a.values()]), f"invalid type {type(a)}: only int is available"
        assert all([type(value) in [int] for value in b.values()]), f"invalid type {type(b)}: only int is available"

        assert a.keys() == b.keys(), f"keys of a and b must be same"
        assert all([value != 0 for value in b.values()]), f"invalid value in b: cannot divide by zero"

        return HKDict.from_dict({key: a[key] // b[key] for key in a.keys()})
    
    @staticmethod
    def elem_mod(a, b):
        assert type(a) in [HKDict, dict], f"invalid type {type(a)}: only HKDict, dict are available"
        assert type(b) in [HKDict, dict], f"invalid type {type(b)}: only HKDict, dict are available"

        assert all([type(value) in [int] for value in a.values()]), f"invalid type {type(a)}: only int is available"
        assert all([type(value) in [int] for value in b.values()]), f"invalid type {type(b)}: only int is available"

        assert a.keys() == b.keys(), f"keys of a and b must be same"
        assert all([value != 0 for value in b.values()]), f"invalid value in b: cannot divide by zero"

        return HKDict.from_dict({key: a[key] % b[key] for key in a.keys()})

    # for dict-like methods
    def keys(self):
        return self.__dict__.keys()
    
    def values(self):
        return self.__dict__.values()
    
    def items(self):
        return self.__dict__.items()
    
    def get(self, key, default=None):
        return self.__dict__.get(key, default)
    
    def pop(self, key, default=None):
        return self.__dict__.pop(key, default)
    
    def popitem(self):
        return self.__dict__.popitem()
    
    def clear(self):
        self.__dict__.clear()

    def update(self, other):
        return self.__iadd__(other)

    def setdefault(self, key, default=None):
        return self.__dict__.setdefault(key, default)
    
    def copy(self):
        return self.__copy__()
    
    def deepcopy(self):
        return self.__deepcopy__(None)
    