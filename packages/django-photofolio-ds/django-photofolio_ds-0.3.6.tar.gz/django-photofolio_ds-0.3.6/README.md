# django-photofolio_ds

django-photofolio_ds 는 photofolio-pro v4.8.0을 장고에 맞게 포팅한 장고앱이다.

## 프로젝트에 설치하기
1. settings.py에 다음 설정을 추가한다.
```python
import os
...
INSTALLED_APPS = [
    ...
    'demian_parts',
    'photofolio',
]
...
# static 파일을 _static 폴더에 저장하도록 설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '_static/'),
]
...
# 팝업창 모듈에서 이미지를 업로드 하기 위해
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
X_FRAME_OPTIONS = 'SAMEORIGIN'
```

2. 프로젝트의 urls.py에 다음을 추가한다.
```python
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
...
urlpatterns = [
    ...
    path('', include('photofolio.urls')),
]
# 팝업창 모듈에서 이미지를 업로드 하기 위해
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

3. 데이터 베이스를 생성한다.
```commandline
python manage.py makemigrations photofolio demian_parts
python manage.py migrate
python manage.py createsuperuser
```

4. 프로젝트의 구조를 생성한다.
```text
_data 폴더를 생성하고 contents.py내에 데이터를 형식에 맞게 입력한다.
_static 폴더를 생성하고 각종 이미지 등을 형식에 맞게 저장한다.
필요하면 admin으로 접속하여 팝업창을 생성한다.
```

***

### 참고 : SCSS 설치하기 - 프로젝트에 SCSS를 설치해야 앱이 작동한다.    
https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/   
1. django_compressor, django-libsass를 설치한다. (photofolio 앱을 설치하면 자동 설치)
```commandline
pip install django_compressor django-libsass
```

2. settings.py에 다음 세팅을 추가하여 compressor가 캐시할 수 있도록한다.
```python
import os
INSTALLED_APPS = [
    ...
    'compressor',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

# compressor 앱을 실행하기 위해서는 STATIC_ROOT가 설정되어 있어야 한다.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
