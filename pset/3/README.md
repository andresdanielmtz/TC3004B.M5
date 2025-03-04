# Tarea 3

Andrés Martínez - _A00227463_

> Based on [Refactory Guru Example](https://refactoring.guru/design-patterns/abstract-factory/python/example) and [GeeksForGeeks](https://www.geeksforgeeks.org/abstract-factory-pattern/) examples.

## Instalación y Ejecución

Debido a que este programa no utiliza librerías externas, no es necesario instalar dependencias, etc. Utiliza únicamente funciones y atributos dentro de la librería estándar de Python (3.13.0)

Para ejecutar el programa, puedes utilizar el siguiente comando:

```bash
python3 main.py
```

## Diagrama

![Diagrama UML](assets/uml.png)

## Explicación

Para esta implementación creamos una fabrica de computadoras a partir de sus interfaces  (the ones in `./computers/`), en donde creamos un interfaz para una fabrica abstracta (`factory/ComputerFactoryClass.py`)

A partir de esto podemos crear fabricas concretas, en nuestro caso sería la fabrica de ASUS y HP (`./factory/ASUSFactoryClass` y ``./factory/HPFactoryClass`).

Finalmente podemos declarar la funcionalidad de estos productos de cada marca en (`./model/ASUS.py` y `./model/HP.py`) y crear una clase Client que maneje estas fabricas (`./client.py`)

## Trivia

La carpeta `.unused` es un archivo de una implementación temprana del proyecto, y actualmente en desuso, puesto que usaba el Factory Pattern en lugar del Abstract Factory Pattern.
