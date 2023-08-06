import copy
import random
import pytest
from typing import Any

from bigraph_schema.parse import parse_type_parameters

NONE_SYMBOL = ''

required_schema_keys = (
    '_default',
    '_apply',
    '_serialize',
    '_deserialize',
)

optional_schema_keys = (
    '_type',
    '_value',
    '_divide',
    '_description',
    '_ports',
    '_type_parameters',
    '_super',
)

type_schema_keys = required_schema_keys + optional_schema_keys

overridable_schema_keys = (
    '_default',
    '_apply',
    '_serialize',
    '_deserialize',
    '_value',
    '_divide',
    '_description',
)

merge_schema_keys = (
    '_ports',
    '_type_parameters',
)

# check to see where are not adding in supertypes of types
# already present
concatenate_schema_keys = (
    '_super',
)


def type_merge(dct, merge_dct, path=tuple(), merge_supers=True):
    """Recursively merge type definitions, never overwrite.
    Args:
        dct: The dictionary to merge into. This dictionary is mutated
            and ends up being the merged dictionary.  If you want to
            keep dct you could call it like
            ``deep_merge_check(copy.deepcopy(dct), merge_dct)``.
        merge_dct: The dictionary to merge into ``dct``.
        path: If the ``dct`` is nested within a larger dictionary, the
            path to ``dct``. This is normally an empty tuple (the
            default) for the end user but is used for recursive calls.
    Returns:
        ``dct``
    """
    for k in merge_dct:
        if not k in dct or k in overridable_schema_keys:
            dct[k] = merge_dct[k]
        elif k in merge_schema_keys or isinstance(
            dct[k], dict
        ) and isinstance(
            merge_dct[k], collections.abc.Mapping
        ):
            type_merge(dct[k], merge_dct[k], path + (k,))
        elif k in concatenate_schema_keys:
            # this check may not be necessary if we check
            # for merging super types
            if k != '_super' or merge_supers:
                dct[k].extend(merge_dct[k])
        else:
            raise ValueError(
                f'cannot merge types at path {path + (k,)}: '
                f'{dct} overwrites {k} from {merge_dct}'
            )
            
    return dct


def deep_merge(dct, merge_dct):
    """ Recursive dict merge
    This mutates dct - the contents of merge_dct are added to dct (which is also returned).
    If you want to keep dct you could call it like deep_merge(copy.deepcopy(dct), merge_dct)
    """
    if dct is None:
        dct = {}
    if merge_dct is None:
        merge_dct = {}
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.abc.Mapping)):
            deep_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]
    return dct


class Registry(object):
    def __init__(self):
        """A Registry holds a collection of functions or objects."""
        self.registry = {}
        self.main_keys = set([])

    def register(self, key, item, alternate_keys=tuple(), force=False):
        """Add an item to the registry.

        Args:
            key: Item key.
            item: The item to add.
            alternate_keys: Additional keys under which to register the
                item. These keys will not be included in the list
                returned by ``Registry.list()``.

                This may be useful if you want to be able to look up an
                item in the registry under multiple keys.
        """
        keys = [key]
        keys.extend(alternate_keys)
        for registry_key in keys:
            if registry_key in self.registry and not force:
                if item != self.registry[registry_key]:
                    raise Exception(
                        'registry already contains an entry for {}: {} --> {}'.format(
                            registry_key, self.registry[key], item))
            else:
                self.registry[registry_key] = item
        self.main_keys.add(key)

    def register_multiple(self, schemas, force=False):
        for key, schema in schemas.items():
            self.register(key, schema, force=force)

    def access(self, key):
        """Get an item by key from the registry."""
        return self.registry.get(key)

    def list(self):
        return list(self.main_keys)

    def validate(self, item):
        return True


