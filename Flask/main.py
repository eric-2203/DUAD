#Crea un API con Flask de que permita un CRUD (Create, Read, Update, Delete) de tareas. 
# Importé todas las librerías que vi en el video, en caso de necesitarlas.
from flask import Flask, jsonify, request, Response, url_for, session, redirect
import json
from dataclasses import dataclass

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Bienvenido al API de Tareas!</h1>"

valid_status = ["por hacer", "en progreso", "completada"]

def write_file(tasks):
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)
        

def read_file():
    try:
        with open('tasks.json', 'r', encoding='utf-8') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        return []
    return tasks


@app.route("/tareas")
def show_tasks():
    tasks = read_file()
    tasks_filter = request.args.get("estado")
    if tasks_filter:
        tasks = list(
            filter(lambda task: task["estado"] == tasks_filter, tasks)
        )
    return {"data": tasks}

@app.route("/register", methods=['POST'])
def register_task():
    tasks = read_file()
    try:
        if "identificador" not in request.json or request.json["identificador"] == "":
            raise ValueError("Hace falta el identificador de la tarea.")
        
        if "titulo" not in request.json or request.json["titulo"] == "":
            raise ValueError("Hace falta el titulo de la tarea.")
        
        if "descripcion" not in request.json or request.json["descripcion"] == "":
            raise ValueError("Hace falta la descripcion de la tarea.")
        
        if "estado" not in request.json or request.json["estado"] == "":
            raise ValueError("Hace falta el estado de la tarea.")
        if request.json["estado"].lower() not in valid_status:
            raise ValueError("El estado ingresado no es valido. Ingrese un estado valido.")
        
        for task in tasks:
            if task["identificador"] == request.json["identificador"]:
                raise ValueError("Este identificador de tarea ya existe. Inserta un identificador nuevo.")

        tasks.append(
            {
                "identificador": request.json["identificador"],
                "titulo": request.json["titulo"],
                "descripcion": request.json["descripcion"],
                "estado": request.json["estado"].lower()
            }
        )

        write_file(tasks)
        return tasks
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
    
@app.route("/edit", methods=['PUT'])
def edit_task():
    tasks = read_file()
    found = False
    try: 
        if "titulo" not in request.json or request.json["titulo"] == "":
            raise ValueError("Hace falta el titulo de la tarea.")
        
        if "descripcion" not in request.json or request.json["descripcion"] == "":
            raise ValueError("Hace falta la descripcion de la tarea.")
        
        if "estado" not in request.json or request.json["estado"] == "":
            raise ValueError("Hace falta el estado de la tarea.")
        if request.json["estado"].lower() not in valid_status:
            raise ValueError("El estado ingresado no es valido. Ingrese un estado valido.")
        
        for task in tasks:
            if task["identificador"] == request.json["identificador"]:
                task["titulo"] = request.json["titulo"]
                task["descripcion"] = request.json["descripcion"]
                task["estado"] = request.json["estado"].lower()
                found = True
                break
        if found is True:
            write_file(tasks)
            return tasks
        elif found == False:
            raise ValueError("El identificador de tarea no existe o enviaste un valor vacío.")


    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500


@app.route("/delete", methods=['DELETE'])
def delete_task():
    tasks = read_file()
    found = False
    try:  
        for task in tasks:
            if task["identificador"] == request.json["identificador"]:
                tasks.remove(task)
                found = True
                break
        if found is True:
            write_file(tasks)
            return "Tarea eliminada de manera exitosa."
        elif found is False:
            raise ValueError("El identificador de tarea no existe o enviaste un valor vacío.")
    
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500


if __name__ == '__main__':
    app.run(host="localhost", debug=True)