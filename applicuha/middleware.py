import datetime

from django.contrib.auth import logout


class LogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            last_activity = request.session.get('last_activity')
            if last_activity:
                last_activity = datetime.datetime.strptime(last_activity, '%Y-%m-%d %H:%M:%S.%f')
                if last_activity > datetime.datetime.now() - datetime.timedelta(minutes=5):
                    request.session['last_activity'] = str(datetime.datetime.now())
                else:
                    logout(request)

        response = self.get_response(request)
        if request.user.is_authenticated and not request.user.is_superuser:
            request.session['last_activity'] = str(datetime.datetime.now())
        return response
