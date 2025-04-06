from fonctions import creer_population,fitness,selection,crossover,mutation,formation


def genetique(villes,taille_pop):
#principe : on repète tant qu'on améliore , donc si first_best n'a pas pas chnagé au cours de l'algo on s'arrête sinon tant que ça change on continue
    population = creer_population(villes,taille_pop)
    first_best = max(population, key=fitness)
    while(True):
        #selection des parents 
        parent1,parent2 = selection(population,k=3)

        #recombinaison des parents
        enfant = crossover(parent1,parent2)

        #Mutation de l'enfant
        enfant = mutation(enfant)

        #Formation : ajouter l'enfant à la popultion en mettenant la taille de la population
        population = formation(population,enfant)
        
        #find of the best way
        best = max(population,key = fitness)

        #si la fitness optimal augmente(c-a-d la distance diminue) alors on continu sinon on s'arrête
        if fitness(best) > fitness(first_best) :  
            first_best = best
        else : break #si l'ancine optimal est égal au nouveau alors pas d'amélioration on arrête
    return first_best , 1/fitness(first_best)
