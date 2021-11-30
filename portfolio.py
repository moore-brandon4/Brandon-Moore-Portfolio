#python --version
#pip install flask


from flask import Flask, render_template  
portfolio = Flask(__name__)             

@portfolio.route("/")                          
def index():                    
    return render_template("index.html")


@portfolio.route("/resume")                          
def resume():                    
    return render_template("resume.html")
    
@portfolio.route("/programming")                          
def programming():                    
    return render_template("programming.html")

@portfolio.route("/development")                          
def development():                    
    return render_template("development.html")        


if __name__ == "__main__":         
    portfolio.run(debug=True)       