class TypeRegistry(Registry):

    def __init__(self):
        super().__init__()

        self.supers = {}
        self.register('any', {})


    def register(self, key, item, alternate_keys=tuple(), force=False):
        item = copy.deepcopy(item)
        if isinstance(item, dict):
            supers = item.get('_super', ['any']) # list of immediate supers
            if isinstance(supers, str):
                supers = [supers]
                item['_super'] = supers
            for su in supers:
                assert isinstance(
                    su, str), f"super for {key} must be a string, not {su}"
            self.supers[key] = supers
            for su in supers:
                su_type = self.registry.get(su, {})
                new_item = copy.deepcopy(su_type)
                item = type_merge(
                    new_item,
                    item,
                    merge_supers=False)

        super().register(key, item, alternate_keys, force)


    def resolve_parameters(self, qualified_type):
        type_name, parameter_types = qualified_type
        outer_type = self.registry.get(type_name)

        if outer_type is None:
            raise ValueError(f'type {qualified_type} is looking for type {type_name} but that is not in the registry')

        parameters = {}
        if '_type_parameters' in outer_type:
            parameter_names = outer_type['_type_parameters']
            resolved = [
                self.resolve_parameters(parameter_type)
                for parameter_type in parameter_types
            ]
            parameters = dict(zip(parameter_names, resolved))

        result = {
            '_type': type_name,
        }

        if parameters:
            result['_type_parameters'] = parameters

        return result


    def substitute_type(self, schema):
        if isinstance(schema, str):
            schema = self.access(schema)
            if schema is None:
                raise Exception(f'trying to substitute a type that is unrecognized {schema}')
        elif '_type' in schema:
            type_key = schema['_type']
            type_schema = copy.deepcopy(self.access(type_key))
            schema = deep_merge(type_schema, schema)

        return schema


    def expand_schema(self, schema):
        # make this only show the types at the leaves

        step = self.substitute_type(schema)
        for key, subschema in step.items():
            if key not in type_schema_keys:
                step[key] = self.expand_schema(subschema)
        return step
        

    def expand(self, schema):
        duplicate = copy.deepcopy(schema)
        return self.expand_schema(duplicate)


    def generate_default(self, schema):
        default = None

        if isinstance(schema, str):
            schema = self.access(schema)
        elif '_type' in schema:
            schema = self.substitute_type(schema)

        if '_default' in schema:
            if not '_deserialize' in schema:
                raise Exception(
                    f'asking for default for {type_key} but no deserialize in {schema}')
            deserialize = deserialize_registry.access(
                schema['_deserialize'])
            if '_type_parameters' in schema:
                default = deserialize(
                    schema['_default'],
                    schema['_type_parameters'])
            else:
                default = deserialize(
                    schema['_default'])
        else:
            default = {}
            for key, subschema in schema.items():
                if key not in type_schema_keys:
                    default[key] = self.generate_default(subschema)

        return default
        

    def generate_default_type(self, type_key):
        schema = self.access(type_key)
        return self.generate_default(schema)


    def access(self, key):
        """Get an item by key from the registry."""
        typ = self.registry.get(key)

        if typ is None:
            parse = parse_type_parameters(key)
            if parse[0] in self.registry:
                typ = self.resolve_parameters(parse)

        return typ


    def lookup(type_key, attribute):
        return self.access(type_key).get(attribute)


    # description should come from type
    def is_descendent(self, key, ancestor):
        for sup in self.supers.get(key, []):
            if sup == ancestor:
                return True
            else:
                found = self.is_descendent(sup, ancestor)
                if found:
                    return True
        return False


class RegistryRegistry(Registry):
    def type_attribute(self, type_key, attribute):
        type_registry = self.access('_type')
        type_value = type_registry.access(type_key)
        attribute_key = type_value.get(attribute)
        if attribute_key is not None:
            attribute_registry = self.access(attribute)
            return attribute_registry.access(attribute_key)


apply_registry = Registry()
serialize_registry = Registry()
deserialize_registry = Registry()
divide_registry = Registry()
type_registry = TypeRegistry()

registry_registry = RegistryRegistry()
registry_registry.register('_type', type_registry)
registry_registry.register('_apply', apply_registry)
registry_registry.register('_divide', divide_registry)
registry_registry.register('_serialize', serialize_registry)
registry_registry.register('_deserialize', deserialize_registry)


def apply_update(schema, state, update):
    # expects an expanded schema

    if '_apply' in schema:
        apply_function = apply_registry.access(schema['_apply'])
        if '_type_parameters' in schema:
            state = apply_function(state, update, schema['_type_parameters'])
        else:
            state = apply_function(state, update)
    elif isinstance(update, dict):
        for key, branch in update.items():
            if key not in schema:
                raise Exception(f'trying to update a key that is not in the schema {key} for state:\n{state}\nwith schema:\n{schema}')
            else:
                subupdate = apply_update(
                    schema[key],
                    state[key],
                    branch
                )

                state[key] = subupdate
    else:
        schema = type_registry.expand_schema(schema)
        state = apply_update(schema, state, update)

    return state


def apply(schema, initial, update):
    expanded = type_registry.expand(schema)
    state = copy.deepcopy(initial)
    return apply_update(expanded, initial, update)


def accumulate(current, update):
    return current + update

def concatenate(current, update):
    return current + update

def divide_float(value):
    half = value / 2.0
    return (half, half)

# support function types for registrys?
# def divide_int(value: int, _) -> tuple[int, int]:
def divide_int(value):
    half = value // 2
    other_half = half
    if value % 2 == 1:
        other_half += 1
    return half, other_half


# class DivideRegistry(Registry):
    

