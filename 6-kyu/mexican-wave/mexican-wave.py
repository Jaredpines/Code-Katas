def wave(people):
    if people == "":
        return []
    wave = []
    for person in range(0, len(people)):
        if people[person] != " ":
            wa = people[:person] + people[person].upper() + people[person+1:]
            wave.append(wa)
    return wave