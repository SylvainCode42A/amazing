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