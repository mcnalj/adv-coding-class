teachers = ["McCray, Susan", "Ford, Mark", "Doane, Stephanie", "Kutvirt, Jacque", "Robinson, CC", "Nicholson, Gwyneth", "Nichols, Rebecca", "Loughlin, Anne", "Meahl, Jack", "McNally, Jake", "Murray, Kevin", "Haar, Mallory"]

for teacher in teachers:
    teacher = teacher.lower()
    commaIndex = teacher.find(",")
    initialIndex = commaIndex + 2
    if commaIndex >=5:
        namePart = teacher[0:5]
        firstInitial = teacher[initialIndex]
        email = namePart + firstInitial + "@portlandschools.org"
        print(email)
    else:
        namePart = teacher[0:4]
        secondInitialIndex = initialIndex + 2
        firstInitials = teacher[initialIndex:secondInitialIndex]
        email = namePart + firstInitials + "@portlandschools.org"
        print(email)

    