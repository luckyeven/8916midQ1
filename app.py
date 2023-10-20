from flask import Flask, request, jsonify, abort

app = Flask(__name__)


students = {}

@app.route('/')
def index():
    return 'API alive'

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    return jsonify(student)

@app.route('/students', methods=['POST'])
def create_student():
    
    student = {
        'id': request.json['id'],
        'name': request.json['name'],
        'grade': request.json['grade'],
    }
    students[student['id']] = student

    return jsonify(student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = students.get(student_id)
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    students[student_id] = student
    return jsonify(student)

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):


    del students[student_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
