from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Plan, Promotion


# Create your views here.


class Welcome(APIView):
    @staticmethod
    def get(request):
        return Response({'message': 'I am Alive'}, status.HTTP_200_OK)


class CreatePlan(APIView):

    @staticmethod
    def post(request):

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
                'data': {
                    'id': new_plan.id,
                    'name': new_plan.name
                }
            }
            return Response(data, status.HTTP_200_OK)
        except Exception as e:
            data = {
                'success': False,
                'msg': 'Some Error Occurred on our end',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)


class CreatePromotion(APIView):
    @staticmethod
    def post(request):
        name = request.data.get("name")
        plan_id = request.data.get('plan_id')
        validity_type = request.data.get('validity_type')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        users_left = request.data.get('users_left')
        benefit_percentage = request.data.get('benefit_percentage')

        if not name or not plan_id or not benefit_percentage or (validity_type not in ['end_date', 'num_of_users']):
            data = {
                'success': False,
                'msg': 'Missing name, plan, validity or benefitPercentage',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)

        if validity_type == 'end_date':
            if not start_date or not end_date:
                data = {
                    'success': False,
                    'msg': 'Enter start Date and End Date',
                    'data': {}
                }
                return Response(data, status.HTTP_200_OK)
            else:
                start_date = datetime.strptime(start_date, '%d-%m-%Y').date()
                end_date = datetime.strptime(end_date, '%d-%m-%Y').date()

        if validity_type == 'num_of_users':
            if not users_left:
                data = {
                    'success': False,
                    'msg': 'Missing number of users',
                    'data': {}
                }
                return Response(data, status.HTTP_200_OK)
        plan = Plan.objects.filter(id=plan_id)
        if not plan:
            return Response({
                'success': False,
                'msg': 'No Such plan Exists',
                'data': {}
            }, status.HTTP_200_OK)
        plan = plan[0]

        try:
            new_promotion = Promotion(
                name=name,
                plan=plan,
                validity_type=validity_type,
                benefitPercentage=benefit_percentage,
                start_date=start_date,
                end_date=end_date,
                users_left=users_left
            )
            new_promotion.save()
            data = {
                'success': True,
                'msg': 'Promotion Created Successfully',
                'data': {
                    'id': new_promotion.id,
                    'name': new_promotion.name
                }
            }
            return Response(data, status.HTTP_200_OK)

        except Exception as e:
            data = {
                'success': False,
                'msg': 'Some error occurred on our end',
                'data': {}
            }
            return Response(data, status.HTTP_200_OK)


class ListAllPlansAndPromotions(APIView):
    @staticmethod
    def get(request):

        all_promotions = Promotion.objects.filter(is_active=True)
        plan_id_to_exclude = set([plan.plan.id for plan in all_promotions])
        all_plans = Plan.objects.filter(is_active=True).exclude(id__in=list(plan_id_to_exclude))

        plans, promotions = [], []

        for promo in all_promotions:
            promotions.append({
                'id': promo.id,
                'name': f'{promo.plan.name}-{promo.name}',
                'validity_type': promo.validity_type,
                'start_date': promo.start_date,
                'end_date': promo.end_date,
                'users_left': promo.users_left,
                'benefit_percentage': promo.benefitPercentage,
                'amount_options': promo.plan.amountOptions,
                'tenure_options': promo.plan.tenureOptions,
                'benefit_type': promo.plan.benefitType
            })

        for plan in all_plans:
            plans.append({
                'id': plan.id,
                'name': plan.name,
                'benefit_percentage': plan.benefitPercentage,
                'amount_options': plan.amountOptions,
                'tenure_options': plan.tenureOptions,
                'benefit_type': plan.benefitType
            })

        data = {
            'success': True,
            'msg': "",
            'data': {
                'promotions': promotions,
                'plans': plans
            }
        }
        return Response(data, status.HTTP_200_OK)