# def divide_longest(dimensions: Dimension) -> Tuple[Dimension, Dimension]:
def divide_longest(dimensions):
    # any way to declare the required keys for this function in the registry?
    # find a way to ask a function what type its domain and codomain are

    width = dimensions['width']
    height = dimensions['height']
    
    if width > height:
        a, b = divide_int(width)
        return [{'width': a, 'height': height}, {'width': b, 'height': height}]
    else:
        x, y = divide_int(height)
        return [{'width': width, 'height': x}, {'width': width, 'height': y}]


def divide_list(l, parameters):
    result = [[], []]
    divide_type = parameters[0]
    divide = registry_registry.type_attribute(divide_type, '_divide')

    for item in l:
        if isinstance(item, list):
            divisions = divide_list(item)
        else:
            divisions = divide(item)

        result[0].append(divisions[0])
        result[1].append(divisions[1])

    return result


def divide_dict(d, parameters):
    result = [{}, {}]
    # get the type of the values for this dict
    divide_type = parameters[0]
    divide = registry_registry.type_attribute(divide_type, '_divide')

    for key, value in d:
        if isinstance(value, dict):
            divisions = divide_dict(value)
        else:
            divisions = divide(value)

        result[0][key], result[1][key] = divisions

    return result


def replace(old_value, new_value):
    return new_value


# TODO: make these work
def serialize_dict(value, type_parameters):
    return value


def deserialize_dict(value, type_parameters):
    return value


def maybe_apply(current, update, type_parameters):
    if current is None or update is None:
        return update
    else:
        maybe_type = type_registry.access(parameters[0])
        return apply_update(maybe_type, current, update)


def maybe_divide(value, type_parameters):
    if value is None:
        return [None, None]
    else:
        pass


def maybe_serialize(value, type_parameters):
    if value is None:
        return NONE_SYMBOL
    else:
        maybe_type = type_registry.access(parameters[0])
        return serialize(maybe_type, value)


def maybe_deserialize(encoded, type_parameters):
    if encoded == NONE_SYMBOL:
        return None
    else:
        maybe_type = type_registry.access(parameters[0])
        return deserialize(maybe_type, encoded)


# validate the function registered is of the right type?
apply_registry.register('accumulate', accumulate)
apply_registry.register('concatenate', concatenate)
apply_registry.register('replace', replace)
apply_registry.register('merge', deep_merge)
apply_registry.register('maybe_apply', maybe_apply)

divide_registry.register('divide_float', divide_float)
divide_registry.register('divide_int', divide_int)
divide_registry.register('divide_longest', divide_longest)
divide_registry.register('divide_list', divide_list)
divide_registry.register('divide_dict', divide_dict)
divide_registry.register('maybe_divide', maybe_divide)

serialize_registry.register('str', str)
serialize_registry.register('serialize_dict', serialize_dict)
serialize_registry.register('maybe_serialize', maybe_serialize)

deserialize_registry.register('float', float)
deserialize_registry.register('int', int)
deserialize_registry.register('str', str)
deserialize_registry.register('eval', eval)
deserialize_registry.register('deserialize_dict', deserialize_dict)
deserialize_registry.register('maybe_deserialize', maybe_deserialize)

# if super type is re-registered, propagate changes to subtypes (?)

# remove shape types
type_library = {
    # abstract number type
    'number': {
        '_apply': 'accumulate',
        '_serialize': 'str',
        '_description': 'abstract base type for numbers',
    },

    'int': {
        '_default': '0',
        # inherit _apply and _serialize from number type
        '_deserialize': 'int',
        '_divide': 'divide_int',
        '_description': '64-bit integer',
        '_super': 'number',
    },

    'float': {
        '_default': '0.0',
        '_deserialize': 'float',
        '_divide': 'divide_float',
        '_description': '64-bit floating point precision number',
        '_super': 'number',
    }, 

    'string': {
        '_default': '',
        '_apply': 'replace',
        '_serialize': 'str',
        '_deserialize': 'str',
        '_divide': 'divide_int',
        '_description': '64-bit integer'
    },

    'list': {
        '_default': '[]',
        '_apply': 'concatenate',
        '_serialize': 'str',
        '_deserialize': 'eval',
        '_divide': 'divide_list',
        '_type_parameters': ['A'],
        '_description': 'general list type (or sublists)'
    },

    'tree': {
        '_default': '{}',
        '_apply': 'merge',
        '_serialize': 'str',
        '_deserialize': 'eval',
        '_divide': 'divide_dict',
        '_type_parameters': ['A'],
        '_description': 'mapping from str to some type (or nested dicts)'
    },

    'dict': {
        '_default': '{}',
        '_apply': 'merge',
        '_serialize': 'serialize_dict',
        '_deserialize': 'deserialize_dict',
        '_divide': 'divide_dict',
        '_type_parameters': ['key', 'value'],
        '_description': 'mapping from keys of any type to values of any type'
    },

    'maybe': {
        '_default': 'None',
        '_apply': 'maybe_apply',
        '_serialize': 'maybe_serialize',
        '_deserialize': 'maybe_deserialize',
        '_divide': 'maybe_divide',
        '_type_parameters': ['value'],
        '_description': 'type to represent values that could be empty'
    },

    'edge': {
        'wires': {
            '_type': 'tree[list[string]]'
        },
    },

    # 'process': {
    #     'process': {'_type': 'process instance'},
    #     'config': {'_type': 'dict'},
    #     '_super': 'edge',
    # },
}


