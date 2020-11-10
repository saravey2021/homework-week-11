def getComment(grade):
    if grade>10:
        return "Good"
    else:
        return "bad"
print(getComment(12)+getComment(8))
