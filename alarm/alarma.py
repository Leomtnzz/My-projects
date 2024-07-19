#le digo una hora a la que quiero que me diga 'wake up' y que sepa la hora que es.

from datetime import time

hora_actual=str(datetime.datetime.now())
print(hora_actual)

horas=('1','2','3','4','5','6','7','8','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')

horas=str(20, 29)
if hora_actual in horas:
    print('Wake up!')
else:
    print('You\'re good')


# from datetime import time, tzinfo, timedelta
# class TZ1(tzinfo):
#      def utcoffset(self, dt):
#          return timedelta(hours=1)
#      def dst(self, dt):
#          return timedelta(0)
#      def tzname(self,dt):
#          return "+01:00"
#      def  __repr__(self):
#          return f"{self.__class__.__name__}()"

# t = time(12, 10, 30, tzinfo=TZ1())
# t
# datetime.time(12, 10, 30, tzinfo=TZ1())
# t.isoformat()
# '12:10:30+01:00'
# t.dst()
# datetime.timedelta(0)
# t.tzname()
# '+01:00'
# t.strftime("%H:%M:%S %Z")
# '12:10:30 +01:00'
# 'The {} is {:%H:%M}.'.format("time", t)
# 'The time is 12:10.'
# print(t)