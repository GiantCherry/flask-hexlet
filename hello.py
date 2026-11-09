from flask import Flask

app = Flask(__name__)

@app.route('/')
def index() -> str:
    greet_with_link = """<h1>Hello, world!</h1>
        <p><a href="user/Вася/Пупкин">Push me</a></p>"""
    return greet_with_link

@app.route('/user/<surname>/<name>')
def get_user(name, surname):
    personal_instrict = f"""<h1>Привет, {surname} {name}!<h/1>
    <p>Измени имя пользователя в адресной строке и перезагрузи страницу</p>"""
    return personal_instrict

if __name__ == '__main__':
    app.run(debug=True)