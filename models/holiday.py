class FederalHoliday(AutoEnum):
  NewYear = "New Year's Day", 'absolute', Month.JANUARY, 1
  MLK = "Birthday of Martin Luther King, Jr.", 'relative', Month.JANUARY, Weekday.MONDAY, 3
  President = "Washington's Birthday", 'relative', Month.FEBRUARY, Weekday.MONDAY, 3
  Memorial = "Memorial Day", 'relative', Month.MAY, Weekday.MONDAY, 5
  Juneteenth = "Juneteenth National Independence Day", 'absolute', Month.JUNE, 19
  Independence = "Independence Day", 'absolute', Month.JULY, 4
  Labor = "Labor Day", 'relative', Month.SEPTEMBER, Weekday.MONDAY, 1
  Columbus = "Columbus Day", 'relative', Month.OCTOBER, Weekday.MONDAY, 2
  Veterans = "Veterans Day", 'relative', Month.NOVEMBER, 11, 1
  Thanksgiving = "Thanksgiving Day", 'relative', Month.NOVEMBER, Weekday.THURSDAY, 4
  Christmas = "Christmas Day", 'absolute', Month.DECEMBER, 25
  
  def __init__(self, doc, type, month, day, occurrence=None):
      self.__doc__ = doc
      self.type = type
      self.month = month
      self.day = day
      self.occurrence = occurrence
      
  def date(self, year):
      "returns the observed date of the holiday for `year`"
      if self.type == 'absolute' or isinstance(self.day, int):
          holiday =  Date(year, self.month, self.day)
          if Weekday(holiday.isoweekday()) is Weekday.SUNDAY:
              holiday = holiday.replace(delta_day=1)
          return holiday
      days_in_month = days_per_month(year)
      target_end = self.occurrence * 7 + 1
      if target_end > days_in_month[self.month]:
          target_end = days_in_month[self.month]
      target_start = target_end - 7
      target_week = list(xrange(start=Date(year, self.month, target_start), step=one_day, count=7))
      for holiday in target_week:
          if Weekday(holiday.isoweekday()) is self.day:
              return holiday
      
  @classmethod
  def year(cls, year):
      """
      Return a list of US Federal Holidays.
      """
      holidays = []
      for fh in cls:
          holidays.append(fh.date(year))
      return holidays   
