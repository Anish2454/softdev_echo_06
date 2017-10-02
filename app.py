'''
Anish Shenoy
SoftDev1 pd7
HW06 -- Echo
2017-10-02
'''


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/response")
def response():
    print "\n\n****request.args****"
    print request.args
    print "****request.headers****"
    print request.headers
    print "****request.method****"
    print request.method
    return render_template("response.html", name=request.args["username"], method=request.method)

if (__name__ == "__main__"):
    app.debug = True;
    app.run()
