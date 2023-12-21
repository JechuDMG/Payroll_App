from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Daily_Sales_Form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = {
            'Timestamp': request.form['timestamp'],
            'Your_first_name': request.form['first_name'],
            'Stops': request.form['stops'],
            'Short_Stories': request.form['short_stories'],
            'Presentations': request.form['presentations'],
            'Asked': request.form['asked'],
            'Ipad': request.form['ipad'],
            'Approval': request.form['approval'],
            'Donation_Amount': request.form['donation_amount'],
            'Email_address': request.form['email'],
            'Date_of_Sales': request.form['date_of_sales'],
            'Badge_Number': request.form['badge_number'],
            'Your_last_name': request.form['last_name'],
            'Sales_ID': request.form['sales_id']
        }

        with open('submitted_forms.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)

        return "Form submitted successfully!"
    else:
        return "Method not allowed!"

if __name__ == '__main__':
    app.run(debug=True)
