from flask import Flask,render_template
"""
模板
"""
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index3.html")

@app.route('/data/')
def show_data():
    t_int = 18,
    t_str = "curry"
    t_list = [1,2,3,4,5,6,2,3,1]
    t_dict={
        'name' : "durant",
        'age' : 25
    }
    return render_template("index4.html",
                           
                           my_int=t_int,
                           my_str=t_str,
                           my_list=t_list,
                           my_dict=t_dict)
# @app.route('/data2/')
# def show_data2():
#     t_int = 18,
#     t_str = "curry"
#     t_list = [1,2,3,4,5,6,2,3,1]
#     t_dict={
#         'name' : "durant",
#         'age' : 25
#     }
#     return render_template("index4.html",
                           
#                            t_int   #这样不行
#                           )




if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    