from flask import Flask, render_template, url_for, request

app=Flask(__name__)

crop_info = {
    "Corn (Maize)": {
        "climate": "Warm temperatures, well-distributed rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Atrazine, Glyphosate, Pyrethroids"
    },
    "Wheat": {
        "climate": "Cool temperatures during the growing season, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Triazole, Imidazole, Pyrethroids"
    },
    "Rice": {
        "climate": "Warm temperatures, high humidity, and abundant water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorantraniliprole, Pyrethroids, Neonicotinoids"
    },
    "Soybeans": {
        "climate": "Warm temperatures, well-drained soils, moderate rainfall.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Glyphosate, Pyrethroids, Neonicotinoids"
    },
    "Potatoes": {
        "climate": "Cool temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorothalonil, Methamidophos, Neonicotinoids"
    },
    "Tomatoes": {
        "climate": "Warm temperatures, ample sunlight, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethrins, Bacillus thuringiensis, Neonicotinoids"
    },
    "Cotton": {
        "climate": "Warm temperatures, long frost-free period, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethroids, Neonicotinoids, Spinosad"
    },
    "Apples": {
        "climate": "Cool to moderate temperatures, well-drained soils, adequate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Carbaryl, Captan, Imidacloprid"
    },
    "Grapes": {
        "climate": "Warm temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Sulfur, Copper compounds, Pyrethroids"
    },
    "Oranges": {
        "climate": "Warm temperatures, subtropical to tropical climate, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Azadirachtin, Imidacloprid, Pyrethroids"
    },
    "Bananas": {
        "climate": "Warm temperatures, high humidity, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Coffee": {
        "climate": "Warm temperatures, high altitude, ample rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Neonicotinoids, Chlorpyrifos, Triazoles"
    },
    "Tea": {
        "climate": "Moderate temperatures, high humidity, well-drained acidic soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethroids, Chlorantraniliprole, Imidacloprid"
    },
    "Sugar Cane": {
        "climate": "Warm temperatures, abundant rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Glyphosate, Glufosinate, Pyrethroids"
    },
    "Carrots": {
        "climate": "Cool temperatures, well-drained soils, consistent moisture.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Methomyl, Spinosad"
    },
    "Lettuce": {
        "climate": "Cool temperatures, well-drained soils, moderate humidity.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorothalonil, Cypermethrin, Imidacloprid"
    },
    "Cabbage": {
        "climate": "Cool temperatures, well-drained soils, moderate humidity.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Bifenthrin, Carbaryl, Diazinon"
    },
    "Broccoli": {
        "climate": "Cool temperatures, well-drained soils, moderate humidity.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Bacillus thuringiensis, Spinosad, Methoxyfenozide"
    },
    "Spinach": {
        "climate": "Cool temperatures, well-drained soils, moderate humidity.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Spinosad, Pyrethroids, Chlorantraniliprole"
    },
    "Cucumbers": {
        "climate": "Warm temperatures, well-drained soils, consistent moisture.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorothalonil, Cypermethrin, Neonicotinoids"
    },
    "Peppers": {
        "climate": "Warm temperatures, well-drained soils, ample sunlight.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Methamidophos, Pyrethrins, Spinosad"
    },
    "Pumpkins": {
        "climate": "Warm temperatures, well-drained soils, consistent moisture.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Cyfluthrin, Deltamethrin"
    },
    "Onions": {
        "climate": "Cool to moderate temperatures, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Pyrethroids, Propiconazole"
    },
    "Squash": {
        "climate": "Warm temperatures, well-drained soils, consistent moisture.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Carbaryl, Pyrethrins, Neonicotinoids"
    },
    "Barley": {
        "climate": "Cool temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Triazole, Imidazole, Pyrethroids"
    },
    "Oats": {
        "climate": "Cool temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Triazole,Imidazole,Pyrethroids"
    },
    "Sorghum": {
        "climate": "Warm temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Atrazine,Glyphosate,Pyrethroids"
    },
    "Sunflowers": {
        "climate": "Warm temperatures, well-drained soils, moderate rainfall or irrigation.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Glyphosate,Pyrethroids,Neonicotinoids"
    },
    "Peanuts": {
        "climate": "Warm temperatures, well-drained sandy soils, moderate rainfall.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Chlorpyrifos,Methamidophos,Neonicotinoids"
    },
    "Cocoa": {
        "climate": "Warm temperatures, high humidity, well-drained soils.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Neonicotinoids,Chlorpyrifos,Triazoles"
    },
    "Almonds": {
        "climate": "Warm temperatures, well-drained soils, low humidity.",
        "fertilizers": "Nitrogen (N),Phosphorus (P),Potassium (K)",
        "pesticides": "Chlorpyrifos,Imidacloprid,Pyrethroids"
    },
    "Walnuts": {
        "climate": "Cool to moderate temperatures, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Carbaryl, Captan, Imidacloprid"
    },
    "Cashews": {
        "climate": "Warm temperatures, high humidity, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Pistachios": {
        "climate": "Warm temperatures, well-drained soils, low humidity.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Imidacloprid, Pyrethroids"
    },
    "Macadamia Nuts": {
        "climate": "Warm temperatures, well-drained soils, high rainfall.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Carbaryl, Pyrethrins, Neonicotinoids"
    },
    "Hazelnuts": {
        "climate": "Cool to moderate temperatures, well-drained soils.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Captan, Imidacloprid"
    },
    "Cranberries": {
        "climate": "Cool temperatures, acidic and well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorothalonil, Methomyl, Spinosad"
    },
    "Blueberries": {
        "climate": "Cool temperatures, acidic and well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Chlorpyrifos, Methomyl, Spinosad"
    },
    "Strawberries": {
        "climate": "Cool temperatures, well-drained soils, ample water.",
        "fertilizers":"Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethrins, Bacillus thuringiensis, Neonicotinoids"
    },
    "Raspberries": {
        "climate": "Cool temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethrins, Bacillus thuringiensis, Neonicotinoids"
    },
    "Blackberries": {
        "climate": "Cool temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Pyrethrins, Bacillus thuringiensis, Neonicotinoids"
    },
    "Avocado": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Mango": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Pineapple": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Kiwi": {
        "climate": "Moderate temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen(N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Papaya": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Guava": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
    "Dragon Fruit": {
        "climate": "Warm temperatures, well-drained soils, ample water.",
        "fertilizers": "Nitrogen (N), Phosphorus (P), Potassium (K)",
        "pesticides": "Mancozeb, Dithiocarbamates, Neonicotinoids"
    },
}


def get_crop_info(crop):
    if crop in crop_info:
        return crop_info[crop]
    else:
        return None

#crop = input("Enter the name of the crop: ").strip()
#crop_details = get_crop_info(crop)
'''
if crop_details:
    print(f"\nClimate: {crop_details['climate']}")
    print("\nFertilizers:")
    for fertilizer in crop_details["fertilizers"]:
        print(fertilizer)
    print("\nPesticides:")
    for pesticide in crop_details["pesticides"]:
        print(pesticide)
else:
    print("Crop not found.")
'''


@app.route('/')
@app.route('/home')
def home():
    return render_template("crop.html")


@app.route('/result', methods=['POST', 'GET'])
def result():
    output = request.form.get("name")
    name=get_crop_info(output)

    return render_template('crop.html', name=list(name.items()))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12345)
