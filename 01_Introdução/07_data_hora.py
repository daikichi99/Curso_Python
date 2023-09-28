import time
from datetime import datetime
from pytz import timezone

# utilizando a Lib TIME
# utilizando a Lib DATETIME
# utilizando a Lib PYTZ



print (datetime.today())
dthr = datetime.now()
fuso_br = timezone('america/sao_Paulo')
sp = dthr.astimezone(fuso_br)
print(sp)

# como formatar data e hora

sp_formatado = sp.strftime('%d-%m-%Y %H:%M')
print(sp)
print(sp_formatado)

