from enum import Enum

 
class Case(Enum):
    HIT_MAX_ACC_HITS_MIN_ACC = 1
    DOESNT_HIT_MAX_ACC_HIT_MIN_ACC = 2
    HIT_MAX_ACC_DOESNT_HIT_MIN_ACC = 3
    DOESNT_HIT_MAX_ACC_DOESNT_HIT_MIN_ACC = 4


def get_fastest_case_nr(v0, v1, x, v_max, a_max, j_max):
	assert False  # Not yet implemented


def get_slowest_case_nr(v0, v1, x, v_max, a_max, j_max):
	assert False  # Not yet implemented


def mjuk(v0, v1, x, v_max, a_max, j_max, min_duration=None):
	assert j_max > 0
	assert a_max > 0
	assert v_max > 0

	assert x > 0

	v_min = 0.0
	a_min = -a_max
	j_min = -j_max

	assert v0 <= v_max
	assert v0 >= v_min

	assert v1 <= v_max
	assert v1 >= v_min

	if min_duration not is None:
		assert min_duration >= 0.0

	case_nr = get_slowest_case_nr(v0, v1, x, v_max, a_max, j_max)

	# Calc slowest_time
	if case_nr == Case.HIT_MAX_ACC_HITS_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.DOESNT_HIT_MAX_ACC_HIT_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.HIT_MAX_ACC_DOESNT_HIT_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.DOESNT_HIT_MAX_ACC_DOESNT_HIT_MIN_ACC:
		assert False  # Not yet implemented
	else:
		assert False

	if slowest_time > min_duration:
		return False

	case_nr = get_fastest_case_nr(v0, v1, x, v_max, a_max, j_max)

	# Calc fastest_time
	if case_nr == Case.HIT_MAX_ACC_HITS_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.DOESNT_HIT_MAX_ACC_HIT_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.HIT_MAX_ACC_DOESNT_HIT_MIN_ACC:
		assert False  # Not yet implemented
	elif case_nr == Case.DOESNT_HIT_MAX_ACC_DOESNT_HIT_MIN_ACC:
		assert False  # Not yet implemented
	else:
		assert False

	# TODO: Return the actual trajectory, too.
	return max(fastest_time, min_duration)
