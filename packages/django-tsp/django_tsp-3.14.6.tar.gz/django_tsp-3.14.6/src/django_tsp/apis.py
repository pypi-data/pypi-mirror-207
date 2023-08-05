from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
from drf_spectacular.utils import extend_schema
from .services import create_tsp_problem, publish_tsp_sloution
from .serializers import LocationSerializer 


class SolverApi(APIView):
    class InputSolverSerializer(serializers.Serializer):
        locations = LocationSerializer(many=True)
        num_vehicles = serializers.FloatField(default=1)
        depot = serializers.FloatField(default=0)

    @extend_schema(request=InputSolverSerializer)
    def post(self, request):
        serializer = self.InputSolverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            create_tsp_problem(
                request.data
            )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(status=status.HTTP_204_NO_CONTENT)

class WebhookApi(APIView):
    class InputSerializer(serializers.Serializer):
        locations = serializers.ListSerializer(child=serializers.CharField())
        id = serializers.CharField()

    @extend_schema(request=InputSerializer)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            publish_tsp_sloution(
                request.data
            )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(status=status.HTTP_204_NO_CONTENT)