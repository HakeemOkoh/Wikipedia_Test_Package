import unittest
from WIKIFramework.tests.test_Landing import LandingPageTest


lp = unittest.TestLoader().loadTestsFromTestCase(LandingPageTest)

regressionTest = unittest.TestSuite([lp])

unittest.TextTestRunner(verbosity=1).run(regressionTest)
