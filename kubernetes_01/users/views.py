from rest_framework.response import Response
from rest_framework.views import APIView


class HelloKubernetesApiView(APIView):
	def get(self, request, *args, **kwargs):
		obj_user = {
				'name': 'Isaac',
				'username': 'Izaark',
				'github': 'https://github.com/Izaark',
				'country': 'Mexico',
				'city': 'Mexico City',
				'linkedin': 'https://www.linkedin.com/in/isaacflm/'
		}
		response_data = {'message': 'success', 'user': obj_user}
		return Response(response_data)