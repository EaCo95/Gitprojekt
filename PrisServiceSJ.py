from dataclasses import dataclass
from datetime import timedelta
import datetime

idag = datetime.datetime.now()
julafton = datetime.datetime(2023,12,24)
td = julafton - idag
print(td.days)



delta = timedelta()
days = 3,6
hours = 24





def calculatePrice(grundPris, datum):

    grundpris = 500

    if datum >= hours:
        return grundPris * 0.8

    elif datum >= days:
        return grundPris * 0.95

    elif datum >= weeks:
       return grundPris * 0.94


