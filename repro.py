import scipy._lib._testutils
print('scipy import okay')

try:
    from packaging.tags import sys_tags
    _tags = list(sys_tags())  # raises ValueError
except ImportError as err:
    print(err)

print(0)
