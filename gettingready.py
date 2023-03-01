from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/index/<title>')
def index1(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', title=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    proflist = ['инженер-исследователь', 'пилот', 'строитель',
                'экзобиолог', 'врач', 'инженер по терраформированию',
                'климатолог', 'специалист по радиационной защите',
                'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения',
                'метеоролог', 'оператор марсохода', 'киберинженер',
                'штурман', 'пилот дронов']
    return render_template('list_prof.html', title=f"127.0.0.1:8080/list_prof/{list}", list0=list,
                           proflist=proflist)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')