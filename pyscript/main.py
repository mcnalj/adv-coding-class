import arrr
from pyscript import document

def runCode(event):
    paragraph = document.querySelector("p")
    paragraph.innerText = "Hello World"
    print(event)


# paragraph = document.querySelector("p")
# paragraph.addEventListener("click", runCode)
#paragraph.innerHTML = "Hello World!"
def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english)

