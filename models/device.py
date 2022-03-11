# Device Module

class Device(object):
  _id = int()
  _status = str()
  _name = str()
  _measurement = int()
  _patient_id = int()
  
  def set_id(self, num):
    self._id = num
    
  def get_id(self):
    return self._id
  
  def set_status(self, status):
    self._status = status
    
  def get_status(self):
    return self._status
  
  def set_name(self, name):
    self._name = name
    
  def get_name(self):
    return self._name
  
  def set_measurement(self, measurement):
    self._measurement = measurement
    
  def get_measurement(self):
    return self._measurement
  
  def set_patient_id(self, patient_id):
    self._patient_id = patient_id)
    
  def get_patient_id(self):
    return self._patient_id
  
  
