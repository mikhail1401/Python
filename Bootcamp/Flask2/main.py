# This lesson is about HTML, CSS, Jinja
# Jinja - шаблонизатор (templating engine), позволяющий вставлять в html динамические данные
# php - это язык, который отвечает за перепроцессор html


from flask import Flask, render_template

# the app is our server
app = Flask(__name__)   # in python __name__ holds the name of the current module (main.py)

@app.route('/')
def main():
    context = {
        "title": "Главная страница",
        "author_name": "Mikhail"
    }
    return render_template('base.html', **context)

@app.route('/students')
def students():
    names = ["Алекскей", "Михаил Ф.", "София",
             "Михаил А.", "Алиса", "Кристина Н",
             "Кристина Х.", "Маруся", "Елена",
             "Дмитрий", "Ярослав М.", "Ярослав А."]
    return render_template('students.html', title='Список всех студентов',
                           names=names)

@app.route('/test_super')
def test_super():
    author_name = "Mikhail"
    return render_template('test_super.html', author_name=author_name)

if __name__ == '__main__':
    app.run()
