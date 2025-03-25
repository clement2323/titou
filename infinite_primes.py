"""
Démonstration visuelle de l'infinité des nombres premiers - Pour Titou, avec tout mon amour ❤️
"""
import matplotlib.pyplot as plt
import numpy as np
import sympy
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.gridspec import GridSpec
import math

# Configuration du style
plt.style.use('ggplot')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

class InfinitePrimesDemo:
    def __init__(self):
        # Création de la figure avec une disposition personnalisée
        self.fig = plt.figure(figsize=(14, 8))
        gs = GridSpec(2, 2, width_ratios=[1, 1.2], height_ratios=[1, 1])
        
        # Création des sous-graphiques
        self.ax1 = self.fig.add_subplot(gs[0, 0])  # Crible d'Ératosthène
        self.ax2 = self.fig.add_subplot(gs[0, 1])  # Preuve d'Euclide
        self.ax3 = self.fig.add_subplot(gs[1, :])  # Graphique de croissance des nombres premiers
        
        self.fig.suptitle("Démonstration de l'infinité des nombres premiers - Pour Titou, avec tout mon amour ❤️", 
                           fontsize=16, color='darkred')
        
        # Stockage des nombres premiers trouvés
        self.premiers = []
        self.limit = 2
        self.animation = None
        
        # Initialisation des couleurs
        self.colors = {
            'background': '#f8f9fa',
            'prime': '#e63946',
            'non_prime': '#a8dadc',
            'highlight': '#1d3557',
            'text': '#457b9d'
        }
        
        # Initialisation des données pour la courbe de croissance
        self.x_data = []
        self.y_data = []
        self.line, = self.ax3.plot([], [], 'r-', linewidth=2)
        
    def est_premier(self, n):
        """Vérifie si un nombre est premier."""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def init_animation(self):
        """Initialisation de l'animation."""
        self.ax1.clear()
        self.ax1.set_title("Crible d'Ératosthène: Identification des nombres premiers")
        self.ax1.set_xlabel("Nombres")
        self.ax1.set_ylabel("État")
        
        self.ax2.clear()
        self.ax2.set_title("Preuve d'Euclide par contradiction")
        self.ax2.axis('off')
        
        self.ax3.clear()
        self.ax3.set_title("Croissance des nombres premiers")
        self.ax3.set_xlabel("n-ième nombre premier")
        self.ax3.set_ylabel("Valeur du nombre premier")
        self.ax3.grid(True, linestyle='--', alpha=0.7)
        
        self.x_data = []
        self.y_data = []
        self.line.set_data([], [])
        
        return [self.line]
    
    def update_animation(self, i):
        """Mise à jour de l'animation pour chaque frame."""
        # Augmenter progressivement la limite
        self.limit = min(100, 10 + i * 5)
        
        # Mise à jour du crible d'Ératosthène
        self._update_sieve()
        
        # Mise à jour de la preuve d'Euclide
        self._update_euclid_proof()
        
        # Mise à jour du graphique de croissance
        self._update_growth_chart()
        
        return [self.line]
    
    def _update_sieve(self):
        """Mise à jour du crible d'Ératosthène."""
        self.ax1.clear()
        self.ax1.set_title("Crible d'Ératosthène: Identification des nombres premiers")
        self.ax1.set_xlabel("Nombres")
        self.ax1.set_ylabel("État")
        
        # Générer tous les nombres jusqu'à la limite
        nombres = list(range(2, self.limit + 1))
        etats = [self.est_premier(n) for n in nombres]
        
        # Mettre à jour la liste des nombres premiers
        self.premiers = [n for n, etat in zip(nombres, etats) if etat]
        
        # Tracer le crible
        barres = self.ax1.bar(nombres, height=[1] * len(nombres), 
                             color=[self.colors['prime'] if etat else self.colors['non_prime'] for etat in etats])
        
        # Ajouter les labels
        for bar, nombre in zip(barres, nombres):
            height = bar.get_height()
            self.ax1.text(bar.get_x() + bar.get_width()/2., 1.05*height,
                         str(nombre), ha='center', va='bottom', 
                         color=self.colors['prime'] if self.est_premier(nombre) else 'gray',
                         fontweight='bold' if self.est_premier(nombre) else 'normal')
        
        self.ax1.set_ylim(0, 1.5)
    
    def _update_euclid_proof(self):
        """Mise à jour de la preuve d'Euclide."""
        self.ax2.clear()
        self.ax2.axis('off')
        
        if not self.premiers:
            self.ax2.text(0.5, 0.5, "En attente de nombres premiers...", 
                         horizontalalignment='center', fontsize=12)
            return
        
        # Limiter à un nombre raisonnable de premiers pour la démonstration
        display_premiers = self.premiers[:min(5, len(self.premiers))]
        
        # Calculer le produit des premiers + 1
        produit = np.prod(display_premiers)
        produit_plus_un = produit + 1
        
        # Déterminer si ce nouveau nombre est premier
        est_nouveau_premier = self.est_premier(produit_plus_un)
        
        # Trouver ses facteurs premiers (s'il n'est pas premier)
        if not est_nouveau_premier:
            facteurs = list(sympy.primefactors(produit_plus_un))
        else:
            facteurs = [produit_plus_un]
        
        # Afficher les informations
        self.ax2.text(0.05, 0.95, "Preuve d'Euclide:", fontsize=14, fontweight='bold', 
                     transform=self.ax2.transAxes)
        
        # Afficher les nombres premiers trouvés
        premiers_str = " × ".join([str(p) for p in display_premiers])
        self.ax2.text(0.05, 0.85, f"Nombres premiers trouvés: {', '.join([str(p) for p in display_premiers])}", 
                     fontsize=12, transform=self.ax2.transAxes)
        
        # Afficher le produit + 1
        self.ax2.text(0.05, 0.75, f"Produit P = {premiers_str} = {produit}", 
                     fontsize=12, transform=self.ax2.transAxes)
        
        self.ax2.text(0.05, 0.65, f"P + 1 = {produit} + 1 = {produit_plus_un}", 
                     fontsize=12, transform=self.ax2.transAxes, color=self.colors['highlight'])
        
        # Explication de la preuve
        if est_nouveau_premier:
            self.ax2.text(0.05, 0.55, f"{produit_plus_un} est un nombre premier qui n'est pas dans notre liste!", 
                         fontsize=12, transform=self.ax2.transAxes, color=self.colors['prime'], fontweight='bold')
            
            self.ax2.text(0.05, 0.45, "Nous avons trouvé un nouveau nombre premier qui n'était pas\n"
                                      "dans notre liste supposément complète de nombres premiers.", 
                          fontsize=12, transform=self.ax2.transAxes)
        else:
            self.ax2.text(0.05, 0.55, f"{produit_plus_un} n'est pas premier, ses facteurs premiers sont: {facteurs}", 
                         fontsize=12, transform=self.ax2.transAxes)
            
            # Vérifier si les facteurs sont différents des premiers de notre liste
            nouveaux_facteurs = [f for f in facteurs if f not in display_premiers]
            if nouveaux_facteurs:
                self.ax2.text(0.05, 0.45, 
                             f"Les nombres {', '.join(map(str, nouveaux_facteurs))} sont des facteurs premiers\n"
                             f"qui ne sont pas dans notre liste supposément complète!", 
                             fontsize=12, transform=self.ax2.transAxes, color=self.colors['prime'], fontweight='bold')
        
        # Conclusion
        self.ax2.text(0.05, 0.30, "Par contradiction, notre hypothèse (qu'il y a un nombre fini\n"
                                  "de nombres premiers) est fausse.", 
                     fontsize=12, transform=self.ax2.transAxes, fontweight='bold')
        
        self.ax2.text(0.05, 0.20, "Donc il y a une infinité de nombres premiers.", 
                     fontsize=14, transform=self.ax2.transAxes, color='darkred', fontweight='bold')
        
        # Message d'amour pour Titou
        self.ax2.text(0.5, 0.05, "Pour Titou, la plus belle étoile de mon univers infini ❤️", 
                     fontsize=12, transform=self.ax2.transAxes, style='italic', 
                     ha='center', color='purple', fontweight='bold')
    
    def _update_growth_chart(self):
        """Mise à jour du graphique de croissance des nombres premiers."""
        # Actualiser les données
        self.x_data = list(range(1, len(self.premiers) + 1))
        self.y_data = self.premiers
        
        # Mettre à jour la ligne
        self.line.set_data(self.x_data, self.y_data)
        
        # Mise à jour des limites
        if self.premiers:
            self.ax3.set_xlim(0, max(5, len(self.premiers) + 1))
            self.ax3.set_ylim(0, max(10, max(self.premiers) * 1.1))
            
            # Tracé de la fonction n*ln(n) (théorème des nombres premiers)
            x_theory = np.linspace(1, len(self.premiers) + 1, 100)
            y_theory = [x * np.log(x) for x in x_theory]
            
            # Suppression des anciennes courbes théoriques
            for line in self.ax3.lines[1:]:
                line.remove()
                
            # Ajouter la nouvelle courbe théorique
            self.ax3.plot(x_theory, y_theory, '--', color='blue', alpha=0.7, 
                        label='n ln(n) (approximation théorique)')
            
            # Ajouter une légende
            self.ax3.legend(loc='upper left')
            
            # Ajouter du texte explicatif
            if len(self.premiers) > 10:
                pnt = self.ax3.text(0.05, 0.95, 
                                  "Le théorème des nombres premiers montre que la densité\n"
                                  "des nombres premiers diminue logarithmiquement.", 
                                  transform=self.ax3.transAxes, fontsize=10,
                                  bbox=dict(facecolor='white', alpha=0.7))
    
    def run(self):
        """Lancer l'animation."""
        self.animation = animation.FuncAnimation(
            self.fig, self.update_animation, init_func=self.init_animation,
            frames=30, interval=1000, blit=False)
        
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajuster pour le titre
        plt.show()

if __name__ == "__main__":
    print("❤️ Démarrage de la démonstration de l'infinité des nombres premiers - Pour Titou, avec amour ❤️")
    demo = InfinitePrimesDemo()
    demo.run()