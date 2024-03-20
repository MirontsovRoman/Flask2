from flask import Flask, render_template, abort

app = Flask(__name__)

@app.get('/')
def home():
    return render_template("index.html")


@app.get('/names')
def names():
    entities = list()
    with open("files/names.txt", encoding="utf-8") as f:
        for raw_line in f:
            entities.append(raw_line.strip())
    return render_template("names.html", entities=entities)


@app.route('/table')
def table():
    entities = list()
    with open("files/humans.txt", encoding="utf-8") as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            entities.append({
                'last_name': data[0], 
                'name': data[1],
                'surname': data[2]
            })
    return render_template('table.html', entities=entities)
    
    
@app.route("/users")
def users_list():
    entities = list()
    with open("files/users.txt", encoding="utf-8") as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            entities.append(
                dict(zip(('login', 'last_name', 'name',
                     'surname', 'birth_date', 'phone'), data))
            )
    return render_template('users_list.html', **{'entities': entities})
        
    
@app.route("/users/<login>")
def user_info(login):
    item = None
    with open('files/users.txt', encoding="utf-8") as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            if data[0] == login:
                item = {
                    'login': data[0],
                    'last_name': data[1],
                    'name': data[2],
                    'surname': data[3],
                    'birth_date': data[4],
                    'phone': data[5]
                }
                break
    if item is None:
        abort(404, f'User with login: {login} not found')
    return render_template('user_info.html', item=item)
    
    
    
    
@app.route('/about')
def about():
    return 'About us'


if __name__ == '__main__':
    app.run(debug=True)
    
