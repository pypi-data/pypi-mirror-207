from rest_framework.renderers import JSONRenderer
from djangorestframework_camel_case.render import CamelCaseJSONRenderer  # type: ignore
from ..http import USER_AGENT


class CustomJsonRenderer(CamelCaseJSONRenderer):
    def render(self, data, *args, **kwargs):
        request = kwargs.get("request")
        if not request:
            return super().render(data, *args, **kwargs)

        # Avoid camelizing the response for requests from internal services
        user_agent = request.headers.get("User-Agent")
        if user_agent == USER_AGENT:
            return super(JSONRenderer, self).render(data, *args, **kwargs)

        return super().render(data, *args, **kwargs)
