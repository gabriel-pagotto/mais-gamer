import pytz
from datetime import datetime, timedelta
from pytz import timezone

def DatePost(date_before):
    date_now = datetime_sao_paulo()

    date_init = datetime(year=date_before.year, month=date_before.month, day=date_before.day)
    date_final = datetime(year=date_now.year, month=date_now.month, day=date_now.day, hour=date_now.hour)
    diference_date = (date_final - date_init)

    if diference_date.days == 0:
        time_init = timedelta(hours=date_before.hour, minutes=date_before.minute, seconds=date_before.second)
        time_final = timedelta(hours=date_now.hour, minutes=date_now.minute, seconds=date_now.second)
        diference_time = str(time_final - time_init).split(':')
        diference_hour = int(diference_time[0])
        diference_minute = int(diference_time[1])
        diference_second = int(diference_time[2])
        if diference_hour != 0:
            if diference_hour == 1:
                return str(diference_hour) + ' hora atrás'
            else:
                return str(diference_hour) + ' horas atrás'
        elif diference_minute != 0:
            if diference_minute == 1:
                return str(diference_minute) + ' minuto atrás'
            else:
                return str(diference_minute) + ' minutos atrás'
        else:
            if diference_second == 1:
                return str(diference_second) + ' segundo atrás'
            else:
                return str(diference_second) + ' segundos atrás'
    elif diference_date.days <= 3:
        if diference_date.days == 1:
            return 'Ontem'
        else:
            return str(diference_date.days) + ' dias atrás'
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
    utc_time =utc_time.replace(tzinfo=pytz.UTC) 
    st_sao_paulo_time=utc_time.astimezone(tz)
    return datetime.utcnow #st_sao_paulo_time
