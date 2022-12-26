import requests

def send_sentence(sentence):
    # Set the URL of the server microservice
    url = "http://localhost:8000/transform"

    # Send an HTTP POST request to the server, including the sentence in the request body
    response = requests.post(url, json={"sentence": sentence})

    # Read the transformed sentence from the response body
    transformed_sentence = response.json()["transformed_sentence"]

    return transformed_sentence




if __name__ == "__main__":
    # Read the value from the console
    value = input("Enter a value: ")

    # Send the value to the server and print the transformed value
    print(send_sentence(value))
