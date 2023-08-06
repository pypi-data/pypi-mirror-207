# -*- coding: utf-8 -*-
"""  dates utilities
Doc::
"""
import os, sys, time, datetime,inspect, json, yaml, gc, numpy as np, pandas as pd

#############################################################################################
from utilmy.utilmy_base import log, log2

def help():
    """function help        
    """
    from utilmy import help_create
    print(  help_create(__file__) )


####################################################################################################
def test_all():
    """function test_all        
    """
    test1()
    test2()


def test1():    
    log("Testing dates.py ...")

    df = pd.DataFrame(columns=['Birthdate'])
    df['Birthdate'] = pd_random_daterange(start=pd.to_datetime('2000-01-01'), end=pd.to_datetime('2022-01-01'), size=10)
    print(df)
    assert not df.empty, 'FAILED, generate df data'


    df2 = pd_date_split(df, coldate='Birthdate', sep='-')
    print(df2)
    assert not df2.empty, 'FAILED, pd_date_split'

    import datetime
    res =  date_to_timezone(datetime.datetime.now())
    print(res)
    assert res, 'FAILED, date_to_timezone'

    res = date_is_holiday([pd.to_datetime('2000-01-01')])
    print(res)
    assert res, 'FAILED, date_is_holiday'

    res = date_weekmonth2(datetime.datetime.now())
    print(res)
    assert res, 'FAILED, date_weekmonth2'

    # date_weekyear2
    res = date_weekyear2(datetime.datetime.now())
    print(res)
    assert res, 'FAILED, date_weekyear2'

    # date_weekday_excel
    res = date_weekday_excel("20220223")
    print(res)
    assert res, 'FAILED, date_weekday_excel'

    # date_weekyear_excel
    res = date_weekyear_excel("20220223")
    print(res)
    assert res, 'FAILED, date_weekyear_excel'


    date_ = date_generate(start='2021-01-01', ndays=100)
    print(date_)
    assert date_, 'FAILED, date_generate'

    date_weekyear_excel('20210317')
    date_weekday_excel('20210317')


def test2():
    # test date_now()
    res = date_now()
    log(res)
    assert res, 'FAILED, date_now'

    # test date_now with add more days
    res = date_now(add_days=5, timezone='Asia/Tokyo')
    log(res)
    assert res, 'FAILED, date_now'

    # test date_now with new format
    res = date_now(fmt="%d/%m/%Y", add_days=12)
    log(res)
    assert res, 'FAILED, date_now'

    assert date_now(timezone='Asia/Tokyo')    #-->  "20200519"   ## Today date in YYYMMDD
    assert date_now(timezone='Asia/Tokyo', fmt='%Y-%m-%d')    #-->  "2020-05-19"

    res = date_now('2020-12-10', fmt='%Y%m%d', add_days=-5, returnval='int')
    log(res )
    assert res == 20201205, 'FAILED, date_now'

    res = date_now(20211005, fmt='%Y-%m-%d', fmt_input='%Y%m%d', returnval='str')  #-->  '2021-10-05'
    log(res )
    assert res == '2021-10-05', 'FAILED, date_now'



def pd_random_daterange(start, end, size):
    """pd_random_daterange is used to get random dates between start and end date.

    Docs::

        Args:
            Start (pd.to_datetime):   Starting date
            End (pd.to_datetime):     Ending date
            Size (int):    Number of random dates we want to generate.
        Returns: Return the "n" random dates between start and end dates
        Example: from utilmy.dates import pd_random_daterange
                 df = pd.DataFrame(columns=['Birthdate'])
                 df['Birthdate'] = pd_random_daterange(start=pd.to_datetime('2000-01-01'), end=pd.to_datetime('2022-01-01'), size=3)
                 print(df)

                 Output:        Birthdate
                             0 2010-08-12
                             1 2009-05-22
                             2 2021-09-22


    """
    divide_by = 24 * 60 * 60 * 10**9
    print(".value", start.value)
    start_u = start.value // divide_by
    end_u = end.value // divide_by
    return pd.to_datetime(np.random.randint(start_u, end_u, size), unit="D")




####################################################################################################
##### Utilities for date  ##########################################################################
def pd_date_split(df, coldate =  'time_key', prefix_col ="",sep="/" ,verbose=False ):
    """function pd_date_split to split date into different formate.

    Docs::

        Args:
            df (pd):          df is the random date
            coldate (str):    The name we want to give to the random date. (Ex: 'Birthdate')
            prefix_col (str): The space we leave in prefix of each date.
            sep (str):         separation between (Year,week), (year,Month), (year, quarter)
                         (Ex: year quarter 2021/3, '/' is separation)
            verbose (bool):   If True, print the output.
        Returns: Return date in different formate.

        Example:    from utilmy.dates import pd_date_split

                    df2= pd_date_split(df, coldate ='Birthdate', sep='/')
                    print(df2)


                    Output:      Birthdate        date     year   month   day   weekday   weekmonth   weekmonth2   weekyeariso   weekyear2   quarter   yearweek   yearmonth  yearqarter   isholiday
                                2021-11-26  2021-11-26     2021      11    26         4           4            4            47          48         3    2021/47     2021/11      2021/3          0



        
    """
    import pandas as pd

    df = df.drop_duplicates(coldate)
    df['date'] =  pd.to_datetime( df[coldate] )

    ############# dates
    df['year']          = df['date'].apply( lambda x : x.year   )
    df['month']         = df['date'].apply( lambda x : x.month   )
    df['day']           = df['date'].apply( lambda x : x.day   )
    df['weekday']       = df['date'].apply( lambda x : x.weekday()   )
    df['weekmonth']     = df['date'].apply( lambda x : date_weekmonth(x)   )
    df['weekmonth2']    = df['date'].apply( lambda x : date_weekmonth2(x)   )
    df['weekyeariso']   = df['date'].apply( lambda x : x.isocalendar()[1]   )
    df['weekyear2']     = df['date'].apply( lambda x : date_weekyear2( x )  )
    df['quarter']       = df.apply( lambda x :  int( x['month'] / 4.0) + 1 , axis=1  )

    def merge1(x1,x2):
        if sep == "":
            return int(str(x1) + str(x2))
        return str(x1) + sep + str(x2)

    df['yearweek']      = df.apply(  lambda x :  merge1(  x['year']  , x['weekyeariso'] )  , axis=1  )
    df['yearmonth']     = df.apply( lambda x : merge1( x['year'] ,  x['month'])         , axis=1  )
    df['yearquarter']   = df.apply( lambda x : merge1( x['year'] ,  x['quarter'] )         , axis=1  )

    df['isholiday']     = date_is_holiday(df['date'])

    exclude = [ 'date', coldate]
    df.columns = [  prefix_col + x if not x in exclude else x for x in df.columns]
    if verbose : log( "holidays check", df[df['isholiday'] == 1].tail(15)  )
    return df


