import tkinter as tk
from tkinter import ttk
import random
from fonctions import creer_population,fitness,selection,crossover,mutation,formation
from genetique_algo import genetique

villes= []


def generer_villes():
    canvas.delete("all") #reinitialisé la fenetre 
    global villes
    villes= []
    n = int(entry.get())
    for _ in range (n) :
        x,y = random.randint(10,490), random.randint(10,190)
        canvas.create_oval(x-5, y-5, x+5, y+5, fill= "red",tags="ville")

        villes.append((x,y))

    for i in range (len(villes)-1):
        x1,y1 = villes[i]
        x2,y2 = villes [i+1]
        canvas.create_line(x1,y1,x2,y2, fill ="black",width=2,tags="ligne")#liaison entre les villes

def dessiner_villes(villes):
    canvas_resultat.delete("all") #reinitialisé la fenetre 
    for i in range (len(villes)-1):
        x1,y1 = villes[i]
        x2,y2 = villes [i+1]
        canvas_resultat.create_oval(x1-5, y1-5, x1+5, y1+5, fill= "red",tags="ligne")
        canvas_resultat.create_line(x1,y1,x2,y2, fill ="black",width=2, tags = "ligne",)#liaison entre les villes
    

    x1, y1 = villes[-1]
    x2, y2 = villes[0]
    canvas_resultat.create_line(x1, y1, x2, y2, fill="red", width=2, tags="ligne")
    canvas_resultat.create_oval(x1-5, y1-5, x1+5, y1+5, fill= "red",tags="ligne")


    #return villes #on utilisera la ville retournée pour paramètre de créer_population


def run_algo():
    taille_pop = 100


    best_way ,best_fit = genetique(villes,taille_pop)
    print(f"le meilleur chemin trouvé est : {best_way} ")
    print(f"la meilleure distance trouvée est : {best_fit} ")


    return best_way, best_fit ,dessiner_villes(best_way), label_distance.config(text=f"BEST DIST : {best_fit :.2f}")





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
fenetre.title("Travelling Salesman Problem")
fenetre.geometry("600x700") #largeur x Hauteur

###############"generer les villes"##################
frame_genere_ville = tk.Frame(fenetre , bg ="white" )
frame_genere_ville.pack(side=tk.TOP, fill = tk.BOTH , expand= True)

label1 = tk.Label(frame_genere_ville, text="CITY GENERATION", bg="white", font=("Arial", 14))
label1.pack(pady=10)

#Canva pour afficher les villes générées 
canvas = tk.Canvas(frame_genere_ville,width=500,height=200,bg="white")
canvas.pack()

#################Résultat de l'algorithme###########""
frame_genetic = tk.Frame(fenetre,bg = "white")
frame_genetic.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

label2 = tk.Label(frame_genetic, text="OUTPUT OF THE ALGORITHME", bg="white", font=("Arial", 14))
label2.pack(pady=10)

#Canvas pour afficher le résultat de l'algorithme
canvas_resultat = tk.Canvas(frame_genetic, width=500, height=200, bg="white")
canvas_resultat.pack()

####################les boutons##################""
#frame_boutton = tk.Frame(fenetre,bg="white")
#frame_boutton.pack(side=tk.RIGHT, fill = tk.Y)

#label3 = tk.Label(frame_boutton, text="Contrôles", bg="#f0f0f0", font=("Arial", 14))
#label3.pack(pady=10)

entry = tk.Entry(frame_genere_ville) #utilisateur peut entrer une valeur 
entry.pack()

#Boutons

bouton1= tk.Button(frame_genere_ville, text = "generate cities", command = generer_villes)
bouton1.pack(pady=5)

bouton2 = tk.Button(frame_genetic,text="Run the genetic algorithme", command=run_algo)
bouton2.pack(pady=5)

label_distance = tk.Label(frame_genetic,text="BEST DISTANCE : ")
label_distance.pack()





# Lancer l'application
fenetre.mainloop()



