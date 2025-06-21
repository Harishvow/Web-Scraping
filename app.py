

from flask import Flask,render_template,request


from main import scrape,extract

app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():

    if request.method == "POST":
        url = request.form["floatinglink"]
        source = scrape(url)
        Price = extract(source)
        return render_template('index.html',price=f"{Price} Now")
    return render_template('index.html', price="")

if __name__=="__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)