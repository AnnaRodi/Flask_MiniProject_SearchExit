from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['get', 'post'])  #главная
def index():
    return render_template('index.html')

@app.route('/room', methods = ['get', 'post'])  #выбор комнаты
@app.route('/room/<int:room_number>', methods = ['get', 'post'])
def choose_room():
    room_number = 'start'
    if request.method =='POST':
        room_number=request.form.get('message')
    return render_template('choose_room.html', room_number = room_number)


@app.route('/plan', methods = ['get', 'post']) #navbar  план замка
def plan():
    return render_template('plan.html')

@app.route('/gold', methods = ['get', 'post']) #navbar  сокровище
def gold():
    return render_template('gold.html')

@app.route('/skelet', methods = ['get', 'post'])  #navbar  скелет
def skelet():
    return render_template('skelet.html')



if __name__=='__main__':
    app.run(debug=True)

