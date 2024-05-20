from flask import Flask, render_template, request

app=Flask(__name__)

diseases = {
    'Powdery Mildew': {'White powdery spots on leaves stems and flowers.', 'Leaves may curl or distort.'},
    'Downy Mildew': {'Yellow or pale green spots on upper leaf surfaces with fuzzy grayish growth on the undersides.'},
    'Late Blight': {'Dark water-soaked lesions on leaves and stems which turn brown and papery.', 'White mold may develop in humid conditions.'},
    'Fusarium Wilt': {'Yellowing and wilting of leaves often starting with lower leaves.', 'Dark streaks may appear on stems.'},
    'Verticillium Wilt': {'Wilting of leaves usually on one side of the plant.', 'Yellowing and browning of leaves.'},
    'Anthracnose': {'Dark sunken lesions on leaves stems and fruits.', 'Pinkish spore masses in wet conditions.'},
    'Root Rot': {'Yellowing and wilting of leaves.', 'Stunted growth.', 'Decayed roots.'},
    'Botrytis Blight (Gray Mold)': {'Gray fuzzy mold on flowers fruits and stems.', 'Infected tissues become water-soaked and may rot.'},
    'Rust': {'Orange to reddish-brown powdery pustules on leaves.', 'stems and fruits.'},
    'Bacterial Leaf Spot': {'Small dark lesions with yellow halos on leaves.', 'Lesions may coalesce and cause leaf drop.'}
}

# Function to predict the disease
def predict_disease(symptoms):
    matching_diseases = set()
    for disease, disease_symptoms in diseases.items():
        if all(symptom in disease_symptoms for symptom in symptoms.split(', ')):  # Add space after comma
            matching_diseases.add(disease)
    return matching_diseases
'''
# Example usage:
symptoms = input("Enter the symptoms: ")
predicted_diseases = predict_disease(symptoms)
if predicted_diseases:
    print("The predicted diseases are:")
    for disease in predicted_diseases:
        print("- " + disease)
else:
    print("No matching diseases found.")
'''

@app.route('/')
@app.route('/home')
def home():
    return render_template("disp.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.get("name")
    name=list(predict_disease(output))
    name=name[0]

    return render_template('disp.html', name=name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12543)
