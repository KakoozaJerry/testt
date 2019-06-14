from django.test import TestCase
from datetime import date, datetime
from base.models import Employees

# Create your tests here.
class another():
    t = date.today()
    dateet = datetime.strptime(t.strftime("%Y-%m-%d"), "%Y-%m-%d")
    lst=[]
    for i in  Employees.objects.filter(employee_id=3):
        dict={"zidi":i.id,"employeezidi":i.employee_id,"datii":i.date,"role":i.seniority}
        lst.append(dict)
    o = len(lst)
    sio = 0
    ptz = 0
    dateeem = dateedm = dateecm = dateebm = dateeam = 0
    """ a = b = c = d = e = '0-0-0'
    dateea = datetime.strptime(a.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dateeb = datetime.strptime(b.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dateec = datetime.strptime(c.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dateed = datetime.strptime(d.strftime("%Y-%m-%d"), "%Y-%m-%d")
    dateee = datetime.strptime(e.strftime("%Y-%m-%d"), "%Y-%m-%d") """
    for sio in range(o):
        if lst[sio]["role"] == 'A':
            a = lst[sio]["datii"]
            dateea = datetime.strptime(a.strftime("%Y-%m-%d"), "%Y-%m-%d")
            dateeam = dateea.month
        elif lst[sio]["role"] == 'B':
            b = lst[sio]["datii"]
            dateeb = datetime.strptime(b.strftime("%Y-%m-%d"), "%Y-%m-%d")
            dateebm = dateeb.month
        elif lst[sio]["role"] == 'C':
            c = lst[sio]["datii"]
            dateec = datetime.strptime(c.strftime("%Y-%m-%d"), "%Y-%m-%d")
            dateecm = dateec.month
        elif lst[sio]["role"] == 'D':
            d = lst[sio]["datii"]
            dateed = datetime.strptime(d.strftime("%Y-%m-%d"), "%Y-%m-%d")
            dateedm = dateed.month
        elif lst[sio]["role"] == 'E':
            e = lst[sio]["datii"]
            dateee = datetime.strptime(e.strftime("%Y-%m-%d"), "%Y-%m-%d")
            dateeem = dateee.month
    """ if dateeem != 0:
        if dateedm != 0:
            if dateee.year == dateet.year:
                zm = dateet.month - dateeem
                
            else:
                zy = dateet.year - dateee.year - 1
                zm = dateet.month + 12*zy + (12 - dateeem)
            if dateee.year == dateed.year:
                zm = dateeem - dateedm
            else:
                zy = dateee.year - dateed.year - 1
                zm = dateeem + 12*zy + (12-dateedm)
        else:
            if dateee.year == dateet.year:
                zm = dateet.month - dateeem
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 25*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 25*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 25*1.5
                        flag = flag + 1

            else:
                zy = dateet.year - dateee.year - 1
                zm = dateet.month + 12*zy + (12 - dateeem)
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 25*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 25*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 25*1.5
                        flag = flag + 1 """
    if dateeam != 0:
        if dateebm != 0:
            if dateeb.year == dateea.year:
                zm = dateebm - dateeam
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 5*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 5*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 5*1.5
                        flag = flag + 1
            else:
                zy = (dateeb.year - dateea.year) - 1
                zm = dateebm + 12*zy + (12-dateeam)
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 5*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 5*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 5*1.5
                        flag = flag + 1
            if dateecm != 0:
                if dateec.year == dateeb.year:
                    zm = dateecm - dateebm
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 10*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 10*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 10*1.5
                            flag = flag + 1
                else:
                    zy = (dateec.year - dateeb.year) -1
                    zm = dateecm + 12*zy + (12 - dateebm)
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 10*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 10*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 10*1.5
                            flag = flag + 1
                    if dateedm != 0:
                        if dateed.year == dateec.year:
                            zm = dateedm - dateecm
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 15*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 15*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 15*1.5
                                    flag = flag + 1
                            if dateeem != 0:
                                if dateee.year == dateed.year:
                                    zm = dateeem - dateedm
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 20*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 20*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 20*1.5
                                            flag = flag + 1
                                else:
                                    zy = dateee.year - dateed.year - 1
                                    zm = dateeem + 12*zy + (12 - dateedm)
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 20*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 20*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 20*1.5
                                            flag = flag + 1
                                if dateee.year == dateet.year:
                                    zm = dateet.month - dateeem
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 25*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 25*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 25*1.5
                                            flag = flag + 1
                                else:
                                    zy = dateee.year - dateed.year - 1
                                    zm = dateeem + 12*zy + (12 - dateedm)
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 25*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 25*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 25*1.5
                                            flag = flag + 1
                            else:
                                if dateed.year == dateet.year:
                                    zm = dateet.month - dateedm
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 20*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 20*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 20*1.5
                                            flag = flag + 1
                                else:
                                    zy = dateet.year - dateed.year - 1
                                    zm = dateet.month + 12*zy + (12 - dateedm)
                                    for s in range(zm):
                                        if flag <= 24:
                                            ptz = ptz + 20*1
                                            flag = flag + 1
                                        elif flag > 24 and flag <= 48:
                                            ptz = ptz + 20*1.25
                                            flag = flag + 1
                                        elif flag > 48:
                                            ptz = ptz + 20*1.5
                                            flag = flag + 1
                        else:
                            zy = dateed.year - dateec.year - 1
                            zm = dateedm + 12*zy + (12 - dateecm)
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 15*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 15*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 15*1.5
                                    flag = flag + 1
                            
                    else:
                        if dateec.year == dateet.year:
                            zm = dateet.month - dateecm
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 15*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 15*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 15*1.5
                                    flag = flag + 1
                        else:
                            zy = dateet.year - dateec.year - 1
                            zm = dateet.month + 12*zy + (12-dateecm)
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 15*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 15*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 15*1.5
                                    flag = flag + 1
            else:
                if dateeb.year == dateet.year:
                    zm = dateet.month - dateebm
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 10*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 10*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 10*1.5
                            flag = flag + 1
                else:
                    zy = dateet.year - dateeb.year - 1
                    zm = dateet.month + 12*zy + dateebm
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 10*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 10*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 10*1.5
                            flag = flag + 1
        else:
            if dateea.year == dateet.year:
                zm = dateet.month - dateeam
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 5*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 5*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 5*1.5
                        flag = flag + 1
            else:
                zy = (dateet.year - dateea.year) - 1 
                zm = dateet.month + 12*zy + (12 - dateeam)
                flag = 0
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 5*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 5*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 5*1.5
                        flag = flag + 1
        
        
        
    elif dateebm != 0:
        flag = 0
        if dateecm != 0:
            if dateec.year == dateeb.year:
                zm = dateecm - dateebm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 10*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 10*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 10*1.5
                        flag = flag + 1
            else:
                zy = dateec.year - dateeb.year - 1
                zm = dateecm + 12*zy + (12 - dateebm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 10*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 10*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 10*1.5
                        flag = flag + 1
            if dateedm != 0:
                if dateed.year == dateec.year:
                    zm = dateedm - dateecm
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 15*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 15*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 15*1.5
                            flag = flag + 1
                else:
                    zy = dateed.year - dateec.year - 1
                    zm = dateedm + 12*zy + (12 - dateecm)
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 15*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 15*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 15*1.5
                            flag = flag + 1
                        if dateeem != 0:
                            if dateee.year == dateed.year:
                                zm = dateeem - dateedm
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 20*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 20*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 20*1.5
                                        flag = flag + 1
                            else:
                                zy = dateee.year - dateed.year - 1
                                zm = dateeem + 12*zy + (12 - dateedm)
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 20*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 20*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 20*1.5
                                        flag = flag + 1
                            if dateee.year == dateet.year:
                                zm = dateet.month - dateeem
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 25*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 25*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 25*1.5
                                        flag = flag + 1
                            else:
                                zy = dateee.year - dateed.year - 1
                                zm = dateeem + 12*zy + (12 - dateedm)
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 25*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 25*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 25*1.5
                                        flag = flag + 1
                        else:
                            if dateed.year == dateet.year:
                                zm = dateet.month - dateedm
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 20*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 20*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 20*1.5
                                        flag = flag + 1
                            else:
                                zy = dateet.year - dateed.year - 1
                                zm = dateet.month + 12*zy + (12 - dateedm)
                                for s in range(zm):
                                    if flag <= 24:
                                        ptz = ptz + 20*1
                                        flag = flag + 1
                                    elif flag > 24 and flag <= 48:
                                        ptz = ptz + 20*1.25
                                        flag = flag + 1
                                    elif flag > 48:
                                        ptz = ptz + 20*1.5
                                        flag = flag + 1
            else:
                if dateec.year == dateet.year:
                    zm = dateet.month - dateecm
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 15*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 15*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 15*1.5
                            flag = flag + 1
                else:
                    zy = dateet.year - dateec.year - 1
                    zm = dateet.month + 12*zy + (12-dateecm)
                    for s in range(zm):
                        if flag <= 24:
                            ptz = ptz + 15*1
                            flag = flag + 1
                        elif flag > 24 and flag <= 48:
                            ptz = ptz + 15*1.25
                            flag = flag + 1
                        elif flag > 48:
                            ptz = ptz + 15*1.5
                            flag = flag + 1
        else:
            if dateeb.year == dateet.year:
                zm = dateet.month - dateebm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 10*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 10*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 10*1.5
                        flag = flag + 1
            else:
                zy = dateet.year - dateeb.year - 1
                zm = dateet.month + 12*zy + dateebm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 10*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 10*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 10*1.5
                        flag = flag + 1
        

    elif dateecm != 0:
        flag = 0
        if dateedm != 0:
            if dateed.year == dateec.year:
                zm = dateedm - dateecm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 15*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 15*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 15*1.5
                        flag = flag + 1
            else:
                zy = dateed.year - dateec.year - 1
                zm = dateedm + 12*zy + (12 - dateecm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 15*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 15*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 15*1.5
                        flag = flag + 1
                    if dateeem != 0:
                        if dateee.year == dateed.year:
                            zm = dateeem - dateedm
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 20*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 20*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 20*1.5
                                    flag = flag + 1
                        else:
                            zy = dateee.year - dateed.year - 1
                            zm = dateeem + 12*zy + (12 - dateedm)
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 20*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 20*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 20*1.5
                                    flag = flag + 1
                        if dateee.year == dateet.year:
                            zm = dateet.month - dateeem
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 25*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 25*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 25*1.5
                                    flag = flag + 1
                        else:
                            zy = dateee.year - dateed.year - 1
                            zm = dateeem + 12*zy + (12 - dateedm)
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 25*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 25*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 25*1.5
                                    flag = flag + 1
                    else:
                        if dateed.year == dateet.year:
                            zm = dateet.month - dateedm
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 20*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 20*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 20*1.5
                                    flag = flag + 1
                        else:
                            zy = dateet.year - dateed.year - 1
                            zm = dateet.month + 12*zy + (12 - dateedm)
                            for s in range(zm):
                                if flag <= 24:
                                    ptz = ptz + 20*1
                                    flag = flag + 1
                                elif flag > 24 and flag <= 48:
                                    ptz = ptz + 20*1.25
                                    flag = flag + 1
                                elif flag > 48:
                                    ptz = ptz + 20*1.5
                                    flag = flag + 1
        else:
            if dateec.year == dateet.year:
                zm = dateet.month - dateecm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 15*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 15*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 15*1.5
                        flag = flag + 1
            else:
                zy = dateet.year - dateec.year - 1
                zm = dateet.month + 12*zy + (12-dateecm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 15*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 15*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 15*1.5
                        flag = flag + 1

    elif dateedm != 0:
        flag = 0
        if dateeem != 0:
            if dateee.year == dateed.year:
                zm = dateeem - dateedm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 20*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 20*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 20*1.5
                        flag = flag + 1
            else:
                zy = dateee.year - dateed.year - 1
                zm = dateeem + 12*zy + (12 - dateedm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 20*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 20*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 20*1.5
                        flag = flag + 1
            if dateee.year == dateet.year:
                zm = dateet.month - dateeem
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 25*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 25*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 25*1.5
                        flag = flag + 1
            else:
                zy = dateee.year - dateed.year - 1
                zm = dateeem + 12*zy + (12 - dateedm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 25*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 25*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 25*1.5
                        flag = flag + 1
        else:
            if dateed.year == dateet.year:
                zm = dateet.month - dateedm
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 20*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 20*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 20*1.5
                        flag = flag + 1
            else:
                zy = dateet.year - dateed.year - 1
                zm = dateet.month + 12*zy + (12 - dateedm)
                for s in range(zm):
                    if flag <= 24:
                        ptz = ptz + 20*1
                        flag = flag + 1
                    elif flag > 24 and flag <= 48:
                        ptz = ptz + 20*1.25
                        flag = flag + 1
                    elif flag > 48:
                        ptz = ptz + 20*1.5
                        flag = flag + 1
    elif dateeem != 0:
        flag = 0
        if dateee.year == dateet.year:
            zm = dateet.month - dateeem
            for s in range(zm):
                if flag <= 24:
                    ptz = ptz + 25*1
                    flag = flag + 1
                elif flag > 24 and flag <= 48:
                    ptz = ptz + 25*1.25
                    flag = flag + 1
                elif flag > 48:
                    ptz = ptz + 25*1.5
                    flag = flag + 1
        else:
            zy = dateee.year - dateed.year - 1
            zm = dateeem + 12*zy + (12 - dateedm)
            for s in range(zm):
                if flag <= 24:
                    ptz = ptz + 25*1
                    flag = flag + 1
                elif flag > 24 and flag <= 48:
                    ptz = ptz + 25*1.25
                    flag = flag + 1
                elif flag > 48:
                    ptz = ptz + 25*1.5
                    flag = flag + 1
    print(ptz)
