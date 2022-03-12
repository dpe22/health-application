#original source for holiday tracking code https://stackoverflow.com/questions/22586895/python-enum-when-and-where-to-use
#modified by dpe22

from enum import Enum
from enum import auto as AutoEnum
from dbf import Date, xrange, days_per_month, one_day

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

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
  def next_20_business_days(cls, date, days=20):
      """
      Return the next 20 business days from date.
      """
      holidays = cls.year(date.year)
      years = set([date.year])
      while days > 0:
          date = date.replace(delta_day=1)
          if date.year not in years:
              holidays.extend(cls.year(date.year))
              years.add(date.year)
          if Weekday(date.isoweekday()) in (Weekday.SATURDAY, Weekday.SUNDAY) or date in holidays:
              continue
          days -= 1
      return date    
      
  @classmethod
  def year(cls, year):
      """
      Return a list of US Federal Holidays.
      """
      holidays = []
      for fh in cls:
          holidays.append(fh.date(year))
      return holidays   
