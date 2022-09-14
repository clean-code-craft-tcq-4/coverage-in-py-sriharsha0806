import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
  
  def test_classify_temperature_breach(self):
    self.assertTrue(classify_temperature_breach("PASSIVE_COOLING", 20) == "NORMAL")
    self.assertTrue(classify_temperature_breach("HI_ACTIVE_COOLING", -1) == "TOO_LOW")
    self.assertTrue(classify_temperature_breach("MED_ACTIVE_COOLING", 50) == "TOO_HIGH")
  
  def test_send_to_controller(self):
    self.assertionIsNone(send_to_controller("TOO_LOW"))
    
  def test_send_to_email(self):
    self.assertIsNone(send_to_email("TOO_LOW"))
    self.assertIsNone(send_to_email("TOO_HIGH"))
    
  def test_check_and_alert(self):
    self.assertIsNone(check_and_alert("TO_CONTROLLER", {"coolingType":"PASSIVE_COOLING"}, 20))
    self.assertIsNone(check_and_alert("TO_EMAIL", {"coolingType":"PASSIVE_COOLING"}, 20))


if __name__ == '__main__':
  unittest.main()
