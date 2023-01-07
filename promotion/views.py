from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Plan


# Create your views here.


class Welcome(APIView):
    @staticmethod
    def get(request):
        return Response({'message': 'I am Alive'}, status.HTTP_200_OK)


class CreatePlan(APIView):

    def post(self, request):

        name = request.data.get('name')
        amount_options = request.data.get('amountOptions')
        tenure_options = request.data.get('tenureOptions')
        benefit_percentage = request.data.get('benefitPercentage')
        benefit_type = request.data.get('benefitType')

        if not name or not amount_options or not tenure_options or not benefit_percentage or not benefit_type:
            data = {
                'success': False,
                'msg': 'Please enter all the details',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)

        try:
            new_plan = Plan(
                name=name,
                amountOptions=amount_options,
                tenureOptions=tenure_options,
                benefitPercentage=benefit_percentage,
                benefitType=benefit_type
            )
            new_plan.save()
            data = {
                'success': True,
                'msg': 'Plan created successfully',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            data = {
                'success': False,
                'msg': 'Some Error Occurred on our end',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)

