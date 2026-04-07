a-maze-ing/
│
├── a_maze_ing.py          # point d'entrée principal
├── config.txt             # config par défaut
├── Makefile
├── README.md
├── .gitignore
│
├── src/
│   ├── config_parser.py   # lecture et validation du fichier config
│   ├── maze_generator.py  # classe MazeGenerator (le coeur)
│   ├── maze_solver.py     # trouve le chemin entry -> exit
│   ├── maze_writer.py     # écrit le fichier de sortie hex
│   └── maze_display.py    # affichage ASCII
│
└── mazegen-1.0.0/         # le package pip (plus tard)



Bit    Position     Direction
0         LSB          Nord
1                      Est    
2                      Sud
3         MSB          Ouest

4 combinaisons de 4 chiffres soit 0 ou 1

0b111 = 0xF = 15 = f


config.txt
    ↓
tu lis WIDTH, HEIGHT, ENTRY, EXIT, PERFECT...
    ↓
tu crées une grille de WIDTH x HEIGHT cellules, toutes à 0xF
    ↓
tu appliques l'algorithme (Recursive Backtracker) → il casse des murs
    ↓
tu écris la grille dans OUTPUT_FILE
    ↓
tu affiches le labyrinthe à l'écran


1         # 0001
1 << 1    # 0010  (décalé d'un cran à gauche)
1 << 2    # 0100  (décalé de deux crans à gauche)
1 << 3    # 1000  (décalé de trois crans à gauche)