# Unit Testing file
import unittest as ut
import raw_transform as rt

test_raw = rt.f_open()


rets = rt.data_transform(test_raw)


rt.f_save(rets)