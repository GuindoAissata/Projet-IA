import tkinter as tk
import random
from fonctions import creer_population,fitness,selection,crossover,mutation,formation
from genetique_algo import genetique

def dessiner_villes():
    canvas.delete("all") #reinitialisé la fenetre 
    villes= []
    n = int(entry.get())
    for _ in range (n) :
        x,y = random.randint(20,480), random.randint(20,480)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill= "red")
        villes.append((x,y))

    for i in range (len(villes)-1):
        x1,y1 = villes[i]
        x2,y2 = villes [i+1]
        canvas.create_line(x1,y1,x2,y2, fill ="black")#liaison entre les villes

    return villes #on utilisera la ville retournée pour paramètre de créer_population

def run_algo():
    return best_way ,best_fit = algo_genetique()





###########TEST DE creer_population #####################
# Liste de villes (coordonnées fictives)
villes_test = [(100, 200), (250, 400), (50, 50), (300, 150)]

# Taille de la population à générer
taille_population_test = 5

# Appel de la fonction
population_generee = creer_population(villes_test, taille_population_test)

parent1,parent2 = selection(population_generee,3)
enfant_i = crossover(parent1,parent2)
enfant_f= mutation(enfant_i)
nouvelle_pop = formation(population_generee,enfant_i)
best_way, best_fit = genetique(villes_test,taille_population_test)

# Affichage des résultats
print("Population générée :")
for i, individu in enumerate(population_generee):
    print(f"Itinéraire {i+1} : {individu} fitness{i+1} : {fitness(individu)}")

print (f"parents séletionnes :  {parent1} , {parent2}")
print (f"un enfant des parents sélectionnés est : {enfant_i} ")
print (f"un enfant des parents sélectionnés est : {enfant_f} ")
print (f"La nouvelle population est : {nouvelle_pop}")
print (f"le meilleur chemin est {best_way}")
print (f"la meilleure distance trouvée {best_fit}")



# fenetre 
fenetre = tk.Tk()
fenetre.title("Voyageur de Commerce")

entry = tk.Entry(fenetre) #utilisateur peut entrer une valeur 
entry.pack()

bouton1= tk.Button(fenetre, text = "générer villes", command = dessiner_villes)
bouton1.pack()

bouton2 = tk.Button(fenetre,text="Run the genetic algorithme", command=run_algo)
bouton2.pack()


canvas = tk.Canvas(fenetre, width=500, height=500, bg="white")
canvas.pack()



# Lancer l'application
fenetre.mainloop()



