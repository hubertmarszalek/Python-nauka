experience = 2
languages = ['python',  'javascript']
contractType = "b2b"



if experience >= 2 and "python" in languages and "java" in languages:
    if contractType == "b2b" or contractType == "employment":
        print("Kandydat spełnia warunki")
    else:
        print("kandydat nie spełnia warunków")
else:
    print("nie spełnia warunkow")