type_registry.register_multiple(type_library)


supported_units = {
    'm/s': {
        '_default': 0.0,
        '_apply': 'accumulate',
        '_serialize': 'str',
        '_deserialize': 'float',
        '_divide': 'divide_float',
        '_description': 'meters per second'
    }
}


for key, units in supported_units.items():
    type_registry.register(key, units)


def schema_zoo():
    mitochondria_schema = {
        'mitochondria': {
            'volume': {'_type': 'float'},
            'membrane': {
                'surface_proteins': {'_type': 'branch[protein]'},
                'potential': {'_type': 'microvolts'}},
            'mass': {'_type': 'membrane?'},
        }
    }

    cytoplasm_schema = {
        'cytoplasm': {
            'mitochondria': {'_type': 'branch[mitochondria]'},
            'proteins': {'_type': 'branch[mitochondria]'},
            'nucleus': {'_type': 'branch[mitochondria]'},
            'transcripts': {'_type': 'branch[mitochondria]'},
        }
    }

    cell_schema = {
        'cell': {
            'shape': {'_type': 'mesh'},
            'volume': {'_type': 'mL'},
            'temperature': {'_type': 'K'},
        }
    }

    cell_composite = {
        'environment': {
            'outer_shape': {
                '_type': 'mesh', '_value': []},
            'cellA': {
                'cytoplasm': {
                    'external_ions': {'_type': 'ions'},
                    'internal_ions': {'_type': 'ions'},
                    'other_ions': {'_type': {
                        '_default': 0.0,
                        '_apply': accumulate,
                        '_serialize': str,
                        '_deserialize': float,
                        '_divide': divide_float,
                        '_description': '64-bit floating point precision number'
                    }},
                    'electron_transport': {
                        '_type': 'process',
                        '_value': 'ElectronTransport',
                        '_ports': {
                            'external_ions': 'ions',
                            'internal_ions': 'ions'},
                        '_wires': {
                            'external_ions': ['..', 'external_ions'],
                            'internal_ions': ['..', 'internal_ions']}
                        }
                    },
                'inner_shape': {'_type': 'mesh', '_value': []},
                '_ports': {
                    'shape': 'mesh',
                    'volume': 'mL',
                    'temperature': 'K'
                },
                '_channel': {
                    'shape': ['inner_shape'],
                },
                '_wires': {
                    'shape': ['..', 'outer_shape']
                }
            }
        }
    }

    compose({
        'cell': {
            'membrane': cell_schema,
            'cytoplasm': cytoplasm_schema
        }
    }, {
        
    })


def test_cube():
    cube_schema = {
        'shape': {},
        
        'rectangle': {
            'width': {'_type': 'int'},
            'height': {'_type': 'int'},
            '_divide': 'divide_longest',
            '_description': 'a two-dimensional value',
            '_super': 'shape',
        },
        
        # cannot override existing keys unless it is of a subtype
        'cube': {
            'depth': {'_type': 'int'},
            '_super': 'rectangle',
        },
    }

    type_registry.register_multiple(cube_schema)


def test_generate_default():
    int_default = type_registry.generate_default(
        {'_type': 'int'}
    )
    assert int_default == 0

    cube_default = type_registry.generate_default(
        {'_type': 'cube'})

    assert 'width' in cube_default
    assert 'height' in cube_default
    assert 'depth' in cube_default


def test_expand_schema():
    schema = {'_type': 'cube'}
    expanded = type_registry.expand(schema)

    assert len(schema) == 1
    assert 'height' in expanded


def test_reregister_type():
    with pytest.raises(Exception) as e:
        type_registry.register('int', type_library['string'])

    type_registry.register('int', type_library['string'], force=True)
    type_registry.register('int', type_library['int'], force=True)


def test_apply_update():
    schema = {'_type': 'cube'}
    state = {
        'width': 11,
        'height': 13,
        'depth': 44,
    }
    update = {
        'depth': -5
    }

    new_state = apply(
        schema,
        state,
        update
    )

    assert new_state['width'] == 11
    assert new_state['depth'] == 39


if __name__ == '__main__':
    test_cube()
    test_generate_default()
    test_expand_schema()
    test_reregister_type()
    test_apply_update()
