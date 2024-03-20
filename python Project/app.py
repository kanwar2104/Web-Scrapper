from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
def substring(unique_strings , content):
    for my_content in unique_strings:
        if(content in my_content or my_content in content):
            return True
        
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        tag = request.form['tag']
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all(tag)
            unique_content = set()
            for element in elements: 
                content = element.text.strip()     
                if substring(unique_content , content) == False:
                    unique_content.add(content)       
            extracted_data = '\n'.join(unique_content)
            return render_template('result.html', data=extracted_data)
        except Exception as e:
            error_message = f"An error occurred: {e}"
            return render_template('index.html', error=error_message)
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)

