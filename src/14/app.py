from flask import Flask,g,request,flash,render_template,redirect
import os
import flask_sijax

"""
FLASK Sijax
"""
app=Flask(__name__)


path=os.path.join('.',os.path.dirname(__file__),'static/js/sijax')
app.config['SIJAX_STATIC_PATH']=path
app.config['SIJAX_JSON_URI']='/static/js/sijax/json2.js'

flask_sijax.Sijax(app)

@app.route('/')
def hello():    
    return "Hello World!<br /><a href='/sijax'>Go to Sijax</a>"
@flask_sijax.route(app,"/sijax")
def hello_sijax():
    def hello_handler(obj_response,hello_form,hello_to):
        obj_response.alert('Hello from %s to %s'%(hello_form,hello_to))
        obj_response.css('a','color','green')
    def goodbye_handler(obj_response):
        obj_response.alert('GoodBye , whoever you are.')
        obj_response.css('a','color','red')
    if g.sijax.is_sijax_request:
        g.sijax.register_callback('say_hello',hello_handler)
        g.sijax.register_callback('say_goodbye',goodbye_handler)
        return g.sijax.process_request()
    else:
        return render_template('sijaxexample.html')
if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
