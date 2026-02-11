class SimpleMiddleware:
	def __init__ (self,get_response):
		self.get_response = get_response

	def __call__ (self, request):
		print("logica antes da view")
		print(f"caminho {request.path} ")

		response = self.get_response(request)

		print("logica apos a view")

		return response

class DetailMiddleware:
	def __init__ (self, get_response):
		self.get_response = get_response

	def process_view (request, view_func, view_args, view_kwargs)
		return f" nome da view : {view_func}"