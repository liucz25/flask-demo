from flask import Flask,make_response,request,session,redirect,url_for,render_template


"""
Cookies
"""
app=Flask(__name__)
@app.route('/set_cookies')
def set_cookies():
    resp=make_response('success')
    resp.set_cookie("aaa_key","aaa_value",max_age=3600)
    return resp
@app.route('/get_cookies')
def get_cookies():
    cookie_1 = request.cookies.get("aaa_key")
    return cookie_1

@app.route('/delete_cookies')
def del_cookies():
    resp=make_response('del success')
    resp.delete_cookie("aaa_key")
    return resp



if __name__=="__main__":
    # app.run(debug=True)
    app.run(debug=True,host='0.0.0.0',port=80,threaded=True)
    