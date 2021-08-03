def scores(list_scores):

    list_strings = []
    pauvre = 0
    adequat = 0
    bien = 0
    excellent = 0
    elite = 0 

    prct_pauvre = 0
    prct_adequat = 0
    prct_bien = 0
    prct_excellent = 0
    prct_elite = 0

    for score in list_scores:
        if (score >= 300 and score <= 599):
            pauvre += 1
        elif (score >= 600 and score <= 699):
            adequat += 1
        elif (score >= 700 and score <= 749):
            bien += 1
        elif (score >= 750 and score <= 799):
            excellent += 1
        elif (score >= 800):
            elite += 1
    
    prct_pauvre = (pauvre/len(list_scores) * 100)
    prct_adequat = (adequat/len(list_scores) * 100)
    prct_bien = (bien/len(list_scores) * 100)
    prct_excellent = (excellent/len(list_scores) * 100)
    prct_elite= (elite/len(list_scores) * 100)
    
    

    print(pauvre, adequat, bien, excellent, elite)

    return(list_strings)
print(scores([830, 320, 710, 720]))



