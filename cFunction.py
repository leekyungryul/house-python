def postweek(yearweek, Wantweek):
    if type(Wantweek) == str : Wantweek = int(Wantweek)    
    if type(yearweek) == int : yearweek = str(yearweek) 
    inputyear = int(yearweek[:4])
    inputweek = int(yearweek[4:])
    i = inputyear
    Maxweek = isoweek.Week.last_week_of_year(inputyear)[1]
    result = int((inputweek + Wantweek) - Maxweek)
    year = inputyear
    if (result <= 0):
        if len(str(inputweek+Wantweek)) == 1 :
            resultYearweek = str(year) + "0" + str(inputweek+Wantweek) 
        else:
            resultYearweek = str(year) + str(inputweek+Wantweek) 
        return resultYearweek
    else:
        while(True):
            year = year + 1
            maxWeek = isoweek.Week.last_week_of_year(year)[1]
            if result == maxWeek:
                resultYearweek = str(year) + str(maxWeek)
                break;
            elif result < maxWeek:
                if len(str(result)) == 1:
                    resultYearweek = str(year) + "0" + str(result)
                else:
                    resultYearweek = str(year) + str(result)
                break;
            result  = result - maxWeek
    return resultYearweek