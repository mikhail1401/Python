# This lesson is about HTML, CSS, Jinja
# Jinja - шаблонизатор, позволяющий вставлять в html динамические данные (templating engine)
# php - это язык, который отвечает за перепроцессор html


from flask import Flask, render_template

# the app is our server
app = Flask(__name__)   # in python __name__ holds the name of the current module (main.py)

@app.route('/')
def main():
    names = ["Алекскей", "Михаил Ф.", "София",
             "Михаил А.", "Алиса", "Кристина Н",
             "Кристина Х.", "Маруся", "Елена",
             "Дмитрий", "Ярослав М.", "Ярослав А."]
    return render_template('base.html', title='Main Page', names=names)

@app.route('/students')
def students():
    names = ["Алекскей", "Михаил Ф.", "София",
             "Михаил А.", "Алиса", "Кристина Н",
             "Кристина Х.", "Маруся", "Елена",
             "Дмитрий", "Ярослав М.", "Ярослав А."]
    return render_template('students.html', title='Список всех студентов',
                           names=names)

if __name__ == '__main__':
    app.run()
