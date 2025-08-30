from flask import Flask, render_template, request
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/", methods=["GET", "POST"])
def add_numbers():
    result = None
    pasd = None
    Dean = None
    Grades = ["Prelim exam grade", "Quizzes grade", "Requirement grade", "recitation grade"]
    n_inputs = 4  # Amount of inputs
    n_inputsabsent = 1
    if request.method == "POST": # if user inserts numbers and clicks submit
        numbers = [
            request.form.get(g, type=float)
            for g in Grades
        ]
        
        numbers_absents = [
            request.form.get(f"numabsents{ i }", type=float)
            for i in range(1, n_inputsabsent + 1)
        ]
        if numbers_absents[0] > 4:
            result = "failed.."
        elif None in numbers or None in numbers_absents: # error when wrong number format
            result = "please enter valid numbers"
            #   ok so, Deduct is for the base grade.
            #   it's for every absent you deduct 10 points from the base grade of 100
            # 
            #  
        else:                   
            BaseGrade = 100
            Deduct = request.form.get("numabsents1", type=float) * 10
            attendance = BaseGrade - Deduct
            #Below classtanding
            Quiz = request.form.get("Quizzes grade", type=float) * .40
            Requirments = request.form.get("Requirement grade", type=float) * .30
            Recitation = request.form.get("recitation grade", type=float) * .30
            Standing = Quiz + Requirments + Recitation
            #Prelim grade below
            PXgrade = request.form.get("Prelim exam grade", type=float) * .60
            ATgrade = attendance * 0.10 
            CSgrade = Standing * .30
            prelim = PXgrade + ATgrade + CSgrade
            #Final grade below
            Pre = prelim *.20
            Mid = .30
            Fin = .50
            pasd = round((75 - Pre) / (Mid + Fin), 2)
            Dean = round((90 - Pre) / (Mid + Fin), 2)
            result = prelim
    return render_template("index.html",  result=result, n_inputs=n_inputs, n_inputsabsent=n_inputsabsent, pasd=pasd, Dean=Dean, Grades=Grades)

if __name__ == "__main__":
    app.run(debug=True)