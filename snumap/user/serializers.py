from rest_framework import serializers, status
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from snumap.utils import ConflictError

#jwt 토큰 세팅
User = get_user_model()
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

# [ user -> jwt_token ] function
def jwt_token_of(user):
    payload = JWT_PAYLOAD_HANDLER(user)
    jwt_token = JWT_ENCODE_HANDLER(payload)

    return jwt_token

class UserCreateSerializer(serializers.Serializer):
    # Read-only fields
    id = serializers.IntegerField(read_only=True)
    token = serializers.SerializerMethodField()

    # Write-only fields
    email = serializers.EmailField(max_length=100, write_only=True)
    username = serializers.CharField(max_length=25, write_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    
    #profile_image -> s3 설정 이후 추가/회원가입 시 추가 or 프로필 변경 시 추가

    def get_token(self, user):
        return jwt_token_of(user)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise ConflictError({'email': "Already existing email."})

        return value

    def validate(self, data): 
        #validation 필요해지면 추가 ex) username 관련.
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

class UserLoginSerializer(serializers.Serializer):
   # Read-only fields
    id = serializers.IntegerField(read_only=True)
    token = serializers.SerializerMethodField()

    # Write-only fields
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def get_token(self, user):
        return jwt_token_of(user)

    def validate(self, data):
        email = data.pop('email')
        password = data.pop('password')
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("이메일 또는 비밀번호가 잘못되었습니다.")
        else:
            self.instance = user

        return data

    def execute(self):
        update_last_login(None, self.instance)