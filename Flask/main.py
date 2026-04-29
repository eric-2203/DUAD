#Crea un API con Flask de que permita un CRUD (Create, Read, Update, Delete) de tareas. 
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Bienvenido al API de Tareas!</h1>"

valid_status = ["pending", "in progress", "completed"]

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


@app.route("/tasks", methods=['GET'])
def show_tasks():
    tasks = read_file()
    tasks_filter = request.args.get("status")
    if tasks_filter:
        tasks = list(
            filter(lambda task: task["status"] == tasks_filter.lower(), tasks)
        )
    return jsonify(tasks)

@app.route("/tasks", methods=['POST'])
def register_task():
    tasks = read_file()
    try:
        if "identifier" not in request.json or request.json["identifier"] == "":
            raise ValueError("Hace falta el identificador de la tarea.")
        
        if "title" not in request.json or request.json["title"] == "":
            raise ValueError("Hace falta el titulo de la tarea.")
        
        if "description" not in request.json or request.json["description"] == "":
            raise ValueError("Hace falta la descripcion de la tarea.")
        
        if "status" not in request.json or request.json["status"] == "":
            raise ValueError("Hace falta el estado de la tarea.")
        if request.json["status"].lower() not in valid_status:
            raise ValueError("El estado ingresado no es valido. Ingrese un estado valido.")
        
        for task in tasks:
            if task["identifier"] == request.json["identifier"]:
                raise ValueError("Este identificador de tarea ya existe. Inserta un identificador nuevo.")

        tasks.append(
            {
                "identifier": request.json["identifier"],
                "title": request.json["title"],
                "description": request.json["description"],
                "status": request.json["status"].lower()
            }
        )

        write_file(tasks)
        return jsonify(tasks), 201
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
    
@app.route("/tasks/<id>", methods=['PUT'])
def edit_task(id):
    tasks = read_file()
    found = False
    try: 

        if "title" not in request.json or request.json["title"] == "":
            raise ValueError("Hace falta el titulo de la tarea.")
        
        if "description" not in request.json or request.json["description"] == "":
            raise ValueError("Hace falta la descripcion de la tarea.")
        
        if "status" not in request.json or request.json["status"] == "":
            raise ValueError("Hace falta el estado de la tarea.")
        if request.json["status"].lower() not in valid_status:
            raise ValueError("El estado ingresado no es valido. Ingrese un estado valido.")
        
        for task in tasks:
            if task["identifier"] == id:
                task["title"] = request.json["title"]
                task["description"] = request.json["description"]
                task["status"] = request.json["status"].lower()
                found = True
                break
        if found is True:
            write_file(tasks)
            return jsonify(tasks)
        elif found == False:
            raise ValueError("El identificador de tarea no existe o enviaste un valor vacío.")


    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500


@app.route("/tasks/<id>", methods=['DELETE'])
def delete_task(id):
    tasks = read_file()
    found = False
    try:  
        for task in tasks:
            if task["identifier"] == id:
                tasks.remove(task)
                found = True
                break
        if found is True:
            write_file(tasks)
            return jsonify(tasks)
        elif found is False:
            raise ValueError("El identificador de tarea no existe o enviaste un valor vacío.")
    
    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500


if __name__ == '__main__':
    app.run(host="localhost", debug=True)