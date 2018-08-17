from django.http import HttpResponse
import CaptchaWeb.captcha_predict as captcha_predict


def check_captcha(request):
    url = request.GET['url']
    captcha = captcha_predict.predict_from_url(url)
    return HttpResponse(captcha)
