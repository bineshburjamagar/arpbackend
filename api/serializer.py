from rest_framework import serializers

class TextAnalysisSerializer(serializers.Serializer):
    """
    Serializer to validate input and format output.
    """
    # Input field
    text = serializers.CharField(
        max_length=5000, 
        required=True, 
        help_text="Enter the text/diary entry to analyze."
    )
    
    # Output fields (read_only=True means the user doesn't send these)
    result = serializers.CharField(read_only=True)
    confidence = serializers.CharField(read_only=True)
    is_depressed = serializers.BooleanField(read_only=True)