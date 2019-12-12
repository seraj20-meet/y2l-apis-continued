from flask import Flask, render_template, request
import requests, json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
	image_url = request.form['url-input']
	headers = {'Authorization': 'Key <serajoo>'}



# putting everything together; sending the request!
	
	api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"

# this is content of the message(data) you are sending to clarifai
	data ={"inputs": [
	{
	"data": {
	"image": {"url": "https://samples.clarifai.com/metro-north.jpg"
          }
        }
      }
    ]}

# putting everything together; sending the request!
	response = requests.post(api_url, headers=headers, data=json.dumps(data))



    
	return render_template('home.html', results=response.content)

if __name__ == '__main__':
	app.run(debug=True)