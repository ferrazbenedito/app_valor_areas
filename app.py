from flask import Flask, render_template
from bokeh.embed import server_document
import panel as pn
from panel_app import create_panel_app

app = Flask(__name__)

@app.route('/')
def index():
    # Start the Panel app in a Bokeh server
    panel_app = create_panel_app()
    server = pn.serve(panel_app, start=False, port=5006, show=False)
    server.start()
    
    # Embed the Panel app in the HTML template using the Bokeh server_document function
    script = server_document("https://github.com/ferrazbenedito/app_valor_areas/blob/main/panel_app.py")

    return render_template('index.html', script=script)

if __name__ == '__main__':
    app.run(port=8000)
