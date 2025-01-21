from flask import Flask, render_template, request
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    """Menghitung probabilitas Poisson."""
    probability = (lmbda ** k) * math.exp(-lmbda) / math.factorial(k)
    return probability

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Mengambil input dari form
        lmbda = float(request.form['lmbda'])
        k = int(request.form['k'])

        # Menghitung probabilitas menggunakan rumus Poisson
        probability = poisson_probability(lmbda, k)

        # Penjelasan langkah-langkah
        explanation = f"""
        1. Rumus distribusi Poisson:
           P(X = k) = (λ^k * e^(-λ)) / k!
        2. Substitusi nilai:
           λ = {lmbda}, k = {k}
        3. Hitung:
           - λ^k = {lmbda}^{k} = {lmbda**k}
           - e^(-λ) = e^(-{lmbda}) = {math.exp(-lmbda)}
           - k! = {math.factorial(k)}
        4. Hasil:
           P(X = {k}) = ({lmbda}^{k} * e^(-{lmbda})) / {math.factorial(k)}
                      = {round(probability, 5)}
        """

        return render_template('index.html', result=round(probability, 5), explanation=explanation, lmbda=lmbda, k=k)
    except ValueError:
        return render_template('index.html', error="Input tidak valid. Masukkan angka yang benar.")

if __name__ == '__main__':
    app.run(debug=True)
