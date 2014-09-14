#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from django.template import Context
from django.template.loader import get_template
import offline
from views import offline_view


class OfflineMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated() and offline.is_enabled() \
            and not request.user.is_staff:
            return offline_view(request)
        elif not (hasattr(request, 'user')
                  and request.user.is_authenticated()) \
            and offline.is_enabled():
            return offline_view(request)
        return

    def process_response(self, request, response):
        if hasattr(request, 'user') and offline.is_enabled() \
            and request.user.is_staff \
            and self.is_html_response(response):
            template = get_template('admin_notification.html')
            warning_message = template.render(Context())
            response.content = re.sub(r'<body.*>', '\g<0>'
                    + warning_message, response.content.decode('utf-8'))
        return response

    def is_html_response(self, response):
        return response['Content-Type'].startswith('text/html')



			
