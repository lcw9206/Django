from django import forms
from django.template.loader import render_to_string
from django.conf import settings
import re


class NaverMapPointWidget(forms.TextInput):
    BASE_LAT, BASE_LNG = '37.497921', '127.027636'

    def render(self, name, value, attrs):
        width = str(self.attrs.get('width', 800))   # attrs dict에 width가 존재하지 않으면 default = 800
        height = str(self.attrs.get('height', 600))
        if width.isdigit(): width += 'px'
        if height.isdigit(): height += 'px'

        context = {
            'naver_client_id' : settings.NAVER_CLIENT_ID,
            'id' : attrs['id'],     # 현재 FormField의 html ID : id_lnglat
            'width' : width, 'height' : height,
            'base_lat' : self.BASE_LAT, 'base_lng' : self.BASE_LNG
        }

        # value로 저장된 위도, 경도를 넘겨 지정된 위치를 마킹함.
        if value:
            try:
                lng, lat = re.findall(r'[+-]?[\d\.]+', value)
                context.update({'base_lat' : lat, 'base_lng' : lng})
            except (IndexError, ValueError):
                pass

            attrs['readonly'] = 'readonly'  # 위도, 경도 수정 불가

        '''
            render는 httpresponse의 인스턴스를 리턴해주므로 render_to_string을 사용해
            필요한 문자열을 리턴받는다.
        '''
        html = render_to_string('widgets/naver_map_point_widget.html', context)

        parent_html = super().render(name, value, attrs)    # TextInput으로 생성되는 html

        return parent_html + html