from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .tasks import process_webhook
from .serializers import WebhookRequestSerializer

import logging

logger = logging.getLogger(__name__)  # Логирование

class WebhookView(APIView):
    def post(self, request):
        try:
            data = WebhookRequestSerializer(**request.data)
            process_webhook.delay(data.message, str(data.callback_url))
            return Response({"message": "Accepted"}, status=status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

