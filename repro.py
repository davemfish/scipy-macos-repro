try:
	from packaging.tags import sys_tags
	_tags = list(sys_tags())
except ImportError as err:
	print(err)

import scipy._lib._testutils
print(scipy._lib._testutils.IS_MUSL)
