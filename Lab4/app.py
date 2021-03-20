from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    main_title = {'title': 'Strona Głowna'}
    main_content = {'data': '20.03.2021', 'author': 'Administrator', 'content': 'Pierwszy wpis na stronie głównej'}
    return render_template('index.html', title=main_title['title'], data=main_content['data'],
                           author=main_content['author'], content=main_content['content'])


@app.route("/about")
def about():
    return render_template('omnie.html')


@app.route("/info")
def info():
    blog = [{
        'autor': {'username': 'Wojciech Pietruszyński'},
        'body': 'Flask jest fajnym narzędziem'},
        {
            'autor': {'username': 'Janek kowalski'},
            'body': 'Bootstrap pomoże w kreowaniu szablonu'
        }]
    return render_template('informacje.html', blog=blog)


@app.route("/content")
def content():
    content_title = {'title': 'Zawartość'}
    content_date = {'content': 'Pierwszy wpis w szablonie content'}
    return render_template('kontent.html', title=content_title['title'], content=content_date['content']) \



if __name__ == "__main__":
    app.run()
