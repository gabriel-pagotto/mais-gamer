import pytz
from datetime import datetime, timedelta
from pytz import timezone

def DatePost(date_before):
    date_now = datetime_sao_paulo()

    date_init = datetime(year=date_before.year, month=date_before.month, day=date_before.day)
    date_final = datetime(year=date_now.year, month=date_now.month, day=date_now.day, hour=date_now.hour)
    difference_date = (date_final - date_init)

    if difference_date.days == 0:
        time_init = timedelta(hours=date_before.hour, minutes=date_before.minute, seconds=date_before.second)
        time_final = timedelta(hours=date_now.hour, minutes=date_now.minute, seconds=date_now.second)
        difference_time = str(time_final - time_init).split(':')
        difference_hour = int(difference_time[0])
        difference_minute = int(difference_time[1])
        difference_second = int(difference_time[2])
        if difference_hour != 0:
            if difference_hour == 1:
                return str(difference_hour) + ' hora atrás'
            else:
                return str(difference_hour) + ' horas atrás'
        elif difference_minute != 0:
            if difference_minute == 1:
                return str(difference_minute) + ' minuto atrás'
            else:
                return str(difference_minute) + ' minutos atrás'
        else:
            if difference_second == 1:
                return str(difference_second) + ' segundo atrás'
            else:
                return str(difference_second) + ' segundos atrás'
    elif difference_date.days <= 3:
        if difference_date.days == 1:
            return 'Ontem'
        else:
            return str(difference_date.days) + ' dias atrás'
    else:
        months = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro',
        }

        return str(date_before.day) + ' de ' + months[date_before.month] + ' de ' + str(date_before.year)

def datetime_sao_paulo():
    utc_time = datetime.utcnow()
    tz = pytz.timezone('America/Sao_Paulo')
    utc_time = utc_time.replace(tzinfo=pytz.UTC) 
    st_sao_paulo_time = utc_time.astimezone(tz)
    return st_sao_paulo_time

def get_datetime_7_days(date_before):
    date_init = datetime(year=datetime_sao_paulo().year, month=datetime_sao_paulo().month, day=datetime_sao_paulo().day)
    date_before = datetime(year=date_before.year, month=date_before.month, day=date_before.day)

    difference_days = (date_init - date_before)

    if int(difference_days.days) <= 7:
        return True
    else:
        return False
