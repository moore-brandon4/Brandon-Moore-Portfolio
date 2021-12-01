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
    

@portfolio.route("/filesanddemos")                          
def filesanddemos():                    
    return render_template("filesanddemos.html")        


if __name__ == "__main__":         
    portfolio.run(debug=True)       