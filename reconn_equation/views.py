from django.shortcuts import render
import cv2
import numpy as np
from . import solver
import base64
from django.http import JsonResponse
from django.shortcuts import render
from io import BytesIO

#Solve the expression entered as image
def process_expression(image):
    # Convert base64 image data to numpy array
    nparr = np.frombuffer(image.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) 
    expression = solver.extract(img)
    solution = solver.solve_expression(expression)

    return expression, solution



#Solve the quadratic equation entered as image
'''def process_quadratic_eq(image):
    nparr = np.frombuffer(image.getvalue(), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR) 
    equation = solver.extract(img)
    equation, solution = solver.solve_linear_equation(equation)

    return equation, solution
    
'''




def index(request):
    return render(request, 'index.html')     


def predict(request):
    operation = BytesIO(base64.urlsafe_b64decode(request.POST['operation']))

    operation,solution = process_expression(operation)
  
    return JsonResponse({
        'operation': operation,
        'solution': solution
    })