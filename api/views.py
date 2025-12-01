from .classifier import DepressionClassifier
from api.serializer import TextAnalysisSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Initialize the model once when the server starts 
# (In production, consider doing this in apps.py ready() method)
classifier = DepressionClassifier()

class AnalyzeDepressionView(APIView):
    """
    API View that receives text and returns a depression classification.
    """
    
    def post(self, request):
        serializer = TextAnalysisSerializer(data=request.data)
        
        if serializer.is_valid():
            input_text = serializer.validated_data['text']
            
            # Call our ML logic
            prediction_data = classifier.predict(input_text)
            
            # Construct response
            response_data = {
                "text": input_text,
                "result": prediction_data['label'],
                "is_depressed": prediction_data['is_depressed'],
                "confidence": prediction_data['confidence']
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)