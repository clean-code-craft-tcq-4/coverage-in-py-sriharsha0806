import unittest
import typewise_alert
from typewise_alert import classify_temperature_breach

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(120, 50, 100) == 'TOO_HIGH')
  
  def test_classify_temperature_breach(self):
    self.assertTrue(classify_temperature_breach("PASSIVE_COOLING", 20) == "NORMAL")
    self.assertTrue(classify_temperature_breach("PASSIVE_COOLING", -20) == "TOO_LOW")
    self.assertTrue(classify_temperature_breach("PASSIVE_COOLING", 50) == "TOO_HIGH")
    
  
  
  
 
  
    
  


if __name__ == '__main__':
  unittest.main()
