# 🌱 건강기능식품 분석 웹사이트 🌱

이 웹사이트는 한국인의 조사를 바탕으로 통계를 내며 **건강기능식품**과 **질병**에 대한 분석을 제공합니다. **Django** 기반 웹페이지에서 사용자들에게 건강기능 식품의 추천 및 효능과 용법을 알려주는 정보를 제공합니다.

## 🚀 시작하기

커널 창에서 아래 명령어를 입력하면 웹서버가 시작됩니다:
```bash
python manage.py runserver
```
웹서버가 시작된 후에는 [http://127.0.0.1:8000/nonmodel/about/](http://127.0.0.1:8000/nonmodel/about/) 링크로 접속하여 웹사이트를 이용할 수 있습니다.

## 📊 데이터베이스 구성

- 사용된 데이터베이스: **Oracle**
- 테이블 구성: 최상단 파일의 "minipro 테이블 정의 하는.sql" 파일을 참고하세요.
- 데이터 입력: `nonmodelapp` 폴더 내 `DB_Sql` 디렉토리의 `prod_insert.ipynb`를 사용하여 csv 파일에서 데이터를 추출하여 DB에 저장하였습니다.

## 사용된 라이브러리

아래는 해당 프로젝트에서 사용된 라이브러리와 그 버전들입니다:

- **anyio**: 3.7.0
- **argon2-cffi**: 21.3.0
- **argon2-cffi-bindings**: 21.2.0
- **arrow**: 1.2.3
- **asgiref**: 3.7.2
- **asttokens**: 2.2.1
- **attrs**: 23.1.0
- **backcall**: 0.2.0
- **beautifulsoup4**: 4.12.2
- **bleach**: 6.0.0
- **branca**: 0.6.0
- **brotli-python**: 1.0.9
- **ca-certificates**: 2023.5.7
- **certifi**: 2023.5.7
- **cffi**: 1.15.1
- **charset-normalizer**: 3.2.0
- **colorama**: 0.4.6
- **comm**: 0.1.3
- **contourpy**: 1.1.0
- **cx_oracle**: 8.3.0
- **cycler**: 0.11.0
- **debugpy**: 1.6.7
- **decorator**: 5.1.1
- **defusedxml**: 0.7.1
- **django**: 4.0.1
- **et-xmlfile**: 1.1.0
- **exceptiongroup**: 1.1.1
- **executing**: 1.2.0
- **fastjsonschema**: 2.17.1
- **folium**: 0.14.0
- **fonttools**: 4.40.0
- **fqdn**: 1.5.1
- **greenlet**: 2.0.2
- **idna**: 3.4
- **importlib-metadata**: 6.7.0
- **importlib-resources**: 5.12.0
- **iniconfig**: 1.1.1
- **intel-openmp**: 2023.1.0
- **ipykernel**: 6.23.3
- **ipython**: 8.14.0
- **ipython-genutils**: 0.2.0
- **ipywidgets**: 8.0.6
- **isoduration**: 20.11.0
- **jedi**: 0.18.2
- **jinja2**: 3.1.2
- **joblib**: 1.3.1
- **jsonpointer**: 2.4
- **jsonschema**: 4.17.3
- **jupyter**: 1.0.0
- **jupyter-client**: 8.3.0
- **jupyter-console**: 6.6.3
- **jupyter-core**: 5.3.1
- **jupyter-events**: 0.6.3
- **jupyter-server**: 2.7.0
- **jupyter-server-terminals**: 0.4.4
- **jupyterlab-pygments**: 0.2.2
- **jupyterlab-widgets**: 3.0.7
- **kiwisolver**: 1.4.4
- **libblas**: 3.9.0
- **libcblas**: 3.9.0
- **liblapack**: 3.9.0
- **markupsafe**: 2.1.3
- **matplotlib**: 3.7.1
- **matplotlib-inline**: 0.1.6
- **mistune**: 3.0.1
- **mkl**: 2020.4
- **nbclassic**: 1.0.0
- **nbclient**: 0.8.0
- **nbconvert**: 7.6.0
- **nbformat**: 5.9.0
- **nest-asyncio**: 1.5.6
- **notebook**: 6.5.4
- **notebook-shim**: 0.2.3
- **numpy**: 1.25.0
- **openpyxl**: 3.1.2
- **openssl**: 3.0.9
- **overrides**: 7.3.1
- **packaging**: 23.1
- **pandas**: 2.0.3
- **pandocfilters**: 1.5.0
- **parso**: 0.8.3
- **pickleshare**: 0.7.5
- **pillow**: 9.5.0
- **pip**: 23.1.2
- **platformdirs**: 3.8.0
- **pluggy**: 1.0.0
- **prometheus-client**: 0.17.0
- **prompt-toolkit**: 3.0.38
- **psutil**: 5.9.5
- **pure-eval**: 0.2.2
- **pycparser**: 2.21
- **pygments**: 2.15.1
- **pyparsing**: 3.1.0
- **pyrsistent**: 0.19.3
- **pysocks**: 1.7.1
- **pytest**: 7.3.1
- **python**: 3.9.16
- **python-dateutil**: 2.8.2
- **python-json-logger**: 2.0.7
- **python-tzdata**: 2023.3
- **python_abi**: 3.9
- **pytz**: 2023.3
- **pywin32**: 306
- **pywinpty**: 2.0.10
- **pyyaml**: 6.0
- **pyzmq**: 25.1.0
- **qtconsole**: 5.4.3
- **qtpy**: 2.3.1