def date_to_timezone(tdate,  fmt="%Y%m%d-%H:%M", timezone='Asia/Tokyo'):
    """ date_to_timezone is used to get date and time for particular timezone

        Docs::

            Args:
                tdate (datetime):    date to convert to timezone
                fmt (str):      formate of date and time (Ex: YYYYMMDD-HH:MM)
                timezone (str): timezone for which we want to find time and date (Ex: 'Asia/Tokyo')

            Returns: return date and time according to timezone

            Example:   from utilmy.dates import date_to_timezone
                       import datetime
                       res= date_to_timezone(datetime.datetime.now())
                       print(res)

                       Output:   20221027-15:04
    """
    from pytz import timezone as tzone
    import datetime
    # Convert to US/Pacific time zone
    now_pacific = tdate.astimezone(tzone('Asia/Tokyo'))
    return now_pacific.strftime(fmt)


##def date_now(fmt="%Y-%m-%d %H:%M:%S %Z%z", add_days=0, timezone='Asia/Tokyo'):
from utilmy.utilmy_base import date_now




def date_is_holiday(array):
    """function date_is_holiday to check the holiday on array of pd.date format.

        Docs::

            Args:
                array (list):   array of pd.date format to check weather it is holiday or not
                                ( Ex. date_is_holiday([ pd.to_datetime("2015/1/1") ]) )

            Returns:    1 if the date is holiday
                        0 if the date is not holiday

            Example:    from utilmy.dates import  date_is_holiday
                        res = date_is_holiday([pd.to_datetime('2000-01-01')])
                        print(res)

                        Output: [1]

    """
    import holidays , numpy as np
    jp_holidays = holidays.CountryHoliday('JP')
    return np.array( [ 1 if x in jp_holidays else 0 for x in array]  )


def date_weekmonth2(d):
     """function date_weekmonth2 to get the week of the month on given date.

    Docs::

        Args:
             d(datetime):   date to find the week of the month (Ex: datetime.datetime(2020, 5, 17))
        Returns:   week of the month on given date

        Example:    from utilmy.dates import  date_weekmonth2
                    res = date_weekmonth2(datetime.datetime(2020, 5, 17))
                    print(res)

                    Output: 3
        """
     w = (d.day-1)//7+1
     if w < 0 or w > 5 :
         return -1
     else :
         return w


def date_weekmonth(date_value):
     """  Incorrect """
     w = (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)
     if w < 0 or w > 6 :
         return -1
     else :
         return w


def date_weekyear2(dt) :
    """function date_weekyear2 to get the week of the year on given date.

    Docs::

        Args:
            dt (datetime):  date to get the week of the year (Ex: datetime.datetime(2020, 5, 17))
        Returns: return week of that date in that year

        Example:    from utilmy.dates import  date_weekyear2
                    res = date_weekyear2(datetime.datetime(2020, 5, 17))
                    print(res)

                    Output: 20
        """
    return ((dt - datetime.datetime(dt.year,1,1)).days // 7) + 1


def date_weekday_excel(x) :
    """method returns the day of the week as an integer, where Monday is 1 and Sunday is 7

    Docs::

        Args:
            x (str):   date in string format (Ex: '20200517')
        Returns: weekday of the date
        """
    import datetime
    date = datetime.datetime.strptime(x,"%Y%m%d")
    wday = date.weekday()
    if wday != 7 : return wday+1
    else :    return 1


def date_weekyear_excel(x) :
    """function is used to return a ISO Week Number.

    Docs::
    
        Args:
              x (str): date in string format (Ex: '20200517')
        Returns: ISO Week Number
    """
    import datetime
    date = datetime.datetime.strptime(x,"%Y%m%d")
    return date.isocalendar()[1]


def date_generate(start='2018-01-01', ndays=100) :
    """function to generate list of n(ndays) consecutive days from the start date.

    Docs::

        Args:
            start (str):   Starting Date default to '2018-01-01'
            ndays (int):   Number of dates to generate (default to 100)
        Returns: List of generated dates

        """
    from dateutil.relativedelta import relativedelta
    start0 = datetime.datetime.strptime(start, "%Y-%m-%d")
    date_list = [start0 + relativedelta(days=x) for x in range(0, ndays)]
    return date_list


###################################################################################################
if __name__ == "__main__":
    import fire
    fire.Fire()