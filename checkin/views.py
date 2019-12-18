from django.views.decorators.http import require_http_methods
from rest_framework.permissions import AllowAny
from checkin.models import WxUser, Comments
from rest_framework.viewsets import ModelViewSet
from .serializers import WxUserSerializer, CommentsSerializer


class CheckInViewSet(ModelViewSet):
    queryset = WxUser.objects.all()
    serializer_class = WxUserSerializer
    permission_classes = (AllowAny, )
    

class CommentViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny, )


'''
登录函数：
'''
def get_user_info_func(user_code):
    api_url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'
    get_url = api_url.format(App_id,App_secret,user_code)
    r = requests.get(get_url)
    return r.json()


@require_http_methods(['POST'])
def user_login_func(request):
    try:
        user_code = request.POST.get('user_code')
        print(user_code)
        if user_code == None:
            print(request.body)
            json_data =  json.loads(request.body)
            user_code = json_data['user_code']
            print(user_code)
    except:
        return JsonResponse({'status':500,'error':'请输入完整数据'})
    try:
        json_data = get_user_info_func(user_code)
        #json_data = {'errcode':0,'openid':'111','session_key':'test'}
        if 'errcode' in json_data:
            return JsonResponse({'status': 500, 'error': '验证错误：' + json_data['errmsg']})
        res = login_or_create_account(json_data)
        return JsonResponse(res)
    except:
        return JsonResponse({'status':500,'error':'无法与微信验证端连接'})


def login_or_create_account(json_data):
    openid = json_data['openid']
    session_key = json_data['session_key']

    try:
        user = User.objects.get(username=openid)
    except:
        user = User.objects.create(
            username=openid,
            password=openid,
        )
    user.session_key = session_key
    user.save()

    try:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        res = {
            'status': 200,
            'token': token
        }
    except:
        res = {
            'status': 500,
            'error': 'jwt验证失败'
        }
    return res

    '''
视图样例：
'''
from django.http import JsonResponse
from rest_framework_jwt.views import APIView
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET','POST']:
            return True
        return obj.user == request.user

class test_view(APIView):
    http_method_names = ['post']  #限制api的访问方式
    authentication_classes = (authentication.SessionAuthentication,JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)       #权限管理

    def post(self,request):                                        #视图函数
        user = request.user.username
        U = User.objects.get(username=user)
        json_data = json.loads(request.body)
        try:
            test = json_data['']
        except:
            return JsonResponse({'status':500,'errmsg':'参数不全'})
        try:
            U.sex = sex
            U.weight = weight
            U.height = height
            U.save()
        except:
            return JsonResponse({'status': 500, 'errmsg': '数据库错误'})
        return JsonResponse({'status':